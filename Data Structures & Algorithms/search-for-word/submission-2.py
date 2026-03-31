class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width  = len(board[0])
        def explore(x, y, index):
            if index == len(word):
                return True
            out_of_bounds = (x < 0 or height <= x or y < 0 or width <= y)
            if out_of_bounds or word[index] != board[x][y] or board[x][y] == "#":
                return False
            index += 1
            board[x][y] = "#"
            is_found = (
                explore(x - 1, y, index) or
                explore(x + 1, y, index) or  
                explore(x, y - 1, index) or 
                explore(x, y + 1, index)
                )
            board[x][y] = word[index - 1]
            return is_found
        for x, row in enumerate(board):
            for y, char in enumerate(row):
                if char == word[0]:
                    is_found = explore(x, y, 0)
                    if is_found:
                        return True
        return False