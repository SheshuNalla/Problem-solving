def wordPattern(pattern, s):
    words = s.split()
    if len(words) != len(pattern):
        return False
    mapping = {}
    rev_mapping = {}
    for i in range(len(pattern)):
        if pattern[i] in mapping:
            if mapping[pattern[i]] != words[i]:
                return False
        if words[i] in rev_mapping:
            if rev_mapping[words[i]] != pattern[i]:
                return False

        mapping[pattern[i]] = words[i]
        rev_mapping[words[i]] = pattern[i]
    return True


s = "dog cat cat fish"
pattern = "aaaa"
print(wordPattern(pattern, s))