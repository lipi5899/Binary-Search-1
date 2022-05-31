# Time Complexity : O(logN)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

#Your code here along with comments explaining your approach
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            #Finding a mid point
            mid = start + ((end - start)//2)
            #If mid is equal to target then return mid
            if nums[mid] == target:
                return mid
            #If left part is sorted, and also "<="" for a case where array size is 2 so mid == start is possible
            if nums[start] <= nums[mid]:
                # Now if target is equal to start and less than mid then decrementing end and incrementing start
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            #Or right part is sorted and then simply searching in right sorted part   
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
            
