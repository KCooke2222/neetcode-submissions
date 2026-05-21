class MedianFinder:
    # maxheap for left, minheap right
        # insert num into side it fits on
    # ensure size diff <= 1 (delmin) O(logn)
    # find median uses heap[0] O(1)

    def __init__(self):
        self.leftheap = []
        self.rightheap = []

    def addNum(self, num: int) -> None:
        if self.leftheap and num <= -self.leftheap[0]:
            heapq.heappush(self.leftheap, -num)
        else:
            heapq.heappush(self.rightheap, num)

        # balance l/r
        diff = len(self.leftheap) - len(self.rightheap)
        if diff > 1:
            popNum = -heapq.heappop(self.leftheap)
            heapq.heappush(self.rightheap, popNum)
        elif diff < -1:
            popNum = heapq.heappop(self.rightheap)
            heapq.heappush(self.leftheap, -popNum)

    def findMedian(self) -> float:
        diff = len(self.leftheap) - len(self.rightheap)
        if diff == 1:
            return -self.leftheap[0]
        elif diff == -1:
            return self.rightheap[0]
        else:
            return (-self.leftheap[0] + self.rightheap[0]) / 2