"""
Problem: Two Sum
LeetCode #: 1
Difficulty: Easy

Primary Pattern: Arrays + Hashing
Secondary: Hash Map

Problem Statement:
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume exactly one solution exists, and you may not use the same element twice.

--------------------------------------------------

Approach 1: Brute Force

Idea:
- Check every pair (i, j)
- If nums[i] + nums[j] == target → return indices

Time Complexity: O(n^2)
Space Complexity: O(1)

Time Complexity Analysis:
- Outer loop runs n times
- Inner loop runs (n-1), (n-2), ..., 1 times
- Total comparisons ≈ n(n-1)/2 → O(n^2)

Space Complexity Analysis:
- No extra data structures used
- Only a few variables → constant space → O(1)

--------------------------------------------------

Approach 2: Hash Map (Optimal)

Key Insight:
- Instead of checking all pairs, store numbers as you go
- For each number, check if (target - num) already exists

Why it works:
- We trade space for time
- Lookup becomes O(1)

Time Complexity: O(n)
Space Complexity: O(n)

Time Complexity Analysis:
- Single loop through array → O(n)
- Each lookup in hashmap → O(1)
- Total = O(n) * O(1) = O(n)

Space Complexity Analysis:
- In worst case, we store all n elements in hashmap
- So space grows linearly with input size → O(n)

--------------------------------------------------
"""

# -------------------------------
# Approach 1: Brute Force
# -------------------------------


def two_sum_bruteforce(nums, target):
    for i in range(len(nums)):          # runs n times
        for j in range(i + 1, len(nums)):  # runs ~n times
            if nums[i] + nums[j] == target:
                return [i, j]


# -------------------------------
# Approach 2: Optimal (Hash Map)
# -------------------------------


def two_sum_optimal(nums, target):
    hashmap = {}  # value -> index

    for i, num in enumerate(nums):   # single pass → n iterations
        complement = target - num

        # O(1) average lookup
        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[num] = i  # O(1) insert


# -------------------------------
# Edge Cases
# -------------------------------
# - Negative numbers
# - Duplicate values
# - Exactly one solution guaranteed


# -------------------------------
# Example Run
# -------------------------------
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print("Brute Force:", two_sum_bruteforce(nums, target))
    print("Optimal:", two_sum_optimal(nums, target))


# -------------------------------
# Key Learning
# -------------------------------
# Brute force checks all pairs → quadratic time.
# Hashmap reduces repeated work by storing seen values,
# turning it into a linear-time solution.
