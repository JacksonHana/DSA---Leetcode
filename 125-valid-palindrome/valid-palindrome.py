class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # print(s.lower())
        # s.lower()
        # filtered_s = "".join(char.lower() for char in s if char.isalnum())
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i+=1
                continue
            elif not s[j].isalnum():
                j-=1
                continue
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
        