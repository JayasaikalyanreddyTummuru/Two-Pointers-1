#Time Complexity: O(n)
#Space Complexity: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        
        Do not return anything, modify nums in-place instead.
        """
        
        low = 0
        high = len(nums)-1
        mid = 0
        
        while mid<= high:
            if nums[mid] == 2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1
                
            elif nums[mid] == 0:
                nums[mid],nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
                
            else:
                if nums[mid] == 1:
                    mid += 1
                    
        