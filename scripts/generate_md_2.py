from typing import Any
from pathlib import Path
import re
from urllib.parse import quote
from functools import cmp_to_key

import yaml
from loguru import logger
from mako.template import Template
from mako.runtime import Context
from io import StringIO


def parse_problem_dir(problem_dir: Path) -> Any:
    with open(problem_dir / "problem-meta.yaml", "r") as f:
        meta_data = yaml.load(f, yaml.Loader)

    def get_solution_num(problem_dir: Path) -> int:
        t = list(problem_dir.glob("solution_v*.*"))

        if len(t) == 0:
            return 1

        return max(
            map(
                lambda x: int(re.match("^solution_v(.*?)\\.(.*?)$", x.name).group(1)), t  # type: ignore
            )
        )

    solution_num = get_solution_num(problem_dir)

    solutions = []
    for solution_idx in range(solution_num):
        if solution_idx == 0:
            solutions.append(
                {
                    "Readme": quote(
                        str(
                            problem_dir / "readme.md"
                            if (problem_dir / "readme.md").exists()
                            else ""
                        )
                    ),
                    "C++": quote(
                        str(
                            problem_dir / "solution.cpp"
                            if (problem_dir / "solution.cpp").exists()
                            else ""
                        )
                    ),
                    "Python": quote(
                        str(
                            problem_dir / "solution.py"
                            if (problem_dir / "solution.py").exists()
                            else ""
                        )
                    ),
                }
            )
        else:
            solutions.append(
                {
                    "Readme": quote(
                        str(
                            problem_dir / "readme_v{}.md"
                            if (problem_dir / "readme_v{}.md").exists()
                            else ""
                        )
                    ),
                    "C++": quote(
                        str(
                            problem_dir / "solution_v{}.cpp".format(solution_idx + 1)
                            if (
                                problem_dir
                                / "solution_v{}.cpp".format(solution_idx + 1)
                            ).exists()
                            else ""
                        )
                    ),
                    "Python": quote(
                        str(
                            problem_dir / "solution_v{}.py".format(solution_idx + 1)
                            if (
                                problem_dir / "solution_v{}.py".format(solution_idx + 1)
                            ).exists()
                            else ""
                        )
                    ),
                }
            )

    return {
        "ID": meta_data["META"]["ID"],
        "TITLE_CN": meta_data["META"]["TITLE_CN"],
        "URL": meta_data["META"]["URL"],
        "HARD_LEVEL": meta_data["META"]["HARD_LEVEL"],
        "SOLUTIONS": solutions,
    }


def parse_problemset_dir(problemset_dir: Path) -> Any:
    return list(map(parse_problem_dir, problemset_dir.iterdir()))


def sort_problemset(problemset: list[Any]):

    def my_cmp(a: Any, b: Any) -> int:
        a = str(a["ID"])
        b = str(b["ID"])

        if a.startswith("L") and b.startswith("L"):
            return int(a[4:]) - int(b[4:])

        if a.startswith("L"):
            return 1

        if b.startswith("L"):
            return -1

        return int(a) - int(b)

    return sorted(problemset, key=cmp_to_key(my_cmp))


def main() -> None:
    logger.info("program begin")

    problemset_dir_path = Path("../problemset")
    logger.info("problem set path = {}", str(problemset_dir_path))

    problemset = parse_problemset_dir(problemset_dir_path)

    # Sort
    problemset = sort_problemset(problemset)

    problem_num = len(problemset)

    logger.info("problem num = {}", problem_num)

    # write template
    buf = StringIO()
    my_template = Template(filename="./template.md")
    ctx = Context(buf, problem_num=problem_num, problemset=problemset)

    my_template.render_context(ctx)
    print(buf.getvalue())
    with open("../docs/problemset.md", "w") as f:
        f.write(buf.getvalue())

    logger.info("program end")


if __name__ == "__main__":
    main()
