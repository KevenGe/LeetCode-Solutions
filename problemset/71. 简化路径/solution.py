# 71. 简化路径
# https://leetcode-cn.com/problems/simplify-path/

################################################################################

class Solution:
    def simplifyPath(self, path: str) -> str:
        dp = []
        for t in path.split("/"):
            if t == "":
                continue
            elif t == ".":
                continue
            elif t == "..":
                if len(dp) == 0:
                    continue
                else:
                    dp.pop()
            else:
                dp.append(t)
        return "/" + "/".join(dp)


################################################################################

if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath("/a/./b/../../c/"))
