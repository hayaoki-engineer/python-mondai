# インポートとは
# 関数などをファイルに記述して、別のファイルからその関数を使用すること
# インポートされるファイルをモジュールという

# calendarモジュールをインポート
import calendar

# インポートしたcalendarモジュールのprmonth関数を使用
calendar.prmonth(2024, 11)

# fromを使ったインポート

# 関数のみをインポート
# from モジュール名 import 関数名
from calendar import prmonth
prmonth(2024, 11)

# ファイルcalc.pyにあるadd()関数をインポート
from calc import add

# ワイルドカードを使ったインポート

# 名前をすべてインポートする
# from モジュール名 import *

# モジュール内の_で始まらない名前が使える

# asを使ったインポート

# モジュールや関数を別名でインポート
# import モジュール名 as 別名

# calendarモジュールを別名calでインポート
import calendar as cal
cal.calendar(2024)

# 関数を別名でインポート
# from モジュール名 import 関数名 as 別名
from calendar import calendar as cal
cal(2024)

# モジュールの属性 __name__

# __name__は、Pythonの特殊な変数で、現在のファイルがどのように実行されているかを示します
# ファイルが直接実行された場合は "__main__" という値になります
# 他のファイルからインポートされた場合は、モジュール名になります

# このif文は、このファイルが直接実行された場合のみ中のコードを実行します
# つまり、他のファイルからインポートされた場合は実行されません
# これにより、テストコードやサンプルコードを書くのに便利です
if __name__ == "__main__":
    print("このファイルが直接実行されたときに実行される")
    



