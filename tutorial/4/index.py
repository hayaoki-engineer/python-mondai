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

# 4.9

# 4.9.1 デフォルトの引数

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# 4.9.2 キーワード引数

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

# 位置引数で呼び出し
parrot(1000)
# キーワード引数で呼び出し
parrot(voltage=1000)
# キーワード引数で呼び出し（actionも指定）
parrot(voltage=1000000, action='VOOOOOM')
# 位置引数で呼び出し（voltage, state, actionを指定）
parrot('a million', 'bereft of life', 'jump')

# 4.9.3 特殊なパラメータ

# 4.9.4 任意の引数リスト

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

# 4.9.5 引数リストのアンパック

print(list(range(3, 6)))
# [3, 4, 5]

args = [3, 6]
print(list(range(*args)))
# [3, 4, 5]

# 4.9.6 ラムダ式

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
# 42
print(f(1))
# 43

# make_incrementor 関数は、引数 n を使ってラムダ関数を生成し、そのラムダ関数は n の値を保持したまま、任意の x に対して加算を行うことができます。これが、ラムダ関数とクロージャの基本的な動作です。
