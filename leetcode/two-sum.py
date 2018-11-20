# Two Sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

#-------------------------------------------------

# brute-force solution

class SolutionBruteForce(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return list((i, j))


# proper one-pass hash map (dictionary) solution; based on "solution" tab

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        themap = dict()
        l = len(nums)
        for i in range(l):
            complement = target - nums[i]
            if complement in themap:
                return list((i,themap[complement]))
            themap[nums[i]] = i
