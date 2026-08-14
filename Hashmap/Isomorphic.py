def isomorphic(s, t):
    if len(s) != len(t):
        return False
    mapping = {}
    rev_mapping = {}
    for i in range(len(s)):
        if s[i] in mapping:
            if mapping[s[i]] != t[i]:
                return False
        if t[i] in rev_mapping:
            if rev_mapping[t[i]] != s[i]:
                return False

        mapping[s[i]] = t[i]
        rev_mapping[t[i]] = s[i]
    return True


s = "foo"
t = "bar"
print(isomorphic(s, t))