class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        nums_check = nums
        count_of_num = len(nums)
        for i in range(0, count_of_num):
            remainder = target - nums[i]
            if remainder in dict.keys():
                return [dict[remainder], i]
            dict[nums[i]] = i
