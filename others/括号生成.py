class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # lastRight = 0
        # lastLeft = n
        res = []

        def helper(ans, lastLeft, lastRight):
            if lastLeft == 0 and lastRight == 0:
                res.append(ans)
            else:
                if lastLeft > 0:
                    helper(ans + "(", lastLeft - 1, lastRight + 1)
                if lastRight > 0:
                    helper(ans + ")", lastLeft, lastRight - 1)

        helper("", n, 0)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
