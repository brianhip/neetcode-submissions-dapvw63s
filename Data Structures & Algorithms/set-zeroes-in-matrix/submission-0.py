class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Iterate over matrix store the rows and columns with zeroes
        NUM_ROWS = len(matrix)
        NUM_COLS = len(matrix[0])

        rows_with_zero = [ False for i in range(NUM_ROWS)]
        columns_with_zero = [ False for i in range(NUM_COLS)]
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if matrix[row][col] == 0:
                    rows_with_zero[row] = True
                    columns_with_zero[col] = True
        
        # Iterate again but now mutate the items that either are in a column or row with 0
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if rows_with_zero[row] == True or columns_with_zero[col] == True:
                    matrix[row][col] = 0
        return