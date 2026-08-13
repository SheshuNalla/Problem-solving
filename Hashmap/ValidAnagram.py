s = "car"
t = "cat"
count = {}
for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
for char in t:
    if char in count:
        count[char] -= 1
    else:
        print(False)
print(all(value == 0 for value in count.values()))