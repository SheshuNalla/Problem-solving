# def validPalindrome(s):
#     cleaned = ""
#     for char in s:
#         if char.isalnum():
#             cleaned += char.lower()
#     if cleaned == cleaned[::-1]:
#         return True
#     else:
#         return False


# print(validPalindrome(s))

def ValidPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True
s = input("enter a string: ")

print(ValidPalindrome(s))
