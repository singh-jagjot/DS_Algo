class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, x in enumerate(nums):
            if x not in d:
                d[x] = [[i], 1]
            else:
                d[x][0].append(i)
                d[x][1] += 1

        for i, x in enumerate(nums):
            k = target - x
            temp = d[x]
            if d[x][1] == 1:
                d.pop(x)
            else:
                d[x][0].remove(i)
                d[x][1] -= 1
            
            if k in d:
                return [i, d[k][0][0]]
