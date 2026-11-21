class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a,b={},{}
        for x in s:
            a[x]=a.get(x,0)+1
        for x in t:
            b[x]=b.get(x,0)+1
        
        if a==b:
            return True
        else:
            return False

