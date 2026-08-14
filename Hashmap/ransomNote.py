def ransom(ransomNote, magazine):

    count = {}
    for char in magazine:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in ransomNote:
        if char in count and count[char] > 0:
            count[char] -= 1
        else:
            return False
    return True

ransomNote = "aa"
magazine = "ab"

print(ransom(ransomNote, magazine))