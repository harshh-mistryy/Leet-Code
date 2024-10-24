class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        if needle in haystack:
            findex = haystack.index(needle)
            return findex
        else: 
            return -1
        
print(Solution.strStr(haystack="sadandsad", needle="sad"))
                
