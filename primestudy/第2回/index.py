# 3

# 数値に関する次の記述のうち、正しいものはどれか。

# 自分の答え
# 演算を行うための「 + 」や「 - 」などの記号はオペランドと呼ばれ、演算の対象は演算子と呼ばれる。
# 演算の対象はオペランドである。

# 正解
# 整数はintという型を持つ。小数点を伴う数はfloatという型を持つ。除算は常にfloatを返す。
# 除算 5 / 2 = 2.5 ← floatを返す

# 切り下げ除算を行って整数解を得たい場合（剰余を捨てたい場合）は「 / 」を使い、剰余のみ得たい場合は「 // 」を使う。
# 切り下げ除算 5 // 2 = 2 ← 「/」ではない
# 剰余        5 % 2 = 1 ← 「//」ではない

# 正解
# 変数は、定義（値の代入）や宣言がなされないまま使おうとするとエラーとなる。

# 対話モードでは、最後に表示した式を変数「**」（アスタリスク2つ）に代入してある。
# 最後の評価結果は _ という変数に格納されるので、「**」（アスタリスク2つ）に代入は誤り。

# 7

# 次の変数Zenに関して指定した場合、実行時にエラーとならないものはどれか。

# Zen = 'BeautifulIsBetterThanUgly'

# 自分の答え
# Zen[50]
# Zenの文字列は26文字であり、インデックス50は存在しないため、IndexErrorが発生します。

# 正解
# Zen[1000:10000]
# スライスは範囲外のインデックスを指定してもエラーを返さず、空の文字列を返します。

# Zen[10] = 'a'
#文字列は不変（immutable）であり、インデックスを使って直接変更することはできません。TypeErrorが発生します。

# Zen['B']
# 文字列のインデックスには整数を使用する必要があり、文字列をインデックスとして指定するとTypeErrorが発生します。

# Zen[1:10] + b
# bが定義されていない場合、NameErrorが発生します。もしbが定義されている場合は、Zen[1:10]の部分は正常に動作しますが、bの値によって結果が変わります。


# 8

# 次のコードの実行結果として正しいものはどれか。

# a, b = 0, 1
# while a < 10:
#     print(a, end=',')
#     a, b = b, a+b


# 9

# 次のコードの実行結果として正しいものはどれか。

# months = ['January', 'March', 'May', 'July']
# months.append('September')
# => ['January', 'March', 'May', 'July', 'September']

# for month in months[:]:
#     if len(month) > 5:
#         months.insert(0,month)

# print(months, end = '')

# 自分の答え
# ['March', 'January', 'January', 'March', 'May', 'July']

# 正解
# ['September', 'January', 'January', 'March', 'May', 'July', 'September']

# 解説
# 条件チェック: 各月の名前の長さが5より大きいかを確認します。
# 'January'（7文字）と 'September'（9文字）は条件を満たす
# 挿入操作: insert(0, month)を使って、条件を満たす月をリストの先頭に追加します。
# 'January'と'September'がそれぞれ挿入される


# 11

# for i in range(-3, -18, -3):
#     print(i, end=", ")

# 自分の答え
# -6, -9, -12, -15,

# 正解
# -3, -6, -9, -12, -15,


# 14

# 次のコードに関し、【A】の行の出力として正しいものはどれか。

# def culc(a, b, squares=[], cubes=[]):
#     squares.append(a ** 2)
#     cubes.append(b ** 3)
#     return squares, cubes

# print(culc(2,2))
# => ([4], [8])

# print(culc(3,3))
# => ([4, 9], [8, 27])

# print(culc(4,4)) 【A】
# => ([4, 9, 16], [8, 27, 64])

# print(culc(5,5))


# 16

# 次のコード1行目の【A】【B】に入る組み合わせとして正しいものはどれか。

# [ コード ]
# def shop(name,【A】, 【B】):
#     print("flowershop:", name)
#     keys = sorted(argsX.keys())
#     for kw in keys:
#         print(kw, ":", argsX[kw])
#     for Y in argsY:
#         print(Y)

# shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")

# 自分の答え
# *argsX, **argsY

# 正解


# 17

# 次の記述のうち、誤っているものはどれか。


# 関数注釈（アノテーション）は関数の__annotations__属性にディクショナリとして格納され、関数のほかの部分にはいかなる影響も及ぼさない。

# 例えば「def func(a: int, b:str) -> value」と関数を記述したときにアノテーションに該当するものは「-> value」のみである。

# docstringの1行目は、常にオブジェクトの目的の短く簡潔な要約を記述し、大文字で始まりピリオドで終わる行とすべきである。

# docstringに2行目以降がある場合、2行目は空行としてようやくと他の記述を視覚的に分離すべきである。

# PEP 8では、演算子の周囲やカンマの後ろにはスペースを入れるが、カッコのすぐ内側にはスペースを入れるべきではないとされる。