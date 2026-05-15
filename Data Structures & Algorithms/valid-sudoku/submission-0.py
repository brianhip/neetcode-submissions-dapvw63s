class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_rows = True
        section = [0, 0]
        for i in range(9):
            # print("Section/Row/Col", i)
            if not self.checkRow(board[i]):
                # print("row failed")
                return False
            if not self.checkColumn(board, i):
                # print("col failed")
                return False
            # If first index is out of bounds reset to next row of section by resetting firs index to 0 and second index to the next section (add three to section[1])
            if section[0] > 6:
                section[0] = 0
                section[1] += 3
            # Call the checkbox function
            if not self.checkBox(board, section):
                # print("box failed")
                return False
            # Increase section first index
            section[0] += 3
        return True

                
    def checkRow(self, row: List[int]) -> bool:
        # check that the row contain only the necessary numbers
        unique_number = set()
        for num in row:
            if num != "." and num in unique_number:
                return False
            unique_number.add(num)
        return True

    def checkColumn(self, matrix: List[List[int]], column_index: int) -> bool:
        # Create a list with the index colum and use check row
        column_list = []
        for i in range(9):
            column_list.append(matrix[i][column_index])
        return self.checkRow(column_list)

    def checkBox(self, matrix: List[List[int]], top_left: (int, int)) -> bool:
        bottom_right = [top_left[0] + 3, top_left[1] + 3]
        # print("top_left",top_left)
        # Create a list with from i = top_left[0] -> bottom_right[0] from j = top_left[1] -> bottom_right[1]
        output = []
        for i in range(top_left[0], bottom_right[0]):
            for j in range(top_left[1], bottom_right[1]):
                output.append(matrix[i][j])
        # use check row to check if this box is good
        # print(output)
        return self.checkRow(output)

