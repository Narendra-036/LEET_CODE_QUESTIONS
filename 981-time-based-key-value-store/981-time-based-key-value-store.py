class TimeMap:

    def __init__(self):
        self.times = collections.defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        heappush(self.times[key], (timestamp*-1, value))
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        for value in self.times[key]:
            if abs(value[0]) <= timestamp:
                res = value[1]
                break
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)