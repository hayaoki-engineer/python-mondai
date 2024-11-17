# 例外を送出する

# raise文を使って、例外を送出する
try:
    raise ValueError("これはテスト用の例外です")
except ValueError as error:
    print(error)


# 例外処理のクリーンアップ動作

# try文の後ろには、except文とfinally文がある
# except文は、try文でエラーが発生した場合に実行される
# finally文は、try文でエラーが発生してもしなくても実行される