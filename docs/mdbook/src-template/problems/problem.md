# ${x["ID"]}. ${x["TITLE_CN"]}

## 题目

为保证权益，题目请参考 <a href='${x["URL"]}' target="_blank">**${x["ID"]}. ${x["TITLE_CN"]}**(From LeetCode)</a>.

% for solution in x["SOLUTIONS"]:

${'##'} 解决方案${loop.index + 1}

% if solution["Readme"] != "":
${'###'} 说明
<%
with open(solution["Readme"], 'r', encoding='utf-8') as file:
    Readme_content = file.read()
%>
${Readme_content}
% endif

% if solution["C++"] != "":
${'###'} CPP
<%
with open(solution["C++"], 'r', encoding='utf-8') as file:
    cpp_content =  file.read()
%>
```C++
${cpp_content}
```
% endif

% if solution["Python"] != "":
${'###'} Python
<%
with open(solution["Python"], 'r', encoding='utf-8') as file:
    python_content =  file.read()
%>
```python
${python_content}
```
% endif
% endfor