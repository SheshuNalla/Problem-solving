def happyNumber(n):
    seen = set()
    while n!=1:
        total = 0
        for digit in str(n):
            total += int(digit) ** 2
        n = total

        if n in seen:
            return False
        seen.add(n)
    return True


n = int(input(" Enter a number: "))
print(happyNumber(n))