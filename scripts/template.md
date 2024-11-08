# Readme of Problemset

|        |          全部数量           |      有记录数量       | 未记录数量 |
| :----: | :-------------------------: | :-------------------: | :--------: |
|  ALL   |    ${problem_num + 547}     |    ${problem_num}     |    547     |
|  EASY  |  ${problem_easy_num + 207}  |  ${problem_easy_num}  |    207     |
| MEDIUM | ${problem_medium_num + 267} | ${problem_medium_num} |    267     |
|  HARD  |  ${problem_hard_num + 73 }  |  ${problem_hard_num}  |     73     |

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
