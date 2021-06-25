# URLify
# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the true length of the string.
# (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)

# Current Solution
# Time Complexity: O(n) where n is the length of str
# Space Complexity: O(n) where n is the newLength

def URLify(str, length):
    # calculate length of new potential string
    newLength = 0
    for char in str:
        if char == ' ':
            newLength += 2
        newLength += 1

    # use a reader and writer pointer
    writer = newLength - 1
    reader = length - 1
    URL = [None] * newLength

    for i in range(reader, -1, -1):
        # if I read a space, then write '%20' and move writer pointer ahead 3, else just copy
        if str[reader] == ' ':
            for i in reversed('%20'):
                URL[writer] = i
                writer -= 1
        else:
            URL[writer] = str[reader]
            writer -= 1
        reader -= 1
    return URL


print(URLify("I like bread.", 13))  # should print "I%20like%20bread."
