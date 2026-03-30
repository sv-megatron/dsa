"""
Problem: Group Anagrams
LeetCode #: 49
Difficulty: Medium

Primary Pattern: Arrays + Hashing
Secondary: Frequency Count

Problem Statement:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

--------------------------------------------------

Approach 1: Sorting

Idea:
- Sort each word and use the sorted string as a key
- Anagrams will have the same sorted representation

Example:
"eat" → "aet"
"tea" → "aet"

Time Complexity Analysis:
- n = number of words
- k = average length of each word
- Sorting each word → O(k log k)
- Loop runs n times

Total:
O(n * k log k)

Space Complexity:
- Storing all words → O(nk)
- Keys also take space → O(nk)

--------------------------------------------------

Approach 2: Frequency Count (Optimal)

Key Insight:
- Anagrams have identical character frequencies
- Use a fixed-size array (26 for lowercase letters) as a signature

Example:
"eat" → [1,0,0,...,1,...]
"tea" → same array → same group

Since lists are not hashable, convert to tuple.

Time Complexity Analysis:
- Loop over n words → O(n)
- Count characters in each word → O(k)

Total:
O(n * k)

Space Complexity:
- Store all words → O(nk)
- Keys are fixed size (26) → O(1) each

Overall:
O(nk)

--------------------------------------------------
"""


# -------------------------------
# Approach 1: Sorting
# -------------------------------
def group_anagrams_sort(strs):
    hashmap = {}

    for word in strs:
        key = "".join(sorted(word))  # O(k log k)

        if key not in hashmap:
            hashmap[key] = []

        hashmap[key].append(word)

    return list(hashmap.values())


# -------------------------------
# Approach 2: Frequency Count (Optimal)
# -------------------------------
def group_anagrams(strs):
    hashmap = {}

    for word in strs:
        count = [0] * 26  # fixed size → O(1)

        # count characters → O(k)
        for c in word:
            count[ord(c) - ord('a')] += 1

        key = tuple(count)  # convert to hashable

        hashmap.setdefault(key, []).append(word)

    return list(hashmap.values())


# -------------------------------
# Example Run
# -------------------------------
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print("Sorting Approach:")
    print(group_anagrams_sort(strs))

    print("\nOptimal Approach:")
    print(group_anagrams(strs))


# -------------------------------
# Key Learnings
# -------------------------------
# 1. Sorting gives a simple solution but costs O(k log k) per word.
# 2. Frequency counting avoids sorting and improves to O(k).
# 3. Tuples are used because they are immutable and hashable.
# 4. This problem is a classic example of grouping using hashing.
