# Last updated: 7/21/2025, 3:20:24 PM
class MedianFinder:

    def __init__(self):
        self.max= []
        self.min= []
        

    def addNum(self, num: int) -> None:
        heappush(self.max,-num)
        heappush(self.min,-heappop(self.max))
        if len(self.min) > len(self.max):
            heappush(self.max,-heappop(self.min))
        

    def findMedian(self) -> float:
        if len(self.min) == len(self.max):
            return (-self.max[0] + self.min[0]) / 2
        else:
            return -self.max[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()