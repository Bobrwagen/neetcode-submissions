class Pair:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.data = []
        

    def put(self, key: int, value: int) -> None:
        for p in self.data:
            if p.key == key:
                p.value = value
                return
        self.data.append(Pair(key,value))

    def get(self, key: int) -> int:
        for p in self.data:
            if p.key == key:
                return p.value
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.data)):
            p = self.data[i]
            if p.key == key:
                self.data.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)