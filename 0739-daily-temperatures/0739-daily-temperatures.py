class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Okay I am going to solve this.
        if not temperatures:
            return []
        
        # I think this approach 
        ans : list = [0]*len(temperatures)
        stack : list = []
        for idx in range(len(temperatures) - 1,-1,-1):
            temperature = 1
            if idx == len(temperatures) - 1:
                ans[idx] = 0
                stack.append((temperatures[idx],1))
            else:
                while stack and temperatures[idx] >= stack[-1][0]:
                    temp = stack.pop()
                    temperature += temp[1]
                if stack == []:
                    ans[idx] = 0
                else:
                    ans[idx] = temperature
                stack.append((temperatures[idx],temperature))
        return ans
            
            
                    