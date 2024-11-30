# 4 

a = 10
b = a ** 2
c = b % 20 + 5
d = 8
e = d / b
print(e) # 0.08
f = d // c
print(f)

print ('{0}, {1}'.format(e, f))

# 5

a = "She said,\"He" + 3 * "y" + "!"
b = "How are you?\" "
print(a, b)

# 15 関数の呼び出す際の引数の指定方法

def location(city, state, country='Japan'):
    print("I live in",country,".")
    print("My company is located in",city,",",state,".")

# # location(state='Tokyo', city='Chiyoda')
# この引数の指定は正しいです。
# キーワード引数を使って、stateとcityのパラメータを指定しています。
# countryは省略可能なデフォルト引数なので、指定しなくてもJapanが使用されます。

# # location(state='California', country='USA', 'San Francisco')
# この引数の指定は正しくありません。
# 位置引数は、キーワード引数の前に指定する必要があります。
# 'San Francisco'は位置引数なので、最初に指定する必要があります。
# 正しい指定方法は以下のようになります:
# location('San Francisco', state='California', country='USA')

# location('Geelong', city='Melbourne')
# この引数の指定は正しくありません。
# 'Geelong'とcity='Melbourne'は同じパラメータ(city)に対する指定となってしまいます。
# 位置引数とキーワード引数で同じパラメータを重複して指定することはできません。
# 正しい指定方法は以下のいずれかになります:
# location('Geelong', state='Victoria')  # 位置引数でcityを、キーワード引数でstateを指定
# location(city='Geelong', state='Victoria')  # 両方キーワード引数で指定

# 34

import sys
print(sys.argv[1:4])

# 36 

# statisticsモジュールを使って、データの平均、中央値、分散を求めたい。
# 次のコードの【A】【B】【C】に入りうる組み合わせとして正しいものはどれか。

import statistics

# データリストの平均値を計算しています
data = [1,10,15,20,25,30,35]
rslt1 = statistics.mean(data)  # statistics.mean()で平均値を計算
print(rslt1)  # 平均値を出力

# データリストの中央値を計算しています
rslt2 = statistics.median(data)  # statistics.median()で中央値を計算
print(rslt2)  # 中央値を出力

# データリストの分散を計算しています
rslt3 = statistics.variance(data)  # statistics.variance()で分散を計算
print(rslt3)  # 分散を出力

# 37

# 今日の日付を得たい場合、次のコード1行目の【A】に入る適切なものはどれか。

from datetime import date
now = date.today()
print(now)

# import date 
# これは誤りです。dateモジュールは存在しません。

# from datetime import date
# これが正解です。
# datetimeモジュールからdateクラスをインポートします。
# これによりdate.today()が使えるようになります。

# import date from datetime
# これは誤りです。
# Pythonのimport文の構文が間違っています。

# from date
# これは誤りです。
# dateモジュールは存在しません。

# import datetime from date
# これは誤りです。
# Pythonのimport文の構文が間違っています。

# 38

# loggingモジュールのメッセージの優先度として正しいものはどれか。
# 左から順に優先度が高いものとする。

# loggingモジュールのメッセージ優先度は以下の順番です（高い順）:

# CRITICAL (50) - 重大なエラー、プログラムが動作できない
# ERROR (40) - エラー、特定の機能が動作できない 
# WARNING (30) - 警告、問題の可能性がある
# INFO (20) - 情報メッセージ
# DEBUG (10) - デバッグ情報

# ERROR、CRITICAL、WARNING、INFO、DEBUG
# ERROR、CRITICAL、WARNING、DEBUG、INFO  
# CRITICAL、ERROR、WARNING、DEBUG、INFO
# CRITICAL、ERROR、WARNING、INFO、DEBUG ← 正解
# CRITICAL、WARNING、ERROR、INFO、DEBUG