class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for x in strs:
            for i in x:
                s+=str(ord(i))
                s+='#'
            s+=','
        return s

    def decode(self, s: str) -> List[str]:
        i,l,d,decode=0,0,'',list()
        while i < len(s):
            if s[i]=='#':
                d+=chr(int(s[l:i]))
                l=i+1
            elif s[i]==',':
                decode.append(d)
                d=''
                l=i+1
            i+=1
        return decode
