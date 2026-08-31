class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]

        diagonals = set()
        anti_diagonal = set()
        rows = [ False for i in range(n)]
        cols = [ False for i in range(n)]

        output = []
        template = [["." for j in range(n)] for i in range(n)]
    
        def alternate_state(i, j, state, perpendicular_bool, diag_callback, anti_diag_callback):
            template[i][j] = state
            rows[i] = perpendicular_bool
            cols[j] = perpendicular_bool
            diag_callback(n + (i - j))
            anti_diag_callback(i + j)

        def add_queen(i, j):
            alternate_state(i, j, "Q", True, diagonals.add, anti_diagonal.add)

        def remove_queen(i, j):
            alternate_state(i, j, ".", False, diagonals.remove, anti_diagonal.remove)
    
        def backtrack(i):
            if i == n:
                output.append([ "".join(row) for row in template])
                return

            for j in range(n):
                if (rows[i] or cols[j] or n + (i - j) in diagonals or i + j in anti_diagonal):
                    continue

                add_queen(i, j)
                backtrack(i + 1)
                remove_queen(i, j)
    
        backtrack(0)
        return output