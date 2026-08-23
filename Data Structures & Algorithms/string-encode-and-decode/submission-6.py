class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return '中é'
    
        sign = 'é'.encode('utf-8')
        res = b''
        for i in range(len(strs) - 1):
            s = strs[i]
            res += s.encode('utf-8')
            res += sign
        
        s = strs[-1].encode('utf-8')
        res += s
        return res.decode('utf8')


    def decode(self, s: str) -> List[str]:
        if s == '中é':
            return []
        return s.split('é')
