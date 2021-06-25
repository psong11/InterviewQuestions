# Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards or backwards.
# A permutation is a rearrangement of letters.
# A palindrome does not need to be limited to just dictionary words.

# Current Solution
# Time Complexity:
# Space Complexity:

def palPerm(str):
    str = str.replace(" ", "")
    str = str.lower()
    # sort the string
    # iterate through the string checking if each letter and the letter immediately after it is the same letter
    letterCount = {}
    for char in str:
        if char in letterCount:
            letterCount[char] += 1
        else:
            letterCount[char] = 1

    if len(str) % 2 == 0:  # even length
        for letter in letterCount:
            if letterCount[letter] % 2 != 0:
                return False
        return True
    else:  # odd length
        hasOdd = False
        for value in letterCount.values():
            if hasOdd:
                return False
            if value % 2 != 0:
                hasOdd = True

    return True


print(palPerm("taco cat"))
print(palPerm("TaCo cAt"))
print(palPerm("hello world"))
print(palPerm("car race"))
print(palPerm("car racer"))
