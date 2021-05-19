class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0
        for x in typed:
            if l < (n := len(name)):
                if x == name[l]:
                    l += 1
                elif l - 1 >= 0 and x == name[l - 1]:
                    pass
                else:
                    return False
            else:
                if x != name[l - 1]:
                    return False
        return l == len(name)

