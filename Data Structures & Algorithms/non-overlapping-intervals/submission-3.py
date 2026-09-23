class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Create dp to track the number of overlapping
        # sort
        # Always delete the one that has the largest 
        
        """
        If we sort the intervals from endinv time we can count the number of non overlapping intervals using a greedy approach to make sure we always get the least amount of remove intervals
        """
        intervals.sort(key = lambda x: x[1])
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                count += 1
            else:
                end = intervals[i][1]
        return count
        
            