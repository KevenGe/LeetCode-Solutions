""" 从JSON文档中生成markdown文件
"""

import json
import pathlib


def main():
    problemset_json_path = pathlib.Path("docs\\problems.json")
    contest_json_path = pathlib.Path("docs\\contests.json")

    with open(str(problemset_json_path), "r") as f:
        problemsets = json.load(f)

    with open(str(contest_json_path), "r", encoding="utf-8") as f:
        contest_dict = json.load(f)

    # problem set

    problemset_md = []
    problemset_md.append("# 题目集合\n")
    problemset_md.append("\n")
    problemset_md.append("| 题目 | 难度 | 题解 | C++ | Python |\n")
    problemset_md.append("| -- | -- | -- | -- | -- |\n")

    cpp_solution_count = 0
    py_solution_count = 0
    solution_count = 0
    question_count = 0

    for problem in problemsets:
        origin_str = problem["origin_str"]
        difficulty = problem["difficulty"]
        url = "https://leetcode.cn" + problem["href"]

        has_tijie = ""
        if len(list(pathlib.Path("./problemset/" + origin_str).glob("*.md"))) != 0:
            has_tijie = "\u2713"

        has_cpp_solution = ""
        if len(list(pathlib.Path("./problemset/" + origin_str).glob("*.cpp"))) != 0:
            has_cpp_solution = "\u2713"
            cpp_solution_count += 1

        has_py_solution = ""
        if len(list(pathlib.Path("./problemset/" + origin_str).glob("*.py"))) != 0:
            has_py_solution = "\u2713"
            py_solution_count += 1

        is_display = False
        if has_cpp_solution != "" or has_py_solution != "":
            is_display = True
            solution_count += 1

        question_count += 1

        if is_display:
            problemset_md.append(
                f"| [{origin_str}]({url}) | {difficulty} | {has_tijie} | {has_cpp_solution} | {has_py_solution} |\n"
            )

    problemset_md.insert(
        1,
        f"完成：{solution_count}/{question_count}={(solution_count / question_count):.2f}, C++: {cpp_solution_count}, Python: {py_solution_count}\n",
    )

    with open("./docs/problems.md", "w", encoding="utf-8") as f:
        f.writelines(problemset_md)

    # contest
    contest_md = []

    contest_md.append("# 竞赛集合\n")
    contest_md.append("\n")
    contest_md.append("| 名称 | Q1 | Q2 | Q3 | Q4 | \n")
    contest_md.append("| -- | -- | -- | -- | -- |\n")

    problems_dict = {}
    for problem in problemsets:
        problems_dict[problem["number"]] = problem

    for contest in contest_dict:
        contest_md.append(
            f"| {contest['name']} | {problems_dict[contest['origin_strs'][0]]['origin_str']} | {problems_dict[contest['origin_strs'][1]]['origin_str']} |   {problems_dict[contest['origin_strs'][2]]['origin_str']}|   {problems_dict[contest['origin_strs'][3]]['origin_str']}|\n"
        )

    for contest in contest_dict:
        contest_md.append(f"## {contest['name']}\n")
        contest_md.append("\n")

        contest_md.append("| 题目 | 难度 | 题解 | C++ | Python |\n")
        contest_md.append("| -- | -- | -- | -- | -- |\n")
        for problem in [
            problems_dict[contest["origin_strs"][0]],
            problems_dict[contest["origin_strs"][1]],
            problems_dict[contest["origin_strs"][2]],
            problems_dict[contest["origin_strs"][3]],
        ]:
            origin_str = problem["origin_str"]
            difficulty = problem["difficulty"]
            url = "https://leetcode.cn" + problem["href"]

            has_tijie = ""
            if len(list(pathlib.Path("./problemset/" + origin_str).glob("*.md"))) != 0:
                has_tijie = "\u2713"

            has_cpp_solution = ""
            if len(list(pathlib.Path("./problemset/" + origin_str).glob("*.cpp"))) != 0:
                has_cpp_solution = "\u2713"
                cpp_solution_count += 1

            has_py_solution = ""
            if len(list(pathlib.Path("./problemset/" + origin_str).glob("*.py"))) != 0:
                has_py_solution = "\u2713"
                py_solution_count += 1

            is_display = False
            if has_cpp_solution != "" or has_py_solution != "":
                is_display = True
                solution_count += 1

            question_count += 1

            if is_display:
                contest_md.append(
                    f"| [{origin_str}]({url}) | {difficulty} | {has_tijie} | {has_cpp_solution} | {has_py_solution} |\n"
                )
        contest_md.append("\n")

    with open("./docs/contests.md", "w", encoding="utf-8") as f:
        f.writelines(contest_md)


if __name__ == "__main__":
    main()
