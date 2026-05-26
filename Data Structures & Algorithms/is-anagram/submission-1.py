class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = dict()
        seen2 = dict()

        for c in s:
            if c in seen1.keys():
                seen1[c] +=1 
            else:
                seen1[c] = 1
        
        for c in t:
            if c in seen2.keys():
                seen2[c] +=1 
            else:
                seen2[c] = 1
        
        return seen1 == seen2