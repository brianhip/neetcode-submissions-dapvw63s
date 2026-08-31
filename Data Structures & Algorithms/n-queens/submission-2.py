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
        def backtrack(i):
            if i == n:
                output.append([ "".join(row) for row in template])
                return
            for j in range(n):
                curr_diag = n + (i - j)
                anti_diag = i + j
                if (rows[i] or cols[j] or curr_diag in diagonals or anti_diag in anti_diagonal):
                    continue

                rows[i] = True
                cols[j] = True
                diagonals.add(curr_diag)
                anti_diagonal.add(anti_diag)
                template[i][j] = "Q"

                backtrack(i + 1)

                template[i][j] = "."
                rows[i] = False
                cols[j] = False
                diagonals.remove(curr_diag)
                anti_diagonal.remove(anti_diag)
    
        backtrack(0)
        return output