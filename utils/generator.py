# 2021-09-10 Qifeng
# 遍历文档，生成表格


################################################################################

# dirPath = "./《剑指offer》"
# dirPath = "./程序员面试金典（第 6 版）"
dirPath = "./Solutions for Python"


################################################################################


import os
import re


print("Generating {0}".format(dirPath))
print("| 序号 | 名称 | 链接 | 情况 |")
print("| -- | -- | -- | -- |")


for fileName in os.listdir(dirPath):
    a = re.search("(.*?)\.(.*?)\.py", fileName)
    if a :
        filePath = os.path.join(dirPath, fileName)
        with open(filePath, "r", encoding="utf8") as f:

            name = ""
            url = ""
            for i, line in enumerate(f.readlines()):
                if i == 0:
                    name = line[2:].strip()
                elif i == 1:
                    url = line[2:].strip()
                else:
                    break

            print(
                "|{0}|{1}|[click]({2})|[click]({3})|".format(
                    a.group(1), a.group(2), url, url
                )
            )

