class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # initiate the window and calculate max
        # slide window until end of window reaches the end of nums
            # update max, keep track of max frequency
            # remove the old start
                # if old start was max decrease frequency and if frequency is now 0 find a new max and frequency in window
                # if old start was not then do nothing
            # update the new end
                # if current end is greater than max update max and set frequency to 1
                # if current end is equal to max increase frequency by 1
            # store current max into output list
        start = 0
        end = 0
        curr_max = float("-inf")
        window_frequencies = defaultdict(int)
        while end < k:
            num = nums[end]
            if num > curr_max:
                curr_max = num
            window_frequencies[num] += 1
            end += 1
        start += 1
        output = []
        output.append(curr_max)
        while end < len(nums):
            if window_frequencies[nums[start - 1]] > 0:
                window_frequencies[nums[start - 1]] -= 1
            if window_frequencies[nums[start - 1]] == 0 and curr_max == nums[start - 1]:
                curr_max = max(nums[start:end+1])
            if nums[end] > curr_max:
                curr_max = nums[end]
                window_frequencies[curr_max] = 1
            elif nums[end] == curr_max:
                window_frequencies[curr_max] += 1
            output.append(curr_max)
            start += 1
            end += 1

        return output