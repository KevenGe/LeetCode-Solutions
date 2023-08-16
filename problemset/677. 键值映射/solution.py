# 677. 键值映射
# https://leetcode-cn.com/problems/map-sum-pairs/

################################################################################


class TreeNode:
    def __init__(self, val: str) -> None:
        self.val = val
        self.children = dict()


class MapSum:
    def __init__(self):
        self.root = TreeNode(0)

    def insert(self, key: str, val: int) -> None:
        t = self.root
        for k in key:
            if k not in t.children:
                t.children[k] = TreeNode(0)
            t = t.children[k]

        t.val = val
        t.children["#"] = None

    def sum(self, prefix: str) -> int:
        t = self.root
        for k in prefix:
            if k not in t.children:
                return 0
            t = t.children[k]

        def dfs(t: TreeNode) -> int:
            ans = 0

            if "#" in t.children:
                ans += t.val

            for chi in t.children.values():
                if chi is not None:
                    ans += dfs(chi)
            return ans

        ans = dfs(t)
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


################################################################################

if __name__ == "__main__":
    # solution = Solution()
    pass
