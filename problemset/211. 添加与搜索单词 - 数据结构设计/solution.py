# 211. 添加与搜索单词 - 数据结构设计
# https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/


################################################################################


class WordTreeNode:
    def __init__(self, letter: str) -> None:
        self.letter = letter
        self.isEnd = False
        self.children = {}

    def setIsEnd(self, isEnd: bool) -> None:
        self.isEnd = isEnd

    def addChild(self, child: str) -> None:
        if child not in self.children:
            self.children[child] = WordTreeNode(child)

    def getChild(self, child: str):
        if child in self.children:
            return self.children[child]
        return None

    def getChildren(self):
        return self.children.values()


class WordDictionary:
    def __init__(self):
        self.root = WordTreeNode("#")

    def addWord(self, word: str) -> None:
        t = self.root
        for letter in word:
            t.addChild(letter)
            t = t.getChild(letter)
        t.setIsEnd(True)

    def search(self, word: str) -> bool:
        def dfs(tNode: WordTreeNode, word: str, index: int):
            if index == len(word):
                return tNode.isEnd

            tmp = word[index]
            if tmp == ".":
                for t in tNode.getChildren():
                    if dfs(t, word, index + 1):
                        return True
                return False
            else:
                t = tNode.getChild(tmp)
                if t is not None:
                    return dfs(t, word, index + 1)
                else:
                    return False

        t = self.root
        return dfs(t, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


################################################################################

if __name__ == "__main__":
    pass
