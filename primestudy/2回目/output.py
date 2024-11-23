# 23

## ディクショナリ

my_dict = {
  "key1": "value1", 
  "key2": "value2",
  "key3": "value3"
}

# ディクショナリの変更
my_dict["key1"] = "value1_new"
print(my_dict)
# {'key1': 'value1_new', 'key2': 'value2', 'key3': 'value3'}

# 新しいキーの追加
my_dict["key4"] = "value4"
print(my_dict)
# {'key1': 'value1_new', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# キーは変更不能であるため、キーを変更しようとするとエラーが発生する。
my_dict["key1"] = "new_key1"
print(my_dict)

# タプル → 変更不能なイミュータブル

my_tuple = (1, 2, 3)
print(my_tuple)
# (1, 2, 3)

# タプルは変更不能であるため、タプルの要素を変更しようとするとエラーが発生する。
# my_tuple[0] = 10
# TypeError: 'tuple' object does not support item assignment

# リスト → 変更可能なミュータブル

my_list = [1, 2, 3]
print(my_list)
# [1, 2, 3]

# リストは変更可能であるため、リストの要素を変更することができる。
my_list[0] = 10
print(my_list)
# [10, 2, 3]

