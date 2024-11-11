# Problems (Order By Number)

| 序号  | 题目  | 难度  | 
| :---: | :---: | :---: |
% for x in problemset:
| ${x["ID"]} \
|  [${x["TITLE_CN"]}](./problems/${x["ID"]|u}.%20${x["TITLE_CN_NO_SPACE"]}.md) \
|  ${x["HARD_LEVEL"]} \
|
% endfor
