# String Compression
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a-z).

# Current Solution
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(2n) where n is the number of unique characters

def compress(s):

    newString = []
    count = 1
    for i in range(len(s)):
        if i == len(s)-1 or s[i+1] != s[i]:
            newString.append(s[i])
            newString.append(str(count))
            count = 1
        else:
            count += 1
    if len(newString) >= len(s):
        return s
    else:
        return "".join(newString)


print(compress("aabcccccaaa"))
print(compress("abcdefghijklmnopqrstuvwxyz"))
