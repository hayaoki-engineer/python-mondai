# 3: 
# 【A】～【E】の行にある#から始まる文字列のうち
# Pythonではコメントとして解釈されないものはどれか。

# あいさつ文を表示します。                  # 【A】
x = 'Hello'  # Helloを変数に代入します。    # 【B】
# Worldを変数に                            # 【C】
# 代入します。                             # 【D】
y = 'World!'
# print('{}!{}!! #あいさつ文はここまでです。'.format(x, y))  # 【E】

# 4

a = 10
b = a ** 2
c = b % 20 + 5
d = 8
e = d / b
f = d // c

print ('{0}, {1}'.format(e, f))
# 0.08, 1

# 5

a = "She said,\"He" + 3 * "y" + "!"
b = "How are you?\" "
print (a, b)
# She said,"Heyyy! How are you?"

# 6

Zen = 'NowIsBetterThanNever'
print('{}{}{}{}'.format(Zen[5], Zen[10], Zen[-7], Zen[-3:-1]))
# Brave

# 7

Zen = 'SimpleIsBetterThanComplex'

# print(Zen[:])
# SimpleIsBetterThanComplex

# print(Zen[1000:])
# ''

# print(Zen[5:1000])
# eIsBetterThanComplex

# Zen[0] = 'J'
# TypeError: 'str' object does not support item assignment

# print(Zen[:1000] + 'J')
# SimpleIsBetterThanComplexJ

# 8

a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a+b
# 1,1,2,3,5,8,

# 9

colors = ['red', 'green', 'blue']

colors.append('yellow')
print(colors)
# ['red', 'green', 'blue', 'yellow']
colors.insert(0,'purple')
print(colors)
# ['purple', 'red', 'green', 'blue', 'yellow']

for color in colors[2:]:
    print(color, len(color), end = ', ')
# green 5, blue 4, yellow 6, 

# 10 難しい

# 外側のループ：2から9までの数字を順番にチェック
for n in range(2, 10):
    # 内側のループ：その数が割り切れるかをチェック
    for x in range(2, n):
        # もし割り切れたら（余りが0なら）
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break  # 内側のループを抜ける
    else:
        # 一度も割り切れなかったら、それは素数
        print(n, 'is a prime number')

# 11

# -10から-30まで-5ずつ減少させながら数値を生成するforループ
for i in range(-10, -30, -5):
    print(i, end=", ")
    
# -10, -15, -20, -25, -30, 

# 12

# このコードは、リストの要素とそのインデックスを同時に表示する例です。

# Zenリストを定義し、5つの単語を格納
Zen = ['Now','is','better','than','never']

# range(len(Zen))で0から4までの数値を生成し、
# それぞれの数値をインデックスとしてZenリストの要素にアクセス
for i in range(len(Zen)):
    print(i, Zen[i])  # インデックスと要素を出力

# より簡潔な書き方として、enumerate()関数を使用することもできます:
# for i, v in enumerate(Zen):
#     print(i, v)

# 0 Now
# 1 is
# 2 better
# 3 than
# 4 never

# 13

i = 5
i = 6

def f(arg = i):
    i = 7
    print(arg)

i = 8
i = 9

f()
# 6

# 14

def culc(a, b=1, squares=[], cubes=[]):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes

print(culc(1))
# ([1], [1])

print(culc(2, 3))
# ([1, 4], [1, 27])

print(culc(3, 4))
# ([1, 4, 9], [1, 27, 64])

#15. 次の関数を呼び出す際に、引数の指定として正しいものはどれか。

def location(city, state, country='Japan'):
    print("I live in",country,".")
    print("My company is located in",city,",",state,".")

# location(state='Tokyo', city='chiyoda')
# location(state='California', country='USA', 'San Francisco')
# location(city='Haryono', state='Jakarta', zipcode='12830')
# location('Geelong', city='Melbourne')
# location()

# 16 次のコード1行目のaに入るものとして正しいものはどれか。

# def shop(name, a):
#     print("flowershop:", name)
#     for arg in arguments:
#         print(arg)
#     print("**Recommended**")
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print(kw, ":", keywords[kw])

# shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")

# #実行結果
# flowershop: Iris
# Open: 9:30 am
# Close: 10:30 pm
# Monday and holidays are closed.
# **Recommended**
# bouquet : Sunflower
# dried : Rose
# plants : Pachira


# arguments, keywords
# *keywords, **arguments
# *arguments, **keywords
# **arguments, *keywords
# **keywords, *arguments

# 3種類の引数を受け取ることができる。
# 普通の引数
# *arguments 複数の値をまとめて受け取る
# **keywords 名前を付きの値をまとめて受け取る

# 18 次の結果を得たい場合に、コードの1行目～3行目を代替し同じ結果を出力するものとして正しいものはどれか。

cubes = []
for x in range(5):
    cubes.append(x ** 3)

print(cubes)
# [0, 1, 8, 27, 64]

cubes = [x ** 3 for x in range(5)]
print(cubes)

# 19. 次の実行結果を得たい場合に、コードの【A】に入るものとして正しいものはどれか。

# 実行結果
# [5, 25, 125]

# コード
matrix = [[2, 3, 5], [4, 9, 25], [8, 27, 125]]
power = [row[2] for row in matrix]
print(power)

# 20. 次の実行結果を得たい場合に、コードの【A】と【B】に入るものの組み合わせとして正しいものはどれか。

# 実行結果
# deque(['cow', 'dog', 'elephant', 'fox'])

from collections import deque
queue = deque(["bear", "cow", "dog", "elephant","fox"])
queue.append("goat")
queue.popleft()
queue.pop()
print(queue)