import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (using negative values)
        self.large = []  # Min heap

    def addNum(self, num):

        heapq.heappush(self.small, -num)

        # Keep smaller values in small heap
        if self.small and self.large:
            if -self.small[0] > self.large[0]:
                val = -heapq.heappop(self.small)
                heapq.heappush(self.large, val)

        # Balance heap sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):

        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2.0
