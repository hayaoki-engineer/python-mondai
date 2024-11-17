# 1. Pythonの特徴に関する次の記述のうち、誤っているものはどれか。


# Pythonはインタープリタ言語であり、コンパイル等が必要でないため、プログラム開発における時間を節約してくれる。インタープリタは対話的に使うことも可能である。
# PythonはWindows、MacOS、Linuxなど多くの環境で動作する。
# Pythonでは、文のグルーピングはカッコで囲うことでなくインデントで行われるなど、プログラムを小さく読みやすく書けるという特徴がある。ただ変数や引数の宣言は必要である。
# Pythonはフリーのオープンソースソフトウェアである。
# Pythonは機械学習やディープラーニング、データ解析、Webアプリケーションなど多くの分野を得意としている。

# 2. Pythonインタープリタに関する次の記述のうち、誤っているものはどれか。


# スクリプトファイルを走らせた後に対話モードに入るには、スクリプトファイル名の前に「-i」を入れるとよい。
# プライマリプロンプトの記号は「>>>」である。
# セカンダリプロンプトの記号はデフォルトでは「<<<」である。
# インタープリタを対話モードで起動すると、はじめにバージョンと著作権からはじまるメッセージが、その後にプライマリプロンプトが表示される。
# プログラムの冒頭で「# coding: （エンコーディング方式）」のようにすると、デフォルト以外のエンコーディングを使うことも可能である。

# 3 【A】～【E】の行にある#から始まる文字列のうちPythonではコメントとして解釈されないものはどれか。

# あいさつ文を表示します。　…【A】
x = 'Hello' # Helloを変数に代入します。　…【B】
# Worldを変数に　…【C】
               # 代入します。　…【D】
y = 'World !'　
print ('{}!{}!! #あいさつ文はここまでです。'.format(x, y)) 　…【E】


# 4. 次のコードの実行結果として正しいものはどれか。

a = 10
b = a ** 2
c = b % 20 + 5
d = 8
e = d / b
f = d // c
print ('{0}, {1}'.format(e, f))

# 0.8, 0
# 0.08, 1
# 0.08, 0
# 0, 1.6
# 0, 0.8

# 5. 次のコードの実行結果はどれか。なおコードの\はバックスラッシュに読み替えること。

a = "She said,\"He" + 3 * "y" + "!"
b = "How are you?\" "
print (a, b)

# 6. 次のコードの実行結果として正しいものはどれか。

Zen = 'NowIsBetterThanNever'
print('{}{}{}{}'.format(Zen[5], Zen[10], Zen[-7], Zen[-3:-1]))

# 7. 次の変数Zenに関して指定した場合、実行時にエラーとなるものはどれか。

Zen = 'SimpleIsBetterThanComplex'


# Zen[:]
# Zen[1000:]
# Zen[5:1000]
# Zen[0] = 'J'
# Zen[:1000] + 'J'

# 8. 次のコードの実行結果として正しいものはどれか。

a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a+b

# 9. 次のコードの実行結果として正しいものはどれか。

colors = ['red', 'green', 'blue']
colors.append('yellow')
colors.insert(0,'purple')
for color in colors[2:]:
    print(color, len(color), end = ', ')


# 10. 次のような結果を得たい場合、コードの【A】の行に入る適切なものはどれか。なお【A】に入るものは、★aの行と同じ数の空白でインデントされている。

# 実行結果
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2

