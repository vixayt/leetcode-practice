class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers)-1

        while first != last:
            sum = numbers[first] + numbers[last]
            if sum > target:
                last -= 1
            elif sum < target:
                first += 1
            else:
                return [first+1, last+1]
            
        
