# isUnique
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUnique(str):
    # create blank hashmap (dict)
    existingLetters = {}
    # iterate through each letter in the string
    for index, letter in enumerate(str):
        # if the letter already existed somewhere earlier in the string, continue
        if letter in existingLetters:
            continue
        else:
            # add the current letter to the hashmap (dict)
            existingLetters[letter] = index
    return len(existingLetters)


print(isUnique("strawberry"))  # should print 8
print(isUnique("Paul"))  # should print 4
print(isUnique("I like it."))  # should print 8
