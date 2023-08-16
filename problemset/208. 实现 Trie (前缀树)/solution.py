# 208. 实现 Trie (前缀树)
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/

################################################################################

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordTree = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        t = self.wordTree
        for s in word:
            if s not in t:
                t[s] = {}
            t = t[s]
        t["end"] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.wordTree
        for s in word:
            if s not in t:
                return False
            else:
                t = t[s]

        return "end" in t

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.wordTree
        for s in prefix:
            if s not in t:
                return False
            else:
                t = t[s]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



################################################################################


if __name__ == "__main__":
    pass
