# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.

# Current Solution
# Time Complexity: O(f) + O(s) + O(n) where f is length of first string, s is length of second string, n is number of unique characters in first word
# Space Complexity: O(n)

def checkPermutation(first, second):
    # If the words are different length, I automatically know they are not permutations of each other.
    if len(first) != len(second):
        return False

    else:
        # Count how many of each letter appears in the first word.
        howManyLetters = {}
        for index, letter in enumerate(first):
            if letter in howManyLetters:
                howManyLetters[letter] += 1
            else:
                howManyLetters[letter] = 1

        # For each letter in the second word, I want to first check if it is in the dict.
        # If it is, then I will "use up" one of the letters.
        for letter in second:
            if letter in howManyLetters:
                if howManyLetters[letter] <= 0:
                    return False
                else:
                    howManyLetters[letter] -= 1
            else:
                return False

        # Make sure every letter was used completely.
        for letter in howManyLetters:
            if howManyLetters[letter] != 0:
                return False
        return True


print(checkPermutation("taco", "coat"))  # should print True
print(checkPermutation("dad", "add"))  # should print True
print(checkPermutation("mother", "motherr"))  # should print False
print(checkPermutation("Apple", "apple"))  # should print False
