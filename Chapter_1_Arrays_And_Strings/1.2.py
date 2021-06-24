# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(first, second):
    howManyLetters = {}
    if len(first) != len(second):
        return False
    else:
        for index, letter in enumerate(first):
            if letter in howManyLetters:
                howManyLetters[letter] += 1
            else:
                howManyLetters[letter] = 1


print(checkPermutation("taco", "coat"))
print(checkPermutation("dad", "add"))
