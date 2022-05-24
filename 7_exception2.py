"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
"""
   
def discounted(price, discount, max_discount=20):
  try:
    price = float(price)
    discount = float(discount)
    max_discount = int(max_discount)
  except(ValueError):
    print(f' {"Некорректно заданы"} {price} {"и"} {discount}')
    return 0
  if max_discount >= 100:
    raise ValueError("Слишком большая максимальная скидка")
  if discount >= max_discount:
    return price
  else:
    return price - (price * discount / 100)
    

data = [
  [100, 2],
  [100, "3"],
  ["100", "4.5"],
  ["five", 5],
  ["сто", "десять"],
  [100.0, 5, "10"]
]
if __name__ == "__main__":
  for p in data:
    t = discounted(p[0], p[1])
    if (t):
      print(t) 

