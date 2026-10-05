class TreeNode:
    def __init__(self):
        self.letters = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.start = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.start
        for char in word:
            if char not in curr.letters:
                curr.letters[char] = TreeNode()
            curr = curr.letters[char]
        curr.is_end = True           

    def search(self, word: str) -> bool:
        curr = self.start
        for char in word:
            if char not in curr.letters:
                return False
            curr = curr.letters[char]
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.start
        for char in prefix:
            if char not in curr.letters:
                return False
            curr = curr.letters[char]
        return True
        
        