# Readme of Problemset


Problem Number = ${problem_num}

| 序号  | 题目  | 难度  | Readme |  C++  |  Py   |
| :---: | :---: | :---: | :----: | :---: | :---: |
% for x in problemset:
% for solution in x["SOLUTIONS"]:
| ${x["ID"]} \
|  [${x["TITLE_CN"]}](${x["URL"]}) \
|  ${x["HARD_LEVEL"]} \
|\
% if solution["Readme"] != "":
[✔️(Click)](${solution["Readme"]}) \
% endif
|\
% if solution["C++"] != "":
[✔️(Click)](${solution["C++"]}) \
% endif
|\
% if solution["Python"] != "":
[✔️(Click)](${solution["Python"]}) \
% endif
|
% endfor
% endfor
