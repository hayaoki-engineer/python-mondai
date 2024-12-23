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

# try:
#   a = 2
#   b = 0
#   print(a / b) # ここで例外が発生
# except ZeroDivisionError:
#   # 例外処理
#   print("0での割り算")

# try:
#   a = [1, 2, 3]
#   print(a[0])
#   print(a[100]) # ここで例外が発生
# except IndexError:
#   # 例外処理
#   print("インデックスが範囲外")

# try:
#   a = 2
#   b = "abc"
#   print(a + b) # 例外が発生
# except TypeError:
#   print("異なる型の演算")

# try:
#   a = 1
#   b = 0
#   print(a / b)
# except ZeroDivisionError:
#   print("例外が発生")
# else:
#   print("例外が発生せずに終了")

# try:
#   a = 1
#   b = 1
#   print(a / b)
# except ZeroDivisionError:
#   print("例外が発生")
# else:
#   print("例外が発生せずに終了")
# finally:
#   print("最後に終了")

try:
  a = 1
  b = 0
  print(a / b)
except ZeroDivisionError as e:
  # 例外メッセージを表示
  print(e)
  # 例外クラスの名前を表示
  print(type(e))

try:
  a = [1, 2, 3, 4]
  print(a[100])
except IndexError as e:
  print(e)
  print(type(e))
