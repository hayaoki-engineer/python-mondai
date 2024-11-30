# 6

import math

print(f"tauの値はおよそ{math.tau:.3f}である")
# => tauの値はおよそ6.283である
# math.tauは円周率の2倍の値を表す定数
# 3fは小数点以下3桁まで表示することを表す


# 15

default_name = "Taro"

def hello1(name=default_name):
  return f"Hello, {name}."

def hello2(name=None):
  if name is None:
    name = default_name
  return f"Hello, {name}."

default_name = "Hanako"
print(hello1(), hello2())
# => Hello, Taro. Hello, Hanako.


# 16

# 2つの引数を連結する関数
def concat(arg1, arg2, /, sep="/"):
  # 引数1と引数2をsepで連結して返す
  return sep.join((arg1, arg2))

# 2つの単語を連結する
words = ["foo", "bar"]
# 連結時のオプションを設定
options = {"sep": "_"}
# 連結した結果を表示
print(concat(*words, **options) )
# => foo_bar

# *は位置専用引数を表す
# **はキーワード専用引数を表す

# 20

def value(arg):
  return arg

result1 = value(0) and value(1) and value(2)
# 0がFalseと評価されるため、その時点でand演算の結果がFalseとなり、以降のvalue関数は評価されない
result2 = value(0) or value(1) or value(2)
# がFalseと評価されるため、次のvalue(1)が評価され、結果は1となる

print(result1, result2)
# => 0 1

# 23

# setの性質

# 追加した要素の順序は保持されない

sample_set = {3, 1, 2}
print(sample_set)
# => {1, 2, 3} # 要素の順序は保持されない

# 要素を追加
sample_set.add(4)
print(sample_set)
# => {1, 2, 3, 4} # 追加した要素の順序は保持されない

# 26

# 29

try:
  times = input("分割回数:")
  value = 100 / int(times)
  print(value)
except () :
  print('エラーが発生しました')

# ValueError: 数値ではない文字列が入力された場合
# ZeroDivisionError: 0が入力された場合

# 33

class Duck:
  def __init__(self):
    # 1. Duckオブジェクトが初期化された際に、鳥の鳴き声を"quack"に設定
    self.birdsong = "quack"

  def sing(self):
    # 鳥の鳴き声を"ga-ga-"に設定
    birdsong = "ga-ga-"
    print(birdsong)

    # Duckオブジェクトの鳴き声を表示
    print(self.birdsong)

    # Duckオブジェクトの鳴き声を"coin"に設定
    self.birdsong = "coin"
    print(self.birdsong)

    # "ga-ga-"を表示
    print(birdsong)

# 5. Duckオブジェクトを作成
duck = Duck()
# 6. 作成したDuckオブジェクトが鳴く
duck.sing()

# 34

# 35

# 36

# 37

# 38