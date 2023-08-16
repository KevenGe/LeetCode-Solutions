# 859. 亲密字符串
# https://leetcode-cn.com/problems/buddy-strings/

################################################################################


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s != goal:
            unequal_num = 0
            unequal_indexs = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    unequal_num += 1
                    unequal_indexs.append(i)

            if unequal_num == 2 and (
                s[unequal_indexs[0]] == goal[unequal_indexs[1]]
                and s[unequal_indexs[1]] == goal[unequal_indexs[0]]
            ):
                return True
            return False
        else:
            char_dict = dict()
            for i in range(len(s)):
                if s[i] in char_dict:
                    return True
                else:
                    char_dict[s[i]] = 1
            return False


################################################################################

if __name__ == "__main__":
    solution = Solution()
    print(solution.buddyStrings("aaaaaaabc", "aaaaaaacb"))