# コード
for n in range(2, 10):
    for x in range(2 ,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    # 【A】
        print(n,'is a prime number')

        continue
    break

# 11. 次のコードの実行結果として正しいものはどれか。

for i in range(-10, -30, -5):
    print(i, end=", ")

# 12. 次の結果を得たい場合、コードの2行目以降を代替するものとして正しいものはどれか。なお各選択肢の次の行には「 print(i, v) 」が記述されるものとする。

# 実行結果
# 0 Now
# 1 is
# 2 better
# 3 than
# 4 never

# コード
Zen = ['Now','is','better','than','never']
for i in range(len(Zen)):
    print(i, Zen[i])


# for i ,v in count(Zen):
# for i ,v in enumerate(Zen):
# in i ,v for calculate(Zen):
# in i ,v for number(Zen):
# for i ,v in list(Zen):
    
# 13. 次のコードの実行結果として正しいものはどれか。

i = 5
i = 6

def f(arg = i):
    i = 7
    print(arg)

i = 8
i = 9

f()

# 14. 次のコードに関し、【A】の行の出力として正しいものはどれか。

# コード
def culc(a, b=1, squares=[], cubes=[]):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes

print(culc(1))
print(culc(2, 3))
print(culc(3, 4)) # 【A】
print(culc(4, 5))

# 15. 次の関数を呼び出す際に、引数の指定として正しいものはどれか。

def location(city, state, country='Japan'):
    print("I live in",country,".")
    print("My company is located in",city,",",state,".")

# location(state='Tokyo', city='chiyoda')
# location(state='California', country='USA', 'San Francisco')
# location(city='Haryono', state='Jakarta', zipcode='12830')
# location('Geelong', city='Melbourne')
# location()

# 16. 次のコード1行目の【A】に入るものとして正しいものはどれか。

# コード
def shop(name, a):
    print("flowershop:", name)
    for arg in arguments:
        print(arg)
    print("**Recommended**")
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")

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

# 17. 次の記述のうち、正しいものはどれか。

# docstringの1行目では、オブジェクトの目的を丁寧に記述し、母国語の異なるエンジニアが読んだ場合にも誤解が生じないようあえて冗長に説明するべきである。
# docstringはコンパクトにまとめ、空行は避けるべきである。
# コメント行は独立させず、該当コードについての説明であることが明示されるよう、同じ行に記述すべきである。
# 演算子の周囲やカンマの後ろ、カッコの内側にもスペースを入れ読みやすさに配慮すべきである。
# 国際的な環境で使用する予定のコードでは、PythonのデフォルトであるUTF-8か、さらにプレーンなASCIIが常に最良である。

# 18. 次の結果を得たい場合に、コードの1行目～3行目を代替し同じ結果を出力するものとして正しいものはどれか。

# 実行結果
# [0, 1, 8, 27, 64]

#コード
cubes = []
for x in range(5):
    cubes.append(x ** 3)

print(cubes)

# cubes = [x ** 3 for range(5) in x]
# cubes = [x ** 3 for x in range(5)]
# cubes = [x in range(5) for x ** 3]
# cubes = [x in x ** 3 for range(5)]
# cubes = [x for x ** 3 in range(5)]

# 19. 次の実行結果を得たい場合に、コードの【A】に入るものとして正しいものはどれか。

# 実行結果
# [5, 25, 125]

# コード
# matrix = 【A】
power = [row[2] for row in matrix]
print(power)


# [[2, 3, 5], [4, 9, 25], [8, 27, 125]]
# [[2, 4, 8], [3, 9, 27], [5, 25, 125]]
# [[2, 4, 8], [5, 25, 125], [3, 9, 27]]
# [[5, 3, 2], [25, 9, 4], [125, 27, 8]]
# [[0, 5], [1, 25], [2, 125]]

# 20. 次の実行結果を得たい場合に、コードの【A】と【B】に入るものの組み合わせとして正しいものはどれか。

# 実行結果
# deque(['cow', 'dog', 'elephant', 'fox'])

# コード
# from 【A】 import deque
# queue = deque(["bear", "cow", "dog", "elephant","fox"])
# queue.append("goat")
# 【B】
# queue.pop()
# print(queue)

# 【A】collections　【B】queue.popleft()
# 【A】collections　【B】queue.pop(1)
# 【A】collection　【B】queue.removeleft("bear")
# 【A】collection　【B】queue.delete()
# 【A】collectitems　【B】queue.pop("bear")

21. 
次のコードの実行結果として正しいものはどれか。

list = [-10, 1, 15, 20, 30]
list.insert(2,5)
list.append(50)
list.sort(reverse = True)
list.pop(-1)
print(list)

22. 
次のコードの実行結果として正しいものはどれか。

Zen = 'ExplicitIsBetterThanImplicit'
print(Zen[1:20:3])


23. 
データ構造に関する次の記述のうち誤っているものはどれか。


タプルは変更不能（immutable）、リストと集合は変更可能（mutable）である。

ディクショナリは変更不能（immutable）であるがキーの型は変更可能（mutable）であり、その値は一意でなければならない。

ディクショナリは、全要素が「キー」と「値」のペアであるという点で、リストやタプルと大きく異なる。

集合には、「順序を持たない」「同一の値の要素を重複して持つことができない」などの特徴がある。

リスト、タプル、集合、ディクショナリには、反復可能（iterable）であるという共通点がある。

24. 
次のうち対話モードで入力したときに「True」が返されるのはどれか。


(1, 2, 3, 4) > (1, 2, 5)

'PHP' < 'Perl' < 'Python'

(1, 2) > (1, 2, -1)

(10, 20) != (10.0, 20.0)

(1, 2, ('bb', 'a')) > (1, 2, ('bcd', 'b'))

25. 
モジュールに関する次の記述のうち、誤っているものはどれか。


モジュールとは、Pythonの定義や文が入ったファイルである。そのファイル名は、モジュール名に接尾辞「.py」を付けたものである。

あるモジュールがインポートされるときにインタープリタが検索する順序は、まずビルトインモジュール、次にsys.path変数で得られるディレクトリ、最後にシンボリックリンクを置いてあるディレクトリである。

sys.pathが初期化されている場所は、入力スクリプトのあるディレクトリ、PYTHONPATH、インストールごとのデフォルトである。

モジュール読み込みの高速化のため、Pythonはコンパイル済みのモジュールを「__pycache__」ディレクトリに、例えば「module.バージョン名.pyc」のような名前でキャッシュする。

Pythonには標準モジュールのライブラリが付属する。

26. 
モジュールが定義している名前を対話モードで確認したい。次のスクリプトの２行目【A】に入るものとして正しいものはどれか。

import sys
【A】


mod(systems)

mod(sys)

mod()

dir(mod)

dir(sys)

27. 
次のコードの実行結果として正しいものはどれか。

import math
print('{1:.3f}, {0:.5f}'.format(math.pi, math.e))


28. 
次のコードを実行して「整数a:」に「5」、「整数b:」に「0」を入力した場合の正しい結果はどれか。なお選択肢中の「, 」は改行に読み替えること。

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


25, C, F, G

25, 0, C, G

25, D, G

25, D, F, G

25, 0, D, F, G

29. 
エラーと例外に関する次の記述のうち誤っているものはどれか。


Pythonのエラーには２つの種類がある。構文エラーと例外である。構文エラーはパース上のエラーとも呼ばれる。

文や式が構文的に正しくても、実行しようとするときにエラーが生じることがある。実行中に検知されるエラーは例外と呼ばれ、これは必ずしも致命的なものではない。

例外のほとんどはプログラムでは処理されず、その結果はエラーメッセージに現れる。エラーメッセージの最終行には、NameError、TypeErrorなど例外の型が記されている。

[Ctrl]+[C]キーなどでユーザーがプログラムに割り込みをかけると、KeyboardInterrupt例外が送出される。

パーサ（構文解釈器）は違反のある行を表示し、最後にエラーが検知された点を小さな矢印で示す。エラーは矢印より後のトークンが原因である。

30. 
次のスクリプトを実行した場合には適切な方法であるクリーンアップがなされる。具体的にはどのような処理がなされているか。

with open("file.txt") as f:
    for line in f:
        print(line, end="")


f.clean()

f.close()

file.clean()

close("file.txt")

file.close()

31. 
次の実行結果を得たい場合、コードの【A】【B】に入る組み合わせとして適切なものはどれか。

[ 実行結果 ]
Saya is a
intelligent
speedster.

[コード]
class OurException(Exception):
    pass
def raise_her_exception(a):
    print(a, 'is a')
    raise 【A】
    print('easygoing person.')
def func(key: int):
    try:
        if key == 0:
            raise_her_exception('Saya')
    except OurException as e:
        print('intelligent')
        raise 【B】

key = 0
try:
    func(key)
except Exception as f:
    print('speedster.')


【A】OurException　【B】Exception

【A】Exception　【B】OurException

【A】Exception　【B】raise_her_exception

【A】何も入らない　【B】Exception

【A】何も入らない　【B】何も入らない

32. 
クラスに関する次の記述のうち、誤っているものはどれか。


名前空間とは、名前とオブジェクトの対応付け（マッピング）のことである。名前空間で重要なのは、異なる名前空間同志の名前には一切の関わりがないということである。

関数のローカル名前空間は関数がコールされたときに作られ、関数から戻ったり関数内で処理されない例外を送出したりしたとき削除される。

スコープとは、ある名前空間から直接アクセスできる、プログラムテキスト上の範囲のことである。

クラスに__init__()メソッドが定義してあると、新規生成されたインスタンスに対して自動的に__init__()メソッドがコールされる。ただし__init__()メソッドに引数を与えることはできない。

クラスオブジェクトは２種類の操作をサポートする。属性参照とインスタンス化である。クラスのインスタンス化には関数の表記法が使われる。

33. 
次の実行結果を得たい場合、コードの【A】【B】の行に入る組み合わせとして適切なものはどれか。なお【A】は★aの行と、【B】は★bの行と同じ数の空白でインデントされている。

[ 実行結果 ]
I'm Saya.
I'm Magatama.
I'm David.

[ コード ]
class kusanagi():
    def s(self):
        print("I'm Saya.")　 …★a　
        【A】
    def m(self): 　 …★b
        print("I'm Magatama.")

class onimaru(kusanagi):
    【B】
        print("I'm David.")

k = kusanagi()
o = onimaru()
k.s()
o.d()


【A】self(m):　【B】self(d)

【A】self(m):　【B】def d(self):

【A】self(m)　【B】self.d()

【A】self.m()　【B】def d(self):

【A】self.m()　【B】self.d()

34. 
コマンドライン上で「python3 script.py one two three four five」を実行したときに、以下の結果を得たい。コード2行目の【A】に入るものとして正しいものはどれか。

[ 実行結果 ]
['one', 'two', 'three']

[ コード ]
import sys
print(【A】)


sys.args[1:4]

sys.args[1:3]

sys.argv[1:4]

sys.argv[1:3]

sys.argv[0:2]

35. 
次の正規表現を用いたコードの【A】の部分に入れたときエラーとなるものはどれか。

import re
prog = re.compile('(K|S)us(a|u)n(a|o)(o|m)?g?i?(saya)?', re.IGNORECASE)
【A】
print(ret[0])


ret = prog.search('KUSANAGI')

ret = prog.search('kusunomi')

ret = prog.search('SUSANOO')

ret = prog.search('kusanomi')

ret = prog.search('Kusaneiro')

36. 
statisticsモジュールを使って、データの平均、中央値、分散を求めたい。次のコードの【A】【B】【C】に入りうる組み合わせとして正しいものはどれか。

import statistics
data = [1,10,15,20,25,30,35]
rslt1 = statistics.【A】(data)
rslt2 = statistics.【B】(data)
rslt3 = statistics.【C】(data)
print(rslt1, rslt2, rslt3)


mean median variance

mean center scatter

average middle variance

balance median scatter

average median variance

37. 
今日の日付を得たい場合、次のコード1行目の【A】に入る適切なものはどれか。

【A】
now = date.today()
print(now)


import date

from datetime import date

import date from datetime

from date

import datetime from date

38. 
loggingモジュールのメッセージの優先度として正しいものはどれか。左から順に優先度が高いものとする。


ERROR、CRITICAL、WARNING、INFO、DEBUG

ERROR、CRITICAL、WARNING、DEBUG、INFO

CRITICAL、ERROR、WARNING、DEBUG、INFO

CRITICAL、ERROR、WARNING、INFO、DEBUG

CRITICAL、WARNING、ERROR、INFO、DEBUG

39. 
仮想環境とパッケージに関する次の記述のうち誤っているものはどれか。


Pythonの仮想環境とは、特定バージョンのPythonのインストール実体を含む、独立に機能するディレクトリツリーおよびパッケージなどから成り立つものである。

仮想環境をアクティベートしたら、pipを使ってパッケージのインストール、アップグレード、リムーブができる。pipはデフォルトではPython Package Indexからパッケージをインストールする。

pip install --upgrade とすることで当該パッケージを最新バージョンにアップグレードすることができる。

pip uninstall にパッケージ名を指定すると、その仮想環境からパッケージを削除できる。削除対象となるパッケージの複数指定はできない。

pip listはその仮想環境にインストールされたすべてのパッケージを表示する。pip freezeも同様の働きをするが、出力形式が異なる。

40. 
次の記述に関して誤っているものはどれか。


変数とモジュールの補完はインタープリタの起動時に自動で有効になっている。

[Tab]キーを押すと補完機能が呼び出せる。この機能はPythonの文（命令）の名前、現在のローカル変数、使用できるモジュール名を検索するものである。

デフォルト設定ではユーザーディレクトリの「.pyhistory」ファイルにヒストリが保存される。ヒストリは対話型インタープリタセッションで利用できる。

拡張された対話型インタープリタとしてbpythonがある。これはタブ補完、オブジェクト探索、高度なヒストリ管理などの機能を持つ。

bpythonに類似した拡張対話環境にIPythonがある。IPythonは「pip install ipython」でインストールでき、IPythonの対話モードはipythonコマンドで起動できる。