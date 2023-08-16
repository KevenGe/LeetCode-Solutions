# 468. 验证IP地址
# https://leetcode.cn/problems/validate-ip-address/


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            # ipv4
            if len(set(queryIP).difference(set("01234567890."))) != 0:
                return "Neither"

            datas = queryIP.split(".")
            if len(datas) != 4:
                return "Neither"

            for i in range(4):
                if not (1 <= len(datas[i]) <= 3):
                    return "Neither"
                if len(datas[i]) != 1 and datas[i].startswith("0"):
                    return "Neither"
                if not (0 <= int(datas[i]) <= 255):
                    return "Neither"

            return "IPv4"
        else:
            # ipv6
            if len(set(queryIP).difference(set("01234567890abcdefABCDEF:"))) != 0:
                return "Neither"

            datas = queryIP.split(":")
            if len(datas) != 8:
                return "Neither"

            for i in range(8):
                if not (1 <= len(datas[i]) <= 4):
                    return "Neither"
                if not (0 <= int(datas[i], 16) <= int("ffff", 16)):
                    return "Neither"

            return "IPv6"