class Solution:
    def minimumAbsDifference(self, arr): #-> List[List[int]]
        max_num = max(arr)
        min_num = min(arr)
        count_dict = [0] * (max_num - min_num + 1)
        for i in arr:
            count_dict[i-min_num] += 1

        res = []
        temp = 0
        min_diff = float('inf')
        for i in range(1,len(count_dict)):
            temp += 1
            if count_dict[i] != 0:
                if temp > min_diff:
                    temp = 0
                    continue
                elif temp == min_diff:
                    res.append([i+min_num-temp,i+min_num])
                    temp = 0
                else:
                    res = [[i+min_num-temp,i+min_num]]
                    min_diff = temp
                    temp = 0
        
        return res
                    