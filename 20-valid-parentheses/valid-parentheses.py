# list      ( [ ) ] 
# pointer     i
# stack     ( [

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapBracket = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            if char in mapBracket: 
                if stack and stack[-1] == mapBracket[char]:         #check empty and in map
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)      #append open
        
        return True if not stack else False
