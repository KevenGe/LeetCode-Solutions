# 475. 供暖器
# https://leetcode-cn.com/problems/heaters/

from typing import List


class Solution:

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()

        distance_min = 0
        heater_index = 0
        for house_index in range(len(houses)):
            while heater_index + 1 < len(heaters) and abs(heaters[heater_index] - houses[house_index]) >= abs(heaters[heater_index+1] - houses[house_index]):
                heater_index += 1
            distance_min = max(distance_min, abs(heaters[heater_index] - houses[house_index]))

        return distance_min