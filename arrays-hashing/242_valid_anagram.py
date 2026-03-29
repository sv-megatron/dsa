"""
Problem: Valid Anagram
LeetCode #: 242
Difficulty: Easy

Primary Pattern: Arrays + Hashing
Secondary: Frequency Count

--------------------------------------------------

Approach 1: Sorting

Idea:
- Sort both strings and compare

Time Complexity:
- Sorting takes O(n log n)
- Two sorts → O(n log n)
- Comparison → O(n)
- Final: O(n log n)

Space Complexity:
- Sorting creates new arrays → O(n)

--------------------------------------------------

Approach 2: Hashmap

Idea:
- Count frequency of characters using dictionary

Time Complexity:
- Two passes → O(n)
- Each operation → O(1)
- Final: O(n)

Space Complexity:
- Store up to n characters → O(n)

--------------------------------------------------

Approach 3: Frequency Array (Optimal)

Key Insight:
- Only lowercase letters → fixed size array (26)

Time Complexity:
- Single loop → O(n)
- Final check → O(1) (array size is constant)
- Final: O(n)

Space Complexity:
- Array size 26 → constant → O(1)

--------------------------------------------------
"""


# -------------------------------
# Approach 1: Sorting
# -------------------------------
def is_anagram_sort(s, t):
    return sorted(s) == sorted(t)


# -------------------------------
# Approach 2: Hashmap
# -------------------------------
def is_anagram_hashmap(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]

    return len(count) == 0


# -------------------------------
# Approach 3: Frequency Array (Optimal)
# -------------------------------
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = [0] * 26

    for i in range(len(s)):
        counts[ord(s[i]) - ord('a')] += 1
        counts[ord(t[i]) - ord('a')] -= 1

    # constant size loop → O(1)
    return all(c == 0 for c in counts)


# -------------------------------
# Example Run
# -------------------------------
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    print("Sorting:", is_anagram_sort(s, t))
    print("Hashmap:", is_anagram_hashmap(s, t))
    print("Optimal:", is_anagram(s, t))


# -------------------------------
# Key Learning
# -------------------------------
# Using a fixed-size frequency array reduces space complexity
# from O(n) to O(1) when character set is limited.
