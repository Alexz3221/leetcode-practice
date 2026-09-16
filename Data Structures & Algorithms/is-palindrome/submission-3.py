class Solution:
    def isPalindrome(self, s: str) -> bool:

        newS = ""
        for c in s:
            if c.isalnum():
                newS = newS + c.lower()
        l = 0
        r = len(newS) - 1
        while l < r:
            #while l < r:
            #    l+= 1
            #while r > l:
            #    r -= 1
            if newS[l] != newS[r]:
                print(s[l]+ " " + s[r])
                return False
            l = l+1 
            r = r-1
        return True