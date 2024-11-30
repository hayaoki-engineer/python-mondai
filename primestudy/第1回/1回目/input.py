# 1 Pythonの特徴に関する次の記述のうち、誤っているものはどれか。

# Pythonはインタープリタ言語であり、コンパイル等が必要でないため、プログラム開発における時間を節約してくれる。インタープリタは対話的に使うことも可能である。
# PythonはWindows、MacOS、Linuxなど多くの環境で動作する。
# Pythonでは、文のグルーピングはカッコで囲うことでなくインデントで行われるなど、プログラムを小さく読みやすく書けるという特徴がある。ただ変数や引数の宣言は必要である。
# Pythonはフリーのオープンソースソフトウェアである。
# Pythonは機械学習やディープラーニング、データ解析、Webアプリケーションなど多くの分野を得意としている。

# 答え：
# 3番目の選択肢が誤り。
# Pythonでは変数や引数の宣言は必要ありません。なぜなら、Pythonは動的型付け言語であり、変数の型は自動的に推論されるためです。
# また、関数の引数も同様に宣言なしで使用できます。インデントによる文のグルーピングは正しい説明ですが、変数や引数の宣言が必要という部分が誤りとなっています。

# 2 Pythonインタープリタに関する次の記述のうち、誤っているものはどれか。

# スクリプトファイルを走らせた後に対話モードに入るには、スクリプトファイル名の前に「-i」を入れるとよい。
# プライマリプロンプトの記号は「>>>」である。
# セカンダリプロンプトの記号はデフォルトでは「<<<」である。
# インタープリタを対話モードで起動すると、はじめにバージョンと著作権からはじまるメッセージが、その後にプライマリプロンプトが表示される。
# プログラムの冒頭で「# coding: （エンコーディング方式）」のようにすると、デフォルト以外のエンコーディングを使うことも可能である。

# 答え：
# 3番目の選択肢が誤り。
# セカンダリプロンプトの記号はデフォルトでは「...」です。
# 「<<<」ではありません。セカンダリプロンプトは、複数行にまたがる入力を継続する際に表示されます。


# 3

# 【A】～【E】の行にある#から始まる文字列のうち
# Pythonではコメントとして解釈されないものはどれか。

# あいさつ文を表示します。                  # 【A】
x = 'Hello'  # Helloを変数に代入します。    # 【B】
# Worldを変数に                            # 【C】
# 代入します。                             # 【D】
y = 'World!'
# print('{}!{}!! #あいさつ文はここまでです。'.format(x, y))  # 【E】

# 4

a = 10
b = a ** 2
c = b % 20 + 5
d = 8
e = d / b
f = d // c

print ('{0}, {1}'.format(e, f))
# 0.08, 1

# 5

a = "She said,\"He" + 3 * "y" + "!"
b = "How are you?\" "
print (a, b)
# She said,"Heyyy! How are you?"

# 6

Zen = 'NowIsBetterThanNever'
print('{}{}{}{}'.format(Zen[5], Zen[10], Zen[-7], Zen[-3:-1]))
# Brave

# 7

Zen = 'SimpleIsBetterThanComplex'

# print(Zen[:])
# SimpleIsBetterThanComplex

# print(Zen[1000:])
# ''

# print(Zen[5:1000])
# eIsBetterThanComplex

# Zen[0] = 'J'
# TypeError: 'str' object does not support item assignment

# print(Zen[:1000] + 'J')
# SimpleIsBetterThanComplexJ

# 8

a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a+b
# 1,1,2,3,5,8,

# 9

colors = ['red', 'green', 'blue']

colors.append('yellow')
print(colors)
# ['red', 'green', 'blue', 'yellow']
colors.insert(0,'purple')
print(colors)
# ['purple', 'red', 'green', 'blue', 'yellow']

for color in colors[2:]:
    print(color, len(color), end = ', ')
# green 5, blue 4, yellow 6, 

# 10 難しい

# 外側のループ：2から9までの数字を順番にチェック
for n in range(2, 10):
    # 内側のループ：その数が割り切れるかをチェック
    for x in range(2, n):
        # もし割り切れたら（余りが0なら）
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break  # 内側のループを抜ける
    else:
        # 一度も割り切れなかったら、それは素数
        print(n, 'is a prime number')

# 11

# -10から-30まで-5ずつ減少させながら数値を生成するforループ
for i in range(-10, -30, -5):
    print(i, end=", ")
    
# -10, -15, -20, -25, -30, 

# 12

# このコードは、リストの要素とそのインデックスを同時に表示する例です。

# Zenリストを定義し、5つの単語を格納
Zen = ['Now','is','better','than','never']

# range(len(Zen))で0から4までの数値を生成し、
# それぞれの数値をインデックスとしてZenリストの要素にアクセス
for i in range(len(Zen)):
    print(i, Zen[i])  # インデックスと要素を出力

# より簡潔な書き方として、enumerate()関数を使用することもできます:
# for i, v in enumerate(Zen):
#     print(i, v)

# 0 Now
# 1 is
# 2 better
# 3 than
# 4 never

# 13

i = 5
i = 6

def f(arg = i):
    i = 7
    print(arg)

i = 8
i = 9

f()
# 6

# 14

def culc(a, b=1, squares=[], cubes=[]):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes

print(culc(1))
# ([1], [1])

print(culc(2, 3))
# ([1, 4], [1, 27])

print(culc(3, 4))
# ([1, 4, 9], [1, 27, 64])

#15. 次の関数を呼び出す際に、引数の指定として正しいものはどれか。

def location(city, state, country='Japan'):
    print("I live in",country,".")
    print("My company is located in",city,",",state,".")

# location(state='Tokyo', city='chiyoda')
# location(state='California', country='USA', 'San Francisco')
# location(city='Haryono', state='Jakarta', zipcode='12830')
# location('Geelong', city='Melbourne')
# location()

# 16 次のコード1行目のaに入るものとして正しいものはどれか。

# def shop(name, a):
#     print("flowershop:", name)
#     for arg in arguments:
#         print(arg)
#     print("**Recommended**")
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print(kw, ":", keywords[kw])

# shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")

# #実行結果
# flowershop: Iris
# Open: 9:30 am
# Close: 10:30 pm
# Monday and holidays are closed.
# **Recommended**
# bouquet : Sunflower
# dried : Rose
# plants : Pachira


# arguments, keywords
# *keywords, **arguments
# *arguments, **keywords
# **arguments, *keywords
# **keywords, *arguments

# 3種類の引数を受け取ることができる。
# 普通の引数
# *arguments 複数の値をまとめて受け取る
# **keywords 名前を付きの値をまとめて受け取る

# 18 次の結果を得たい場合に、コードの1行目～3行目を代替し同じ結果を出力するものとして正しいものはどれか。

cubes = []
for x in range(5):
    cubes.append(x ** 3)

print(cubes)
# [0, 1, 8, 27, 64]

cubes = [x ** 3 for x in range(5)]
print(cubes)

# 19. 次の実行結果を得たい場合に、コードの【A】に入るものとして正しいものはどれか。

# 実行結果
# [5, 25, 125]

# コード
matrix = [[2, 3, 5], [4, 9, 25], [8, 27, 125]]
power = [row[2] for row in matrix]
print(power)

# 20. 次の実行結果を得たい場合に、コードの【A】と【B】に入るものの組み合わせとして正しいものはどれか。

# 実行結果
# deque(['cow', 'dog', 'elephant', 'fox'])

from collections import deque
queue = deque(["bear", "cow", "dog", "elephant","fox"])
queue.append("goat")
queue.popleft()
queue.pop()
print(queue)

# 21

list = [-10, 1, 15, 20, 30]

# インデックス2の位置(3番目)に5を挿入する
list.insert(2, 5)
# [-10, 1, 5, 15, 20, 30]

# リストの末尾に50を追加する
list.append(50)
# [-10, 1, 5, 15, 20, 30, 50]

# リストを降順(大きい順)にソートする
list.sort(reverse = True)
# [50, 30, 20, 15, 5, 1, -10]

# リストの最後の要素を削除する
list.pop(-1)
# [50, 30, 20, 15, 5, 1]

# 22

# スライスの解説:
# Zen[1:20:3] は以下の意味:
# - 1: 開始位置 (2番目の文字から)
# - 20: 終了位置 (21番目の文字の手前まで) 
# - 3: ステップ幅 (3文字おきに取得)

# 'ExplicitIsBetterThanImplicit' から3文字おきに抽出:
# x(2文字目), i(5文字目), t(8文字目), B(11文字目), t(14文字目), T(17文字目), n(20文字目)

Zen = 'ExplicitIsBetterThanImplicit'
print(Zen[1:20:3])
# xitBtTn

# 23 データ構造に関して

# 24 対話モードでTrueが返されるもの

# タプルの比較
(1, 2, 3, 4) > (1, 2, 5)
# False

# 文字列の比較
'PHP' < 'Perl' < 'Python'
# True

(1, 2) > (1, 2, -1)
# False

# 整数（int）と浮動小数点数（float）を比較する際、数値として等しければ == は True を返します：
(10, 20) != (10.0, 20.0)
# False

(1, 2, ('bb', 'a')) > (1, 2, ('bcd', 'b'))
# False

# 25 モジュールに関して

# 26 モジュールが定義している名前を対話モードで確認したい。次のスクリプトの２行目【A】に入るものとして正しいものはどれか。

import sys
dir(sys)
# dir() 関数は、オブジェクトが持つ有効な属性とメソッドのリストを返します
# sys モジュールに対して dir() を使用すると、そのモジュールで利用可能なすべての名前（属性、メソッド等）を表示します

# mod(systems)
# mod(sys)
# mod()
# dir(mod)
# dir(sys)

# 27

import math
print('{1:.3f}, {0:.5f}'.format(math.pi, math.e))
# 2.718, 3.14159

# {1:.3f} - 1番目の引数（math.e）を小数点以下3桁で表示
# {0:.5f} - 0番目の引数（math.pi）を小数点以下5桁で表示

# 28 難しい

# 29 エラーと例外に関して

# 30 次のスクリプトを実行した場合には適切な方法であるクリーンアップがなされる。具体的にはどのような処理がなされているか。

with open("file.txt") as f:
    for line in f:
        print(line, end="")


# 31 難しい

# 32クラスに関する次の記述のうち、誤っているものはどれか。

# 名前空間とは、名前とオブジェクトの対応付け（マッピング）のことである。名前空間で重要なのは、異なる名前空間同志の名前には一切の関わりがないということである。
# 関数のローカル名前空間は関数がコールされたときに作られ、関数から戻ったり関数内で処理されない例外を送出したりしたとき削除される。
# スコープとは、ある名前空間から直接アクセスできる、プログラムテキスト上の範囲のことである。
# クラスに__init__()メソッドが定義してあると、新規生成されたインスタンスに対して自動的に__init__()メソッドがコールされる。ただし__init__()メソッドに引数を与えることはできない。
# クラスオブジェクトは２種類の操作をサポートする。属性参照とインスタンス化である。クラスのインスタンス化には関数の表記法が使われる。

# 答え：
# 4番目の選択肢が誤り。
# __init__()メソッドには引数を与えることができます。
# 実際、selfパラメータに加えて、必要に応じて任意の数の引数を定義することができます。
# これらの引数は、インスタンス生成時にクラスのコンストラクタに渡すことができます。


# 33 難しい


# 34. コマンドライン上で「python3 script.py one two three four five」を実行したときに、以下の結果を得たい。コード2行目の【A】に入るものとして正しいものはどれか。

# 実行結果
# ['one', 'two', 'three']

# コード
# import sys
# print(【A】)

# sys.args[1:4]
# sys.args[1:3]
# sys.argv[1:4]  # ← 正解
# sys.argv[1:3]
# sys.argv[0:2]

# 答え：
# sys.argv[1:4] が正解です。
# 理由：
# - sys.argv はコマンドライン引数を含むリストです
# - sys.argv[0] はスクリプト名 'script.py' 
# - [1:4] は1番目から3番目までの要素を取得します
# - よって ['one', 'two', 'three'] が得られます


# 35. 難しい

# 次の正規表現を用いたコードの【A】の部分に入れたときエラーとなるものはどれか。

# import re
# prog = re.compile('(K|S)us(a|u)n(a|o)(o|m)?g?i?(saya)?', re.IGNORECASE)
# 【A】
# print(ret[0])


# ret = prog.search('KUSANAGI')
# ret = prog.search('kusunomi')
# ret = prog.search('SUSANOO')
# ret = prog.search('kusanomi')
# ret = prog.search('Kusaneiro')

# 36. 
# statisticsモジュールを使って、データの平均、中央値、分散を求めたい。次のコードの【A】【B】【C】に入りうる組み合わせとして正しいものはどれか。

# import statistics
# data = [1,10,15,20,25,30,35]
# rslt1 = statistics.【A】(data)
# rslt2 = statistics.【B】(data)
# rslt3 = statistics.【C】(data)
# print(rslt1, rslt2, rslt3)


# mean median variance
# mean center scatter
# average middle variance
# balance median scatter
# average median variance

# 37

# 今日の日付を得たい場合、次のコード1行目の【A】に入る適切なものはどれか。

# 【A】
# now = date.today()
# print(now)

# import date
# from datetime import date
# import date from datetime
# from date
# import datetime from date


# 38.

# loggingモジュールのメッセージの優先度として正しいものはどれか。左から順に優先度が高いものとする。

# ERROR、CRITICAL、WARNING、INFO、DEBUG
# ERROR、CRITICAL、WARNING、DEBUG、INFO
# CRITICAL、ERROR、WARNING、DEBUG、INFO
# CRITICAL、ERROR、WARNING、INFO、DEBUG ← 正解
# CRITICAL、WARNING、ERROR、INFO、DEBUG

# 39. 

# 仮想環境とパッケージに関する次の記述のうち誤っているものはどれか。

# Pythonの仮想環境とは、特定バージョンのPythonのインストール実体を含む、独立に機能するディレクトリツリーおよびパッケージなどから成り立つものである。
# 仮想環境をアクティベートしたら、pipを使ってパッケージのインストール、アップグレード、リムーブができる。pipはデフォルトではPython Package Indexからパッケージをインストールする。
# pip install --upgrade とすることで当該パッケージを最新バージョンにアップグレードすることができる。
# pip uninstall にパッケージ名を指定すると、その仮想環境からパッケージを削除できる。削除対象となるパッケージの複数指定はできない。← 誤り
# pip listはその仮想環境にインストールされたすべてのパッケージを表示する。pip freezeも同様の働きをするが、出力形式が異なる。

# 40. 

# 次の記述に関して誤っているものはどれか。

# 変数とモジュールの補完はインタープリタの起動時に自動で有効になっている。← 誤り
# [Tab]キーを押すと補完機能が呼び出せる。この機能はPythonの文（命令）の名前、現在のローカル変数、使用できるモジュール名を検索するものである。
# デフォルト設定ではユーザーディレクトリの「.pyhistory」ファイルにヒストリが保存される。ヒストリは対話型インタープリタセッションで利用できる。
# 拡張された対話型インタープリタとしてbpythonがある。これはタブ補完、オブジェクト探索、高度なヒストリ管理などの機能を持つ。
# bpythonに類似した拡張対話環境にIPythonがある。IPythonは「pip install ipython」でインストールでき、IPythonの対話モードはipythonコマンドで起動できる。