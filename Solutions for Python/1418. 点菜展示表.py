from typing import List
import functools


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foodNames = set()
        tableNumbers = set()
        data = dict()
        for customerName, tableNumber, foodName in orders:
            foodNames.add(foodName)
            tableNumbers.add(tableNumber)
            if tableNumber in data:
                if foodName in data[tableNumber]:
                    data[tableNumber][foodName] += 1
                else:
                    data[tableNumber][foodName] = 1
            else:
                data[tableNumber] = {foodName: 1}

        # sort
        foodNames = sorted(list(foodNames))
        tableNumbers = sorted(
            list(tableNumbers), key=functools.cmp_to_key(lambda x, y: int(x) - int(y))
        )

        ans = []
        ans.append(["Table", *foodNames])

        for tableNumber in tableNumbers:

            foodNumbers = []
            for foodName in foodNames:
                if foodName in data[tableNumber]:
                    foodNumbers.append(str(data[tableNumber][foodName]))
                else:
                    foodNumbers.append("0")

            ans.append([tableNumber, *foodNumbers])
        return ans


if __name__ == "__main__":
    so = Solution()
