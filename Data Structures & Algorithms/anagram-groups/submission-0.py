class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary={}
        for x in strs:
            key=''.join(sorted(x))
            if key not in dictionary:
                dictionary[key]=[]
            dictionary[key].append(x)
        final=list(dictionary.values())
        return final
