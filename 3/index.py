# 1
# リストの特徴

my_list = [1, "hello", 3.14, True]

# インデックスを使って要素を参照
print(my_list[0])  # 1を出力
print(my_list[1])  # "hello"を出力

# インデックスを使って要素を更新
my_list[2] = 3.141592
print(my_list)  
# [1, "hello", 3.141592, True]

# 2
data = [1, 2, 3, 4]
print(data[:2], data[3:])
#  [1, 2] [4]

# 3
data = [1, 2]
data.append(3)
print(data)
# [1, 2, 3]

#4
data = [1, 2, 3, 4, 5]
print(len(data))  # 5を出力

# 5
# リストの要素に関して

# リストの入れ子
nested_list = [[1, 2], [4, 5]]

## 入れ子になったリストの要素へのアクセス
print(nested_list[0])      # [1, 2]を出力
print(nested_list[0][1])   # 2を出力

## 入れ子リストの更新
nested_list[1][2] = 60
print(nested_list)
# [[1, 2], [4, 5, 60]]

# 6
data = [[1, 2], [3, 4]]
print([data[0][0], data[1][1]])

# 7
# pop()メソッドは常にリストの最後（末尾）の要素を取り出します
stack = [1, 2, 3, 4]
data = []

while stack:
    data.append(stack.pop())
print(data)

# 9
data = []
for i in [1, 2, 3]:
    for j in [1, 2]:
        if i != j:
            data.append((i, j))
print(data)

# 上記と同じ出力結果の記述
print([(i, j) for i in [1, 2, 3] for j in [1, 2] if i != j])