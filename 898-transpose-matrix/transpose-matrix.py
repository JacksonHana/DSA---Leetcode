#i 0    1   2
#  2    4  -1
# -10   5   11
#  18  -7   6

import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = np.transpose(matrix)
        transpose = transpose.tolist()
        return transpose

        