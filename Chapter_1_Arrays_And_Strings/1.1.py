# isUnique
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# Current Solution
# Time Complexity: O(1)
# Space Complexity: O(n) where n is length of string.

def isUnique(str):
    if len(str) > 128:
        return False

    existingLetters = {}
    for letter in str:
        if letter in existingLetters:
            return False
        else:
            existingLetters[letter] = True
    return True


print(isUnique("r"))  # should print True
print(isUnique("strawberry"))  # should print False
print(isUnique("Paul"))  # should print True
print(isUnique("Piper"))  # should print True
