class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            Understand:
                Input: List with nums
                Output: The top k most frequent numbers
                Observations:
                    We need to calculate the frequency of numbers
                        (later) Can I calculate the frequency and dynamically update the order of most frequent?
                    Return the top k most frequent numbers
            Match: Recommended is       run: O(n)       space: O(n)
                Use counter and sort    run: O(n log n) space: O(n)
                collections.Counter(nums) to get the frequency count of all numbers
                convert into a list with (frequency, number)
                sort list based on frequency 
                return k largest number

                Use bucket sort from 1 - n frequency the largest frequency you can have is n an that is when the entire list has same value

            Plan:
                Create a counter of numbers O(n)
                Iterate the counter and add to the bucket index that corresponds to the frequency O(n)
                Iterate the bucket until you find k numbers greater that 0 and build an output list O(n)
                Return output list O(1)
            Implement:
            Review:
            Evaluate:
        '''
        count_of_number = collections.Counter(nums)

        bucket = [[] for i in range(len(nums))]

        for number, frequency in count_of_number.items():
            bucket[frequency - 1].append(number)
        # print(bucket)
        output = []
        for i in range(len(bucket) - 1, -1, -1):
            if len(output) < k and bucket[i]:
                for number in bucket[i]:
                    if len(output) == k:
                        return output
                    else:
                        output.append(number)
        return output