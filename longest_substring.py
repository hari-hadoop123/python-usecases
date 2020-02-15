class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        from itertools import combinations
        
        comb=list(set(s[x:y] for x, y in combinations((range(len(s)+1)),r=2)))
        
        comb.sort(key=len)
        
        for x in comb[::-1]:
            if len(set(x))==len(x):
                return len(x)