def dive_into_code(teacher, *mentor):
  print(teacher)

dive_into_code("Noro", "Nakao", "Miyaoka")

# 可変長引数 *mentorに"Nakao", "Miyaoka"が入る

import random
print(random.sample(range(1000), 5))

# ランダムに5つの数字を選ぶ
# 1000までの数字から5つ選ぶ
# 重複しないように選ぶ
# 選んだ5つの数字を返す

for i in range(20):
  if i % 3 == 0:
    print("{}は3で割り切れます".format(i), end=" ")
  elif i > 8 and i % 2 == 0:
    break
  else:
    continue


