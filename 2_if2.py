"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
* 1. "Привет" 7
* 2. "Привет" "Привет" 
* 3. "Привет" "Пока"
* 4. "Пока" "learn"
* 5. "Пока" "Привет"
ЗАДАНИЕ НЕКОРРЕКТНО: что делать если строки разные, первая длиннее, а вторая "learn"?
что делать если строки разные, вторая длиннее? + добавила четвертое условие, в котором вторая строка длиннее
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    text1 = "Пока"
    text2 = "Привет"
    print(check_answer(text1, text2))

def check_answer (text1 , text2):
  if type(text1) != str or type(text2) != str :
    return 0 
  elif text1 == text2:
    return 1
  if len(text1) > len(text2):
    return 2
  elif text2 == "learn":
    return 3
  else:
    return 4


if __name__ == "__main__":
    main()


