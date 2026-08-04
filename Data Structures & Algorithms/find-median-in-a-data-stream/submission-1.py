import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = [] # When adding or removing a number, convert the number to negative value 
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        

    def addNum(self, num: int) -> None:

        # min_heap should contain only numbers larger than the max_heap
        # Example [3, 2, 1, 5, 6] -> 
        # min_heap = [3, 5, 6] 
        # max_heap = [-2, -1]
        # At any point the min_heap can only be one number greater than max_heap
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        # reorder
        if self.max_heap:
            top_max = self.max_heap[0] * -1
            top_min = self.min_heap[0]
            if top_max > top_min:
                num1 = heapq.heappop(self.min_heap)
                num2 = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -num2)
                heapq.heappush(self.max_heap, -num1)
    def findMedian(self) -> float:
        # find median should if the list are of equal length return the average of (min_heap[0] and (max_heap[0] * -1)) else return min_heap[0]
        if not len(self.min_heap):
            return 0.0
        if len(self.min_heap) == len(self.max_heap):
            top_max = self.max_heap[0] * -1
            top_min = self.min_heap[0]
            return (top_max + top_min) /2
        else:
            return self.min_heap[0]
        
        