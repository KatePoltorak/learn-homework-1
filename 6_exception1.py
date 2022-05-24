"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
  try:
    while True:
      answer_how_are_you = input("Как дела? ")
      if answer_how_are_you == "Хорошо":
        break
  except (KeyboardInterrupt):
    print(" Пока")
  

if __name__ == "__main__":
    hello_user()
 
