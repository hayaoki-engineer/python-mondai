# 1
# 正しい記述
def greet(name):
    print(f"こんにちは、{name}さん")

# 誤った記述
# def greet name:
#     print(f"こんにちは、{name}さん")
# 引数は()の中に書く必要があります

# 2
# 正しい記述
greet("太郎")

x = greet("太郎")
print(x)
# 関数の戻り値がない場合はNoneが返されます

x = greet
y = x("太郎")
print(y)
# 関数の戻り値がない場合はNoneが返されます

# x = greet "太郎"
# この呼び出し方は誤りです
# 関数呼び出しには()が必要です

# 4
def function(x, y="foo", z="bar"):
    print(x, y, z)

# 正しい記述
function("spam", y="ham", z="eggs")
# spam ham eggs

# 5
default_message_1 = "Hello"

def message(message_1=default_message_1, message_2=""):
    print(f"{message_1} {message_2}")

default_message_1 = "こんにちは"
message_2 = "world"

message(message_2=message_2)


# 6
def function(number, default_arg_list=[]):
    default_arg_list.append(number)
    return default_arg_list

print(function(1))
# [1]

print(function(2, [3, 4]))
# [3, 4, 2]

print(function(3))
# [1, 3]
# デフォルト引数のリストは関数呼び出し時に1度しか評価されません
# そのため、関数が呼び出されるたびにデフォルト引数のリストが更新されていきます

# 7
def function(name, *args, **kwargs):
    print(name)    # 通常の引数
    print(args)    # タプルとして受け取られる可変長引数
    print(kwargs)  # 辞書として受け取られるキーワード引数

function("spam", "ham", kwarg1="eggs", kwarg2="spamhameggs")
# spam
# ('ham',)
# {'kwarg1': 'eggs', 'kwarg2': 'spamhameggs'}

# 8
# 省略

# 9
func = lambda a, b: (b + 1, a * 2)
x, y = 1, 2
x, y = func(x, y)
print(x, y)
# 3 2

# 10
def func():
    """これはdocstringです"""
    pass

print(func.__doc__)
# これはdocstringです
