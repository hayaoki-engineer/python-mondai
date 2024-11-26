# 8. エラーと例外

# コメント： チュートリアルの説明が難しい

# a = 2
# b = 0
# print(a / b)

# a = [1, 2, 3]
# print(a[0])
# print(a[100])

# a = 2
# b = "abc"
# print(a + b)

try:
  a = 2
  b = 0
  print(a / b) # ここで例外が発生
except ZeroDivisionError:
  # 例外処理
  print("0での割り算")

try:
  a = [1, 2, 3]
  print(a[0])
  print(a[100]) # ここで例外が発生
except IndexError:
  # 例外処理
  print("インデックスが範囲外")

try:
  a = 2
  b = "abc"
  print(a + b) # 例外が発生
except TypeError:
  print("異なる型の演算")
