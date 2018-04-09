first_name = input("Введіть Ваше ім'я: ")
last_name = input("Введіть Ваше прізвище: ")
bal = 0
count = 0
k = ''
quest = open('questions.txt','r')
answ = open(first_name + '_' + last_name + '.txt','w')
print('---------------------------------------------------------------------')
print(first_name + ", дізнайтеся про свій рівень знань з англійської мови, виконавши цей тест. \n"
      "Оберіть із декількох запропонованих варіантів відповідей одну правильну, \n"
      "на Вашу думку, відповідь. Зверніть увагу, що за кожну правильну відповідь \n"
      "Вам нараховується 1 бал, а за неправильну (чи відсутність відповіді) – \n"
      "Ви отримуєте 0 балів. Якщо Ви не знаєте відповіді на питання, тоді просто \n"
      "пропустіть його. Відповідайте швидко, не замислюючись, щоб побачити свій \n"
      "поточний рівень англійської мови. Максимальна кількість балів, які Ви можете \n"
      "набрати – 62. Успіхів! ")
print('---------------------------------------------------------------------')

while True:
    question = quest.readline().strip()
    if (not question):
        break
    answer_a = quest.readline().strip()
    answer_b = quest.readline().strip()
    answer_c = quest.readline().strip()
    kod = quest.readline().strip()
    print(question)
    print('a)', answer_a)
    print('b)', answer_b)
    print('c)', answer_c)
    answ.write(question + '\n')
    answ.write('a)'+ answer_a + '\n')
    answ.write('b)'+ answer_b + '\n')
    answ.write('c)'+ answer_c + '\n')
    k = input("Введіть варіант правильної відповіді (a/b/c) та натисніть 'Enter': \n"
              "Для виходу з програми введіть 'stop': ")
    if k == 'stop':
        break
    while k != 'a' and k != 'b' and k != 'c':
        print("Ви ввели не коректне значення: " + "'" + k + "'")
        k = input("Введіть варіант правильної відповіді (a/b/c) та натисніть 'Enter': ")
    print('---------------------------------------------------------------------')
    answ.write('Ваша відповідь:      '+ k + '\n')
    answ.write('Правильна відповідь: '+ kod + '\n')
    count+=1
    if k == kod:
        bal += 1
        answ.write('Ви отримали 1 бал за цю відповідь! ' + '\n')
        answ.write('---------------------------------------------------------------------' + '\n')
    else:
        answ.write('Ви отримали 0 балів за цю відповідь! ' + '\n')
        answ.write('---------------------------------------------------------------------' + '\n')
print(first_name +', Ви відповіли правильно на  ' + str(bal) +' з '+ str(count) + ' запитань!')
answ.write(first_name +', Ви відповіли правильно на  ' + str(bal) +' з '+ str(count) + ' запитань!\n')
if bal <= 6:
    print('Ваш рівень - Starter!')
    answ.write('Ваш рівень - Starter!\n')
elif 7 <= bal <= 14:
    print('Ваш рівень - Elementary!')
    answ.write('Ваш рівень - Elementary!\n')
elif 15 <= bal <= 28:
    print('Ваш рівень - Pre-Intermediate!')
    answ.write('Ваш рівень - Pre-Intermediate!\n')
elif 29 <= bal <= 45:
    print('Ваш рівень - Intermediate!')
    answ.write('Ваш рівень - Intermediate!\n')
elif 46 <= bal <= 59:
    print('Ваш рівень - Upper-Intermediate!')
    answ.write('Ваш рівень - Upper-Intermediate!\n')
elif 60 <= bal <= 62:
    print('Ваш рівень - Advanced!')
    answ.write('Ваш рівень - Advanced! \n')
print('Результати тесту та правильні відповіді записані в файл: '+ first_name + '_' + last_name + '.txt')
print("До побачення, "+first_name)
quest.close()
answ.close()
