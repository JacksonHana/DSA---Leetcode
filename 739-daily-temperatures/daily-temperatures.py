# index          0    1    2    3    4    5    6    7
# temperature    73   74   75   71   69   72   76   73
# pointer                                  i
# stack          75   71   69
# ans            1    1



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ans = [0] * l
        stack = []

        for i,t in enumerate(temperatures):      # get index, value
            while stack and t > temperatures[stack[-1]]:     # temp in list > temp in stack
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)

        return ans
                

        