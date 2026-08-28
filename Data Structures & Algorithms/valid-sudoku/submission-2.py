class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # build list of cols and sections top left to bottom right
        ROWS = [["." for j in range(9)] for i in range(9)]
        COLS = [["." for j in range(9)] for i in range(9)]
        BOXS = [["." for j in range(9)] for i in range(9)] 

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                ROWS[i][j] = val
                COLS[j][i] = val
                BOXS[(i // 3 * 3) + j // 3][(i % 3 * 3)+ j % 3] = val 
        # print("ROWS", ROWS)
        # print("COLS", COLS)
        # print("BOXS", BOXS)
        for i in range(1, 10):
            number = str(i)
            for j in range(9):
                r_occurrences = ROWS[j].count(number)
                c_occurrences = COLS[j].count(number)
                b_occurrences = BOXS[j].count(number)
                if r_occurrences > 1 or c_occurrences > 1 or b_occurrences > 1:
                    return False
        return True
