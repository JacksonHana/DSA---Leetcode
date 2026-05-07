import numpy as np

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = np.transpose(matrix)
        transpose = transpose.tolist()
        return transpose