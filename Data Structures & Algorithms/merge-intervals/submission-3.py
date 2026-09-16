class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        result = []
        to_be_merged = intervals[0]
        for i in range(len(intervals)):
            if to_be_merged[1] < intervals[i][0]:
                result.append(to_be_merged)
                to_be_merged = intervals[i]
            # elif to_be_merged[0] > intervals[i][1 
            else:
                to_be_merged = [
                    min(to_be_merged[0], intervals[i][0]),
                    max(to_be_merged[1], intervals[i][1])
                ]
        result.append(to_be_merged)
        return result