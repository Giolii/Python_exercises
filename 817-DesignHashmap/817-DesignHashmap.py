# Last updated: 6/25/2025, 3:12:16 PM
class MyHashMap:

    def __init__(self):
        self.bucket = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        bucket = self.bucket[key % 1000]
        for b in bucket:
            if b[0] == key:
                b[1] = value
                return
        bucket.append([key,value])

    def get(self, key: int) -> int:
        bucket = self.bucket[key % 1000]
        for b in bucket:
            if b[0] == key:
                return b[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self.bucket[key % 1000]
        for b in bucket:
            if b[0] == key:
                bucket.remove(b)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)