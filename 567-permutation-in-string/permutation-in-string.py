class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # map for s1
        target_map = {}
        for char in s1:
            target_map[char] = target_map.get(char, 0) + 1
        
        # window_map stores characters in the current s2 segment
        window_map = {}
        
        # compare two dictionaries manually
        def is_match(map1, map2):
            if len(map1) != len(map2):
                return False
            for key in map1:
                if map1[key] != map2.get(key, 0):
                    return False
            return True

        # Initialize the first window
        for i in range(n1):
            char = s2[i]
            window_map[char] = window_map.get(char, 0) + 1
        
        if is_match(target_map, window_map):
            return True

        # Slide the window
        for i in range(n1, n2):
            new_char = s2[i]
            old_char = s2[i - n1]
            
            # Add new character
            window_map[new_char] = window_map.get(new_char, 0) + 1
            
            # Remove old character
            window_map[old_char] -= 1
            if window_map[old_char] == 0:
                del window_map[old_char]
            
            # Check for match
            if is_match(target_map, window_map):
                return True
                
        return False