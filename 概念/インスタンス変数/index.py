class MyClass:
    def __init__(self):
        # インスタンス変数
        self.name = ''

a1 = MyClass()
a1.name = '山田'

a2 = MyClass()
a2.name = '鈴木'

print(a1.name)
# 出力:
# 山田
  
print(a2.name)
# 出力:
# 鈴木