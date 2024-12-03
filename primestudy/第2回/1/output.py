# print(5 // 2)
# 切り下げ除算：2

# print(5 % 2)
# 剰余：1

# Zen = 'BeautifulIsBetterThanUgly'

# print(Zen[50])
# インデックス50は存在しないため、IndexErrorが発生します。

# print(Zen[1000:10000])
# スライスは範囲外のインデックスを指定してもエラーを返さず、空の文字列を返します。

# print(Zen[10] = 'a')
# 文字列は不変（immutable）であり、インデックスを使って直接変更することはできません。TypeErrorが発生します。

# monthes = ['January', 'March', 'May', 'July']
# monthes.append('September')

# for month in monthes[:]:
#     if len(month) > 5:
#         monthes.insert(0, month)

# print(monthes, end = '')

# for i in range(-3, -18, -3):
#     print(i, end = ', ')

# -3, -6, -9, -12, -15,

# def culc(a, b, squares=[], cubes=[]):
#     squares.append(a ** 2)
#     cubes.append(b ** 3)
#     return squares, cubes

# print(culc(2,2))
# # ([4], [8])

# print(culc(3,3))
# # ([4, 9], [8, 27])

# print(culc(4, 4))
# # ([4, 9, 16], [8, 27, 64])

# def shop(name, *argsY, **argsX):
#     print("お花屋さんの名前は", name)

#     keys = sorted(argsX.keys())
#     for kw in keys:
#         print(kw, ":", argsX[kw])

#     for Y in argsY:
#         print(Y)

# shop("Iris","開店: 9時","閉店: 10時", b="Sunflower", a="Pachira")

# argsX.keys() argsX の全てのキーを取得
# sorted()     取得したキーをアルファベット順にソート

# お花屋さんの名前は Iris
# a : Pachira
# b : Sunflower
# 開店: 9時
# 閉店: 10時