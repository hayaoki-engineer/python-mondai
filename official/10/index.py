# 1
# このコードはDuckクラスを定義しています:

# 1. クラス変数
#   - family: すべてのDuckインスタンスで共有される"Anatidae"(カモ科)という値

# 2. コンストラクタ (__init__)
#   - インスタンス生成時に自動的に呼び出される
#   - self.birdsong: 各インスタンス固有の"quack"という鳴き声を設定

# 3. インスタンスメソッド
#   - show_family(): Duckの分類(family)を文字列で返す
#   - self.familyでクラス変数にアクセス

class Duck:
  family = "Anatidae"

  def __init__(self):
    print("__init__メソッドが呼び出されました")
    self.birdsong = "quack"
    print(f"birdsongを{self.birdsong}に設定しました")
  
  def show_family(self):
    print("show_familyメソッドが呼び出されました") 
    result = f"Ducks belong to the family {self.family}."
    print(f"戻り値: {result}")
    return result
  
duck = Duck()
duck.show_family()
  
# 2
# duck = Duck()

# 3
class Duck:
  def __init__(self):
    self.birdsong = "quack"

  def sing(self):
    birdsong = "ga-ga-"
    print(birdsong)
    print(self.birdsong)
    self.birdsong = "coin"
    print(self.birdsong)
    print(birdsong)
  
duck = Duck()
duck.sing()

# 4
# 省略

# 5
# class Duck(Bord)

# 6
# isinstance()