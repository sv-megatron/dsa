"""
Problem: Contains Duplicate
LeetCode #: 217
Difficulty: Easy

Primary Pattern: Arrays + Hashing
Secondary: Set

Problem Statement:
Given an integer array nums, return True if any value appears at least twice,
and return False if every element is distinct.

--------------------------------------------------

Approach 1: Brute Force

Idea:
- Compare every pair of elements
- If any nums[i] == nums[j] → duplicate found

Time Complexity Analysis:
- Two nested loops
- Outer loop runs n times
- Inner loop runs ~n times
- Total comparisons ≈ n(n-1)/2 → O(n^2)

Space Complexity Analysis:
- No extra data structures used
- Constant space → O(1)

--------------------------------------------------

Approach 2: Hash Set (Optimal)

Key Insight:
- A set stores only unique elements
- If an element already exists → duplicate found

Time Complexity Analysis:
- Single pass through array → O(n)
- Each lookup in set → O(1) average
- Total = O(n)

Space Complexity Analysis:
- In worst case, all elements are unique
- Set stores n elements → O(n)

--------------------------------------------------
"""


# -------------------------------
# Approach 1: Brute Force
# -------------------------------
def contains_duplicate_bruteforce(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# -------------------------------
# Approach 2: Optimal (Set)
# -------------------------------
def contains_duplicate(nums):
    seen = set()

    for num in nums:   # runs n times
        if num in seen:   # O(1) lookup
            return True
        seen.add(num)     # O(1) insert

    return False


# -------------------------------
# Example Run
# -------------------------------
if __name__ == "__main__":
    nums = [1, 2, 3, 1]

    print("Brute Force:", contains_duplicate_bruteforce(nums))
    print("Optimal:", contains_duplicate(nums))


# -------------------------------
# Key Learning
# -------------------------------
# Sets help detect duplicates efficiently by providing
# constant-time membership checks.

