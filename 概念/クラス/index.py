class MyClass:

    # インスタンス生成時に呼び出される
    def __init__(self):
        self.name = ''
        print('インスタンス化されました')

    # getNameメソッド
    def getName(self):
        return self.name
    
    def setName(self, name):
        # インスタンス変数 self.name に引数 name（山田） を代入
        self.name = name

# クラスのインスタンスを生成
a = MyClass()

# setNameメソッドを呼び出し
a.setName('山田')

# getNameメソッドを呼び出し
print(a.getName())

# 出力:
# インスタンス化されました
# 山田