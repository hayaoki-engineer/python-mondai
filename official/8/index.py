# 1
# ファイルのモード指定について解説します

# 'r' - 読み込み専用モード (デフォルト)
# テキストファイルを読み込むための基本的なモードです
with open('sample.txt', 'r') as f:
    content = f.read()

# 'b' - バイナリモード
# 画像やPDFなどのバイナリファイルを扱う際に使用します
with open('image.png', 'b') as f:
    binary_data = f.read()

# 'wb' - バイナリ書き込みモード
# バイナリデータをファイルに書き込む際に使用します
with open('output.bin', 'wb') as f:
    f.write(b'binary data')

# 'ab' - バイナリ追記モード
# 既存のバイナリファイルの末尾にデータを追加する際に使用します
with open('existing.bin', 'ab') as f:
    f.write(b'additional data')


# 2
fp = open("sample.txt")
s = fp.read()

# 3

# 4 
fp = open("sample.txt")
for s in fp:
    print(s)

# 1行ずつ読み込む別の方法
fp = open("sample.txt")
for s in fp.readlines():
    print(s)

fp = open("sample.txt")
for s in list(fp):
    print(s)

# 5
fp = open("sample.txt", "w")
fp.write("こんにちは、世界！\n")  # ファイルに文字列を書き込む
fp.close()

# 6
import json
data = [{"id": 1}, {"id": 2}]
fp = open("sample.json", "w")
json.dump(data, fp)
fp.close()

# 7
import json
fp = open("sample.json")
s = json.load(fp)