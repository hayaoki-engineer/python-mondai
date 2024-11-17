# 1
# and : 両方の条件がTrueの場合にTrueを返す
# or : どちらかの条件がTrueの場合にTrueを返す
for i in range(1, 7):
  if i % 2 == 0 and i % 3 == 0:
    print(f"{i}は6の倍数です")
  elif i % 2 == 0 or i % 3 == 0:
    print(f"{i}は2か3の倍数です")
  else:
    print(f"{i}は2の倍数でも3の倍数でもありません")

# 2
# and :最初の条件がFalseの場合は、それ以降の条件を評価しない
# or :最初の条件がTrueの場合は、それ以降の条件を評価しない
def num(value):
  return value

value1 = num(0) and num(1) and num(2)
value2 = num(0) or num(1) or num(2)
print(value1, value2)
# 0 2

# 3
# 省略

# 4
# 正しい記述
data = [1, 2, 3]
for i in data:
    print(i)

# 誤った記述
# data = [1, 2, 3]
# for i in data do:
#     print(i)
# Pythonでは'do'は不要です
# RubyやBashのような書き方はエラーになります

# 5
for i in range(4):
  print(i)
# 0 1 2 3

for i in range(0, 4):
  print(i)
# 0 1 2 3

for i in range(1, 8, 2):
  print(i)
# 1 3 5 7

for i in range(1, 4):
  print(i)
# 1 2 3

# 6
for c in "HELLO":
  if c == "L":
    break
print(c)

# 7
# 辞書のキーと値を同時に取得する
data = {"name": "太郎", "age": 20}
for key, value in data.items():
    print(f"{key}: {value}")
# name: 太郎
# age: 20

# 8
# enumerate()関数は、イテラブルオブジェクトのインデックスと要素を同時に取得できます
# この例では文字列"WORD"の各文字とそのインデックスを取得しています
# i にはインデックス(0,1,2,3)が、c には各文字(W,O,R,D)が入ります
# i == 2 の時、つまり3番目の文字'R'を出力します
for i, c in enumerate("WORD"):
  if i == 2:
    print(c)

# 9
print(list(reversed(sorted(["EAT"]))))
# ['T', 'E', 'A']

# 10
# zip()関数は2つのリストを同時に反復処理します
# n には [1, 2, 3] の数値が順番に入ります
# c には ["1", "2", "3"] の文字列が順番に入ります
 # 文字列 c を n 回繰り返して出力します
for n, c in zip([1, 2, 3], ["1", "2", "3"]):
  print(c * n)
# 1
# 22
# 333
