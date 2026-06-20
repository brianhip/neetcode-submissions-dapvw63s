from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = self.createFrequencyList(nums)
        # use the index = i - min_number
        output = []
        i = len(freq_list) - 1
        while len(output) < k:
            if len(freq_list[i]) > 0:
                output.append(freq_list[i].pop())
                i += 1
            i -= 1
        return output
    def createFrequencyList(self, n: List[int]) -> List[int]:
        # counter then create a list with the frequency as index
        count_of_nums = Counter(n)
        frequency_list = [ [] for i in range(len(n) + 1)]
        for number, count in count_of_nums.items(): 
            frequency_list[count].append(number)
        return frequency_list