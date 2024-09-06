class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest = [-float('inf'), -float('inf'), -float('inf')]
        smallest = [float('inf'), float('inf'), float('inf')]
        for num in nums:
            if num > largest[2]:
                largest[0] = largest[1]
                largest[1] = largest[2]
                largest[2] = num
            elif num > largest[1]:
                largest[0] = largest[1]
                largest[1] = num
            elif num > largest[0]:
                largest[0] = num

            if num < smallest[0]:
                smallest[2] = smallest[1]
                smallest[1] = smallest[0]
                smallest[0] = num
            elif num < smallest[1]:
                smallest[2] = smallest[1]
                smallest[1] = num
            elif num < smallest[2]:
                smallest[2] = num

        if smallest[1] < 0 and largest[2] >= 0:
            if smallest[0] * smallest[1] > largest[0] * largest[1]:
                return smallest[0] * smallest[1] * largest[2] 
        return largest[0] * largest[1] * largest[2]