# 3.1.1 数

print(17 / 3)
# 除算 (/) は常に浮動小数点数を返す

print(17 // 3)
# 整数除算 (//) は常に整数を返す

print(17 % 3)
# 剰余 (%) は除算の余りを返す

print(5 ** 2)
# 累乗 (**) はべき乗を返す

width = 20
height = 5 * 9
print(width * height)
# 等号 (=) は変数に値を代入する

# tax = 6 / 3
# price = 12
# price * tax
# price + _
# _ は直前の式の結果を表す

# 3.1.2 テキスト

print('spam eggs')
# シングルクォートで文字列を表す

print("Paris rabbit got your back :)! Yay!")
# ダブルクォートで文字列を表す

print('1975')
# 1975

print('doesn\'t')
# クォートの中でクォートを使いたい場合、 \ を前に付け加えることで「エスケープ」をする必要があります。 

print("doesn't")
# 文字列で使用したいクォートとは別の方のクォートで囲むこともできます。

print(3 * 'un' + 'ium')
# 文字列を繰り返し連結することもできます。

print('Py' 
      'thon')
# 連続して並んでいる複数の 文字列リテラル (つまり、引用符に囲われた文字列) は、自動的に連結されます。

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
# 括弧で文字列をグループ化すると、複数行にわたる文字列を作ることができます。

prefix = 'Py'
print(prefix + 'thon')
# 変数とリテラルを連結したい場合は、+ を使う

word = 'Python'
print(word[0])
# 文字列はインデックスでアクセスできる

print(word[-1])
# 負のインデックスは文字列の末尾からアクセスできる

print(word[-2])
# 負のインデックスは文字列の末尾からアクセスできる

print(word[0:2])
# スライスは文字列の一部分を取り出すことができる

print(word[2:5])
# スライスは文字列の一部分を取り出すことができる

print(word[:2])
# インデックス 0 から 2 までのスライス

print(word[4:])
# インデックス 4 から末尾までのスライス

print(word[:2] + word[2:])
# Python

# print(word[42])
# インデックスが範囲外の場合はエラーになる

print(word[4:42])
# on

print(word[42:])
# インデックスが範囲外の場合は空の文字列を返す

# word[0] = 'J'
# 文字列は変更できない

# word[2:] = 'py'
# Pythonの文字列は不変（immutable）であるため、特定のインデックスの文字を直接変更することはできません。

print('J' + word[1:])
# 元の文字列と別の文字列が必要な場合は、新しく文字列を作成

print(word[:2] + 'py')
# Jython

s = 'supercalifragilisticexpialidocious'
print(len(s))
# 文字列の長さを取得するには len() 関数を使う

# 3.1.3 リスト

squares = [1, 4, 9, 16, 25]
print(squares)
# リストは角括弧で表される

print(squares[0])
# リストのインデックスは 0 から始まる

print(squares[-1])
# 負のインデックスはリストの末尾からアクセスできる

print(squares[-3:])
# 末尾から 3 つの要素をスライス

print(squares + [36, 49, 64, 81, 100])
# リストは連結できる

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)
# リストの要素は変更できる

cubes.append(216)
print(cubes)
# リストの末尾に要素を追加するには append() メソッドを使う

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(len(letters))
# リストの長さを取得するには len() 関数を使う


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
# リストの中にリストを入れることもできる