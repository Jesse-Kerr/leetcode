from typing import List

#Two_sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for this_ind in range(0, len(nums) - 1):
            this_val = nums[this_ind]

            for other_ind in range(this_ind +1, len(nums)):
                other_val = nums[other_ind]
                sum_vals = this_val + other_val
                if sum_vals == target:
                    return [this_ind, other_ind]


solution = Solution()
yo = solution.twoSum(nums=[3, 2, 4], target= 6)
print(yo)

# Other solutions
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h_table = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in h_table and h_table[diff] != i:
                return [h_table[diff], i]
            else:
                h_table[nums[i]] = i

solution = Solution()
yo = solution.twoSum(nums=[3, 2, 4], target= 6)
print(yo)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        

node1 = ListNode(x = 10)
node2 = ListNode(x = 20)

node1.next =
list.next