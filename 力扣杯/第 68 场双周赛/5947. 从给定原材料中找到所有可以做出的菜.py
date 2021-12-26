# 5947. 从给定原材料中找到所有可以做出的菜
# https://leetcode-cn.com/problems/find-all-possible-recipes-from-given-supplies/

from typing import List, Dict
import sys

sys.setrecursionlimit(1000000)


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        supplies_dict = set()
        for supply in supplies:
            supplies_dict.add(supply)

        recipes_could = {}
        for i, recipe in enumerate(recipes):
            isOK = True
            for ingredient in ingredients[i]:
                if ingredient not in supplies_dict:
                    isOK = False
                    break
            recipes_could[recipe] = isOK

        while True:
            hasUpdate = False
            for i, recipe in enumerate(recipes):
                if not recipes_could[recipe]:
                    isOK = True
                    for ingredient in ingredients[i]:
                        if ingredient not in supplies_dict and (ingredient not in recipes_could or (
                                ingredient in recipes_could and recipes_could[ingredient] == False)):
                            isOK = False
                            break
                    if isOK:
                        hasUpdate = True
                        recipes_could[recipe] = True
            if not hasUpdate:
                break

        ans = []
        for k,v in recipes_could.items():
            if v:
                ans.append(k)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.findAllRecipes(["rea", "reb"],
                                  [["sua", "sub", "reb"],
                                   ["rea", "sua"]],
                                  ["sua", "sub"]))
    print(solution.findAllRecipes(["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"],
                                  [["d"],
                                   ["hveml", "f", "cpivl"],
                                   ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
                                   ["cpivl", "hveml", "zpmcz", "ju", "h"],
                                   ["h", "fzjnm", "e", "q", "x"],
                                   ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"], ["f", "hveml", "cpivl"]],
                                  ["f", "hveml", "cpivl", "d"]))
