class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
            1 2 3        7 4 1
            4 5 6   ==>  8 5 2
            7 8 9        9 6 3

             1  2  3  4  5
             6  7  8  9 10
            11 12 13 14 15
            16 17 18 19 20
            21 22 23 24 25

            have a searching window of start and ending rotate every number from start to end with the 90 degree position
                0,0 => 0,5 => 5,5 => 5,0
                0,+1 =>+1,5=>5,-1=>-1,0
        '''
        n = len(matrix)
        start = 0
        end = n - 1
        while start < end:
            for i in range(start, end):
                offset = i - start
                temp = matrix[start][i]
                matrix[start][i] = matrix[end-offset][start]
                matrix[end-offset][start] = matrix[end][end - offset]
                matrix[end][end - offset] = matrix[start + offset][end]
                matrix[start + offset][end] = temp
            start += 1
            end -= 1


        # while start < end:
        #     for i in range(start, end):
        #         offset = i - start
        #         temp = matrix[start][i]
        #         matrix[start][i] = matrix[end - offset][start]
        #         matrix[end - offset][start] = matrix[end][end - offset]
        #         matrix[end][end - offset] = matrix[start + offset][end]
        #         matrix[start + offset][end] = temp
        #     start += 1
        #     end -= 1