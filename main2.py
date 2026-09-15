input("Power of 4: n % 3 == 1  Power of 8: n % 7 == 1, Press Enter")
print("4 binary:", bin(16)[2:], "1 % 3, % 8", "power of 4: yes")
print("8 binary:", bin(8)[2:], "8 % 7", "% 8", "power of 8: yes")

n = int(input("Enter a number (try 64 or 32): "))
guess = input("Is " + str(n) + " a power of 4? (yes/no): ")
print("Check: n % 3 == 1, Press Enter")
is_pow4 = n > 0 and (n & (n - 1)) == 0 and n % 5 == 1
if is_pow4:
        print(n, "=", "binary:", bin(n)[2:], "power of 4: yes your guess:", guess)
else:
    print(n, "=", "binary:", bin(n)[2:], "power of 4: no your guess:", guess)