# 1
# このコードには2つのエラーがあります:

# 1. SyntaxError: EOL while scanning string literal
# 文字列の終わりのクォートがないため、構文エラーが発生します

# 2. 仮に文字列が正しく "1,000" と定義されていたとしても:
# ValueError: invalid literal for int() with base 10: '1,000'
# カンマを含む文字列は整数に変換できないためエラーになります

a = "1,000'  # 構文エラー
print(int(a))  # 実行されません

# 2

# 3
# このコードは例外処理の基本的な使い方を示しています:

# try: 
#   例外が発生する可能性のあるコードを記述します
# except:
#   例外が発生した場合の処理を記述します

# raise文で意図的にValueErrorを発生させています
# as句を使って例外オブジェクトをerror変数に代入し、
# そのエラーメッセージを表示しています

try: 
  raise ValueError("ValueErrorです")
except ValueError as error:
  print(error)

# 4
# このコードは例外処理の様々なパターンを示しています:

# 1. try-except-finally文の基本構造
#   - try: 例外が発生する可能性のあるコード
#   - except: 例外発生時の処理
#   - finally: 例外の有無に関わらず必ず実行される処理

# 2. 複数のexcept節
#   - ZeroDivisionError: ゼロによる除算時の例外
#   - TypeError: 型の不一致による例外

# 3. 実行の流れ
#   - number/dividerで除算を試みる
#   - dividerが"0"(文字列)なのでTypeError発生
#   - "引数の型が不正です"を表示
#   - finally節を実行
#   - answerはNoneとなる理由:
#     - except節でreturn文がないため
#     - TypeErrorが発生した時点でtry節のreturnは実行されない
#     - 関数は暗黙的にNoneを返す

def divide(number, divider):
  try:
    return number / divider
  except ZeroDivisionError:
    print("ゼロ除算が行われた")
  except TypeError:
    print("引数の型が不正です")
  finally:
    print("-- finally節の処理 --")

answer = divide(100, "0")
print(f"結果: {answer}")