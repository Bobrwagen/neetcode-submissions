class LinkedList:
    def __init__(self,key, val):
        self.next, self.prev = None, None
        self.val = val
        self.key = key

class LFUCache:

    def __init__(self, capacity: int):
        self.frequencies = defaultdict(int)
        self.lfu = {}
        self.cache = {}
        self.cap = capacity
    
    def insert(self, node, freq):
        if freq not in self.lfu:
            left, right = LinkedList(0,0), LinkedList(0,0)
            left.next = right
            right.prev = left
            self.lfu[freq] = (left,right)
        _ , r = self.lfu[freq]
        prev,nxt = r.prev, r
        prev.next, nxt.prev = node, node
        node.next = nxt
        node.prev = prev
    
    def remove(self, node):    
        prev,nxt = node.prev, node.next
        nxt.prev, prev.next = prev, nxt



    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        freq = self.frequencies[key]
        self.frequencies[key] += 1
        self.remove(node)
        self.insert(node, freq+1)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.cap:
                minFreq = min(self.frequencies.values())
                l,_ = self.lfu[minFreq]
                minKey = l.next.key
                r = l.next.next
                l.next = r
                r.prev = l
                del self.frequencies[minKey]
                del self.cache[minKey]
            node = LinkedList(key, value)
            self.frequencies[key] = 1
            self.cache[key] = node
            self.insert(node, 1)
        else:
            node = self.cache[key]
            freq = self.frequencies[key]
            self.frequencies[key] += 1
            self.remove(node)
            node.val = value
            self.insert(node, freq+1)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)