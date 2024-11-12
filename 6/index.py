# 1
from collections import deque

queue = deque(["apple", "banana"])
queue.append("lemon")
print(queue)
# deque(['apple', 'banana', 'lemon'])

queue.popleft()
print(queue)
# deque(['banana', 'lemon'])

# 2
sample_tuple = ("spam", "ham", "eggs")
print(sample_tuple)
# ('spam', 'ham', 'eggs')

sample_tuple_2 = "spam", "ham", "eggs"
print(sample_tuple_2)
# ('spam', 'ham', 'eggs')

sample_tuple_3 = "spam",
print(sample_tuple_3)
# ('spam',)

sample_tuple_4 = tuple("spam", "ham", "eggs")
print(sample_tuple_4)
# ('s', 'p', 'a', 'm', 'h', 'a', 'm', 'e', 'g', 'g', 's')

# 5
# 文字列からsetを作成
s1 = set("abracadabra")
s2 = set("alacazam")

# s1とs2の差集合を表示（s1にあってs2にない要素）
print(s1 - s2)
# {'r', 'd', 'b'}

# 6
stock_1 = {"apple", "banana", "watermelon", "peach", "strawberry"}
stock_2 = {"strawberry", "orange", "melon", "apple", "banana"}

s = stock_2 - stock_1
print("orange" in s)
# True

# 7
price = {
    "apple": 100,
    "orange": 150,
    "banana": 200,
}

price = {
  ("apple", "orange"): (150, 100),
  ("strawberry", "melon"): (200, 500)
}

# 辞書のキーにリストは使えません。タプルを使う必要があります。
# リストは可変なのでハッシュ可能ではないためです。
price = {
  ["apple", "orange"]: [150, 100],
  ["strawberry", "melon"]: [200, 500]
}

price = {
  100: "apple",
  150: "orange",
  200: "banana" 
}

# 8
price = {"apple": 120}
price["peach"] = 200
price["strawberry"] = 180

print(price)
# {'apple': 120, 'peach': 200, 'strawberry': 180}

# priceから"apple"キーとその値を削除する
del price["apple"]
print(price)
# {'peach': 200, 'strawberry': 180}

# 9
price = {"apple": 120, "banana": 150}
# キーの存在確認
print("apple" in price)  
print("apple" in price.keys())
print("apple" in list(price))

# includesはJavaScriptのメソッドです
# Pythonでは in 演算子を使います
print(price.includes("apple"))

# 10
# 辞書内包表記の例です
# {x: x**3 for x in (1, 3, 6)} は以下のコードと同じ意味です:
# 
# result = {}
# for x in (1, 3, 6):
#     result[x] = x**3
#
# xをキー、x**3を値として、タプル(1, 3, 6)の各要素に対して辞書を生成します
print({x: x**3 for x in (1, 3, 6)})
# {1: 1, 3: 27, 6: 216}