class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = [set() for i in range(9)]
        COLS = [set()for i in range(9)]
        BOXS = [set() for i in range(9)] 

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in ROWS[i] or val in COLS[j] or val in BOXS[(i // 3 * 3) + j // 3]:
                    return False
                ROWS[i].add(val)
                COLS[j].add(val)
                BOXS[(i // 3 * 3) + j // 3].add(val)
        return True
    