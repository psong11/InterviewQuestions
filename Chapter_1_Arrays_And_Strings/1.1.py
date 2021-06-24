# isUnique
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUnique(str):
    num = 0
    existingLetters = {}
    for index, letter in enumerate(str):
        if letter in existingLetters:
            continue
        else:
            num += 1
            existingLetters[letter] = index
    print(num)


isUnique("strawberry")  # should print 8
isUnique("Paul")  # should print 4
isUnique("I like it.")  # should print 8
