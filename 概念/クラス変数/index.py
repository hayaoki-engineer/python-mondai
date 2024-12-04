# クラス変数 → クラス名.変数名

class MyClass:
    # クラス変数
    PI = 3.14

print(MyClass.PI)
# 出力:
# 3.14

class MyClass2:
    # クラス変数を初期化
    count = 0

    def __init__(self):
        #クラス変数をカウントアップ
        MyClass2.count += 1

a1 = MyClass2()
a2 = MyClass2()
print(MyClass2.count)
# 出力:
# 2


    