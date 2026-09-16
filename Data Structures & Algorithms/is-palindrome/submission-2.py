class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for i in s:
            if i.isalnum():
                newS += i.lower()
        print(newS)
        length = 0
        if len(newS) % 2 == 0:
            length = len(newS) / 2
        else:
            length = (len(newS) - 1)/2
        print (length)
        for i in range(int(length)):
            if newS[i] == newS[len(newS) - i - 1]:
                continue
            else:
                return False
        return True