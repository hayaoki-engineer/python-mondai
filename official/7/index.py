# 1


# 2
# モジュールから特定の関数のみをインポートする場合は from モジュール名 import 関数名 を使用します
from calc import add

# 3
from calc import *

# 4

## A
# calendarモジュールをcalという別名でインポートし、2024年のカレンダーを表示します
import calendar as cal
print(cal.calendar(2024))

## B
from calendar import calendar as cal
print(cal(2024))

# C これは間違いです。
# calendarモジュールをcalとしてインポートしているので、
# calendar.cal()ではなく、cal()を使う必要があります。
print(calendar.cal(2024))

## D
# これは冗長な書き方です。
# calendar関数をcalendarという同じ名前でインポートしているため、
# 単にfrom calendar import calendarと書くのと同じです
from calendar import calendar as calendar
print(calendar(2024))

# 5
# このコードは2つの部分から構成されています:

# 1. add関数の定義
# 2つの引数a, bを受け取り、その和を返す単純な関数です
def add(a, b):
    return a + b

# 2. メインブロック
# if __name__ == "__main__": は、このファイルが直接実行された場合にのみ
# 以下のコードブロックを実行するという意味です
# モジュールとしてインポートされた場合は実行されません
if __name__ == "__main__":
    # add関数を1と2を引数として呼び出し、その結果を表示します
    # 結果は3が出力されます
    print(add(1, 2))

# 6

# 7
