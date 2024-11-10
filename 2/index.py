# 3
text = """spam
ham
eggs
"""

print(text) 

# 7
# f-stringを使用した数値フォーマット
# price:7d は整数を7文字分の幅で右寄せで表示

price = 15000
print(f"価格：{price:7d}")

# => 価格：  15000

# 8
#f-stringを使用して、.5fで小数点以下5桁まで表示するようにフォーマット

import math
print(f"πの値はおよそ{math.pi:.5f}です")