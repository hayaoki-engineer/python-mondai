# 5. データ構造

# 5.1 リスト

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# 'apple' がリストに何回出現するかをカウントして表示
print(fruits.count('apple'))

# 'banana' がリストの何番目にあるかを表示
print(fruits.index('banana'))

# 4番目以降で 'banana' が何番目にあるかを表示
print(fruits.index('banana', 4))

# リストを逆順にする
fruits.reverse()
print(fruits)

# リストをソート
fruits.sort()
print(fruits)

fruits.pop()
print(fruits)

# 5.1.1 リストをスタックとして使う

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)
# [3, 4, 5, 6, 7]
print(stack.pop())
# 7
print(stack)
# [3, 4, 5, 6]

# 5.1.2 リストをキューとして使う

from collections import deque

queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')

print(queue.popleft())

# 5.1.3 リスト内包表記

squares = []
for x in range(10):
  squares.append(x**2)

print(squares)

squares = [x**2 for x in range(10)]
print(squares)

[(x, y) for x in [1, 2, 4] for y in [2, 3, 6] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)

# 5.1.4 ネストしたリスト内包表記

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]

# 5.2 del文

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

# リストの全要素を削除
del a[:]
print(a)

# 5.3 タプルとシーケンス

# 5.4 集合

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# {'orange', 'pear', 'apple', 'banana'}

print('orange' in basket)
# True
print('crabgrass' in basket)
# False

a = set('aabbcc')
print(a)

# 5.5 辞書

tel = {'jack': 4098, 'sape': 4139}
tel['quido'] = 4127
print(tel)
# {'jack': 4098, 'sape': 4139, 'quido': 4127}

print(tel['jack'])
# 4098

del tel['sape']
print(tel)
# {'jack': 4098, 'quido': 4127}

tel['irv'] = 4127
print(tel)
# {'jack': 4098, 'quido': 4127, 'irv': 4127}

print(list(tel))
# ['jack', 'quido', 'irv']

print(sorted(tel))
# ['irv', 'jack', 'quido']

print('quido' in tel)
# True

print('jack' not in tel)
# False

print(dict([('sape', 4139), ('quido', 4127), ('jack', 4098)]))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

print({x: x**2 for x in (2, 4, 6)})
# {2: 4, 4: 16, 6: 36}

# 5.6 ループのテクニック

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
# apple
# apple
# banana
# orange
# orange
# pear

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# apple
# banana
# orange
# pear

# 5.7 条件

# 5.8 シーケンスとその他の型の比較

print((1, 2, 3) < (1, 2, 4))
# True

print([1, 2, 3] < [1, 2, 4])
# True

print(['ABC' < 'C' < 'Pascal' < 'Python'])
# [True]

print((1, 2, 3, 4) < (1, 2, 4))
# True

print((1, 2) < (1, 2, -1))
# True

print((1, 2, 3) == (1.0, 2.0, 3.0))
# True

print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
# True