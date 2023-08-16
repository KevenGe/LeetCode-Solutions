# 394. 字符串解码
# https://leetcode-cn.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        stacks = []
        for st in s:
            if st == "]":
                tmpStr = ""
                while True:
                    t = stacks.pop()
                    if t == "[":
                        break
                    else:
                        tmpStr = t + tmpStr

                num = 0
                i = 0
                while True:
                    if len(stacks) == 0:
                        break

                    t = stacks[-1]
                    if t.isdigit():
                        stacks.pop()
                        num += int(t) * (10 ** i)
                        i += 1
                    else:
                        break

                stacks.append(tmpStr * num)
            else:
                stacks.append(st)

        ans = "".join(stacks)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[b]"))
