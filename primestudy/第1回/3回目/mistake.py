# 8 難しい

# フィボナッチ数列
a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a+b

# 10 難しい

# 外側のループ：2から9までの数字を順番にチェック
for n in range(2, 10):
    # 内側のループ：その数が割り切れるかをチェック
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
        continue
    break

# 実行結果
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2

# 16 次のコード1行目のaに入るものとして正しいものはどれか。

def shop(name, *arguments, **keywords):
    print("flowershop:", name)
    for arg in arguments:
        print(arg)
    print("**Recommended**")
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")

# "Open: 9:30 am", "Close: 10:30 pm", "Monday and holidays are closed."は*argumentsに入ります。これらは通常の引数として受け取られ、リストのように扱われます。
# bouquet="Sunflower", plants="Pachira", dried="Rose"は**keywordsに入ります。これらはキーワード引数として受け取られ、辞書のように扱われます。

# 25


# 28. 次のコードを実行して「整数a:」に「5」、「整数b:」に「0」を入力した場合の正しい結果はどれか。なお選択肢中の「, 」は改行に読み替えること。

try:
    int_a = int(input('整数a:'))
    int_b = int(input('整数b:'))
    print(int_a ** 2)
    print((int_a ** 2) / int_b)
except(ValueError) as v:
    print(type(v))
    print('C')
except(ZeroDivisionError) :
    print('D')
except:
    print('E')
else:
    print('F')
finally:
    print('G')

# 処理の流れ
# ユーザーが「整数a:」に「5」、次に「整数b:」に「0」を入力。
# int_aに5、int_bに0が格納される。
# print(int_a ** 2)で25が出力。
# print((int_a ** 2) / int_b)でゼロ除算が発生し、ZeroDivisionErrorが発生。
# 5. except(ZeroDivisionError)ブロックが実行され、print('D')が出力。
# 6. 最後にfinallyブロックが実行され、print('G')が出力。


# 31

# 35

# 39 仮想環境

# 誤っているものはどれか。

# Pythonの仮想環境とは、特定バージョンのPythonのインストール実体を含む、独立に機能するディレクトリツリーおよびパッケージなどから成り立つものである。

# 仮想環境をアクティベートしたら、pipを使ってパッケージのインストール、アップグレード、リムーブができる。pipはデフォルトではPython Package Indexからパッケージをインストールする。

# pip install --upgrade とすることで当該パッケージを最新バージョンにアップグレードすることができる。

# 誤っている
# pip uninstall にパッケージ名を指定すると、その仮想環境からパッケージを削除できる。削除対象となるパッケージの複数指定はできない。← 誤り

# pip listはその仮想環境にインストールされたすべてのパッケージを表示する。pip freezeも同様の働きをするが、出力形式が異なる。

# 40.

# 次の記述に関して誤っているものはどれか。

# 変数とモジュールの補完はインタープリタの起動時に自動で有効になっている。

# [Tab]キーを押すと補完機能が呼び出せる。この機能はPythonの文（命令）の名前、現在のローカル変数、使用できるモジュール名を検索するものである。

# 誤っている
# デフォルト設定ではユーザーディレクトリの「.pyhistory」ファイルにヒストリが保存される。ヒストリは対話型インタープリタセッションで利用できる。

# 拡張された対話型インタープリタとしてbpythonがある。これはタブ補完、オブジェクト探索、高度なヒストリ管理などの機能を持つ。

# bpythonに類似した拡張対話環境にIPythonがある。IPythonは「pip install ipython」でインストールでき、IPythonの対話モードはipythonコマンドで起動できる。

