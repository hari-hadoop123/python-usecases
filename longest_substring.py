class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
		n=len(s)
		i=0
		a=0
		d={}
		for j in range(n):
			if s[j] in d:
				i=max(d[s[j]],i)
			a=max(a,j-i+1)
			d[s[j]]=j+1
		return a
	