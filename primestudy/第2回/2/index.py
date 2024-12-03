# 2

# Pythonインタープリタに関する次の記述のうち、誤っているものはどれか。

# 正解
# インタープリタがスクリプト名（スクリプトのファイル名）と続く引数群を知らされると、これらは文字列のリストとなる。import listitems を実行することで、このリストにアクセスできる。
# => Pythonのインタープリタがスクリプト名や引数をimport listitemsでアクセスできるわけではないからです。実際には、スクリプト名や引数はsys.argvというリストに格納されます。

# 自分の答え
# 標準入力がttyデバイスに接続された状態で起動した場合は、コマンドを対話的に読み込んで実行するが、引数にファイル名を与えたり、標準入力からファイルを与えて起動した場合は、このファイルに入った「スクリプト」を読み込んで実行する。
https://www.goldwin.co.jp/ap/item/i/m/ND92335
# 8

# 25

# モジュールに関する次の記述のうち、誤っているものはどれか。

# 正解
# sys.pathが初期化されている場所は、入力スクリプトのあるディレクトリ、PYTHONPATHであり、インストールごとのデフォルトは含まれない。
# => インストールごとのデフォルトが含まれる

# 他の選択肢（正しい）
# パッケージとは、「ドット区切モジュール名」を使って、Pythonのモジュールを構築する方法である。
# あるモジュールがインポートされるときにインタープリタが検索する順序は、まずビルトインモジュール、次にsys.path変数で得られるディレクトリである。シンボリックリンクを置いてあるディレクトリはモジュール検索パスに入らない。
# Pythonはソースファイルの最終更新日時をコンパイル済みのバージョンと比較し、再コンパイルが必要か判断する。これは完全に自動的に行われる。
# コンパイル済みのモジュールはプラットフォーム非依存なので、ひとつのライブラリを異なるアーキテクチャのシステム間で共有できる。

# 31

# 次の実行結果を得たい場合、コードの【A】【B】【C】に入る組み合わせとして適切なものはどれか。

# 実行結果
# David is a
# strategic
# AI

class wexal(Exception):
    pass

name = 'David'

def func(name: int):
    try:
        if name != 0:
            raise_his_character(name)
    except wexal:
        print('strategic')
        # raise Exceptionを実行すると、Exceptionクラスの例外が発生する → 最後のtryブロックでキャッチされる
        raise Exception
    
def raise_his_character(a):
    print(a, 'is a')
    # raise wexalを実行すると、wexalクラスの例外が発生する → func関数内のexcept wexalでキャッチされる
    raise wexal
    print('naughty boy')

try:
    func(name)
except Exception:
    print('AI')

# 正解
# 【A】strategic【B】is a【C】naughty boy【D】AI


# 32

# 次のコードの実行結果として正しいものはどれか。なお各選択肢内は改行されているものとして読み替えること。

def scope():
    # locというローカル変数を初期化
    loc = "init"

    # do_local関数を定義
    def do_local():
        loc = "local"

    # do_nonlocal関数を定義
    def do_nonlocal():
      # 外側のスコープのlocを参照 => loc = "init"
      nonlocal loc
      # locの値 "init" を変更 => loc = "nonlocal"
      loc = "nonlocal"

    # do_global関数を定義 
    def do_global():
        # グローバルスコープのlocを参照
        global loc
        # グローバル変数のlocの値を "global" に設定
        loc = "global"

    do_local()  
    print("A:", loc)  
    do_nonlocal()
    print("B:", loc)
    do_global()
    print("C:", loc)

scope() 
# グローバル変数locの値を出力
print("D:", loc)

# 処理の流れ
# 1. scope関数を呼び出す
# 2. locというローカル変数を "init" で初期化
# 3. do_local関数を呼び出す
# 4. loc = "local"とする
# 5. print("A:", loc)とする
# 6. 結果はA: initとなる

# 正解
# A: init B: nonlocal C: nonlocal D: global


# 33

# 実行結果
# Need Speed?
# I'm Saya.
# Need Speed?
# I'm David.

class kusanagi():

    def s(self):
        print('Need Speed?')
        self.m()

    def m(self):
        print("I'm Saya.")

class wexal(kusanagi):
    def m(self):
        print("I'm David.")

k = kusanagi()
w = wexal()

# kのsメソッドを呼び出す
k.s()
# 出力:
# Need Speed?
# I'm Saya.

# wのsメソッドを呼び出す
w.s()
# 出力:
# Need Speed?
# I'm David.
    

# 35

# 36

# 37

from datetime import date
now = date.today()
print(now)
# 2024-12-02

# 39


