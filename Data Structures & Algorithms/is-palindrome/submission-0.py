class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        cleaned = "".join(filter(str.isalnum, s))
        length = len(cleaned)-1
        while i<length:
            if cleaned[i].lower() != cleaned[length].lower():

                return False
            i+=1
            length-=1
        return True