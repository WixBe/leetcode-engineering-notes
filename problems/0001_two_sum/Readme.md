# Two Sum

## Statement

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
### Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
### Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

**Constraints:**

- 2 <= nums.length <= 10<sup>4</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- -10<sup>9</sup> <= target <= 10<sup>9</sup>
Only one valid answer exists.

## 🧠 Pattern
Hash Map / Array

## 📘 Problem Link
[Leetcode - Two Sum](https://leetcode.com/problems/two-sum/)

## 🎯 Key Insight
Instead of checking every pair, store complements.

## 🚀 Versions
- v1: Brute force O(n²)
- v2: HashMap O(n)