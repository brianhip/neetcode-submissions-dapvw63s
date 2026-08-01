class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.iteration_solution(matrix)

    def iteration_solution(self, matrix: List[List[int]]) -> List[int]:
        nums_in_spiral = []
        # WALLS
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        left = 0

        # SPIRAL (4 loops)
        while top < bottom and left < right:
            # ADD TOP ROW from left -> right 
            for i in range(left, right):
                nums_in_spiral.append(matrix[top][i])
            top += 1
            # ADD RIGHT COL from top -> bottom 
            for i in range(top, bottom):
                nums_in_spiral.append(matrix[i][right - 1])
            right -= 1
            # Since we shrink in both directions now we check again
            if not (left < right and top < bottom):
                break
            # ADD BOTTOM ROW from left -> right 
            for i in range(right - 1, left - 1, -1):
                nums_in_spiral.append(matrix[bottom - 1][i])
            bottom -= 1
            # ADD LEFT COL from bottom -> right 
            for i in range(bottom - 1, top - 1, -1):
                nums_in_spiral.append(matrix[i][left])
            left += 1
        return nums_in_spiral

            