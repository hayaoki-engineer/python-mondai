# 4.1 If文

# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# 4.2 for文

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# 4.3 range()関数

for i in range(5):
    print(i)

print(list(range(5, 10)))
# [5, 6, 7, 8, 9]

print(list(range(0, 10, 3)))
# [0, 3, 6, 9]

print(list(range(-10, -100, -30)))
# [-10, -40, -70]

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb

# 4.4 break文

for n in range(2, 10):  # 2から9までの数値を順番に処理
    for x in range(2, n):  # nより小さい数値xについて処理
        if n % x == 0:  # nがxで割り切れる場合
            print(f"{n} equals {x} * {n//x}")  # nがxの何倍かを表示
            break  # このnについての処理を終了

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

# 4.5 else

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# 4.6 pass

# 4.7 match文

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(404))

# 4.8 関数

def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(5)