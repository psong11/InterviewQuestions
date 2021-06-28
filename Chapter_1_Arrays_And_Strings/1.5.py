# One Away
# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

# Current Solution
# Time Complexity:
# Space Complexity:

# three cases: two insertions, an insertion and change, two changes

def oneAway(first, second):
    if abs(len(first) - len(second)) > 1:  # takes care of two insertions
        return False

# checking for double replacement, or insertion and replacement
    index1 = 0
    index2 = 0
    changed = False
    while index1 < len(first) and index2 < len(second):
        if first[index1] != second[index2]:
            if changed:
                return False
            changed = True
            # if lengths are same, then replacement happened
            # else then insertion happened
            if index1 == index2:
                if len(first) > len(second):
                    index1 += 1
                elif len(first) < len(second):
                    index2 += 1
        index1 += 1
        index2 += 1
    return True


# same string
print(oneAway("salami", "salami"))
# abs value of length greater than two
print(oneAway("paul", "paulie"))

# one insertion
print(oneAway("yoghurt", "yogurt"))
# one replacement
print(oneAway("yogurt", "yocurt"))

# one insertion, one replacement
# insertion first
print(oneAway("yoghurt", "yogurd"))
# replacement first
print(oneAway("bogurt", "yogurit"))

# two replacements
print(oneAway("yorurt", "vogurt"))
