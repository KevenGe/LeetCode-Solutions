import functools


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        di = self.countOfAtoms2(formula)
        keys = di.keys()
        keys = sorted(keys)

        ans = []
        for key in keys:
            ans.append(key)
            if di[key] > 1:
                ans.append(str(di[key]))
        ans = "".join(ans)
        return ans

    def countOfAtoms2(self, formula: str) -> dict:
        di = {}
        i = 0
        while i < len(formula):
            if formula[i].isupper():
                st = ""
                end = i + 1
                for j in range(i + 1, len(formula)):
                    if formula[j].islower():
                        end += 1
                    else:
                        break
                st = formula[i:end]

                count = 1
                countEnd = end
                for j in range(end, len(formula)):
                    if formula[j].isdigit():
                        countEnd = j + 1
                    else:
                        break

                t = formula[end:countEnd]
                if t != "":
                    count = int(formula[end:countEnd], 10)

                if st in di:
                    di[st] += count
                else:
                    di[st] = count
                i = countEnd
            elif formula[i] == "(":

                diTmp = {}
                end = i + 1
                bracktLevel = 1
                for j in range(i + 1, len(formula)):
                    if formula[j] == "(":
                        bracktLevel += 1
                    if formula[j] == ")":
                        if bracktLevel == 1:
                            diTmp = self.countOfAtoms2(formula[i + 1 : j])
                            end = j + 1
                            break
                        else:
                            bracktLevel -= 1

                count = 1
                countEnd = end
                for j in range(end, len(formula)):
                    if formula[j].isdigit():
                        countEnd = j + 1
                    else:
                        break

                t = formula[end:countEnd]
                if t != "":
                    count = int(formula[end:countEnd], 10)

                for k, v in diTmp.items():
                    if k in di:
                        di[k] += v * count
                    else:
                        di[k] = v * count

                i = countEnd
        return di


if __name__ == "__main__":
    so = Solution()
    print(so.countOfAtoms("NON3"))
