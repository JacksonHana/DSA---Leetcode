class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row = len(boxGrid)
        col = len(boxGrid[0])

        # move ston # to right
        for r in range(row):
            empty = col - 1 
            for c in range(col - 1, -1, -1):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c], boxGrid[r][empty] = boxGrid[r][empty], boxGrid[r][c]     # Swap stone to 'empty' 
                    empty -= 1
                elif boxGrid[r][c] == '*':
                    empty = c - 1               # obstacle

        box = [[None] * row for _ in range(col)]
        for r in range(row):
            for c in range(col):
                box[c][row - 1 - r] = boxGrid[r][c]          # rotation formula: (r, c) -> (c, row - 1 - r)
                
        return box
        