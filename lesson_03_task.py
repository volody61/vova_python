# #Только Питон!
# Напишите программу, которая считывает одну строку.
# Если это строка «Python», программа выводит «ДА»;
# в противном случае программа выводит «НЕТ».

# slovo = input()
# if slovo == ('python'):
#     print('ДА')
# else:
#     print('НЕТ')

# # Да или нет?!
# Напишите программу, которая считывает две строки и выводит «ВЕРНО»,
# если в каждой из них записано или слово только да, или только слово нет (в любой комбинации).
# Если это не так, выведите «НЕВЕРНО».

# a = input()
# b = input()
# if a == b:
#     print('ВЕРНО')
# else:
#     print('НЕВЕРНО')


# # Ёлочка, гори!
# Напишите программу, которая считывает три строки.
# Если эти три строки – «раз», «два» и «три», то программа выводит «ГОРИ»,
# если нет, то «НЕ ГОРИ».

# ch1 = input()
# ch2 = input()
# ch3 = input()
# if ch1 == ('раз') and ch2 == ('два') and ch3 == ('три'):
#     print('гори')
# else:
#     print('не гори')
    # if ch2 == ('два'):
    #     if ch3 == ('три'):
    #         print('гори')
#         else:
#             print('не гори')
#     else:
#         print('не гори')
# else:
#     print('не гори')

# # # Ёлочка-2
# Усовершенствуйте предыдущую программу так, чтобы не только при вводе «раз», «два», «три»,
# но и при вводе «1», «2» и «3» тоже выводилось «ГОРИ».
# Смешанный ввод (например, «1», «2», «три») даёт «НЕ ГОРИ».

# ch1 = input()
# ch2 = input()
# ch3 = input()
# if ch1 == ('раз') or ('1') and ch2 == ('два') or ('2') and ch3 == ('три') or ('3'):
#     print('гори')
# else:
#     print('не гори')
# ch1 = input()
# ch2 = input()
# ch3 = input()
# if ch1 == ('раз') or ('1'):
#     if ch2 == ('два') or ('2'):
#         if ch3 == ('три') or ('3'):
#             print('гори')
#         else:
#             print('не гори')
#     else:
#         print('не гори')
# else:
#     print('не гори')

# # Ёлочка-3
# Добавьте в предыдущую программу возможность вместо «раз» ввести «один».
# word_1 = input()
# word_2 = input()
# word_3 = input()

# ch1 = input()
# ch2 = input()
# ch3 = input()
# if ch1 == ('раз') or ('1') or ('один') \
#         and ch2 == ('два') or ('2') \
#         and ch3 == ('три') or ('3'):
#     print('гори')
# else:
#     print('не гори')
# ch1 = input()
# ch2 = input()
# ch3 = input()
# if ch1 == ('раз') or ('1') or ('один'):
#     if ch2 == ('два') or ('2'):
#         if ch3 == ('три') or ('3'):
#             print('гори')
#         else:
#             print('не гори')
#     else:
#         print('не гори')
# else:
#     print('не гори')

# Регистрация почты
# При регистрации нового ящика электронной почты пользователя обычно просят ввести, помимо прочего, желаемый
# логин, а также резервный адрес электронной почты (на случай, если понадобится восстановить забытый пароль).
# Напишите программу, которая проверяет, что пользователь ничего не перепутал и ввёл корректный логин
# (не содержащий символ «@») и корректный резервный адрес (содержащий символ «@»). Иных проверок,
# кроме указанных здесь, выполнять не надо.
# Формат ввода
# Вводятся две строки: предлагаемые пользователем логин и резервный адрес.
# Формат вывода
# Выводится одна строка: если все условия выполнены, то выводится «OK» (латиницей); если в логине присутствует
# «@», то выводится «Некорректный логин»; если логин корректный, но в адресе отсутствует «@», то выводится
# «Некорректный адрес».

# login = input()
# adress = input()
# if login.find('@') == -1:
#     if adress.find('@') >= 0:
#         print('ОК')
# if login.find('@') >= 0:
#     print('неверный логин')
# if adress.find('@') == -1:\
#     print('неверный адрес')



# # длина
# Напишите программу, которая считывает с клавиатуры строку и выводит фразу:
# «Слово [введённая строка] имеет длину [длина введённой строки]».

# word = input()
# print('слово', word, 'имеет длину', len(word))
# print(f'слово {word} имеет длину {len(word)}')

# # Каникулы капризного ребенка
# Непросто приходится родителям капризной девочки Жени.
# Прошлым летом в июле она побывала в Туле, а в августе — в Пензе, и ей очень понравилось.
# Поэтому этим летом она снова хочет съездить в два различных города.
# При этом Женя хочет снова побывать в июле в Туле или в августе в Пензе,
# но не то и другое одновременно — повторять прошлогодний маршрут полностью ей будет скучно.
# Определите, подходит ли предлагаемый маршрут под требования Жени.
# Формат ввода
# Вводятся две строки — названия городов, в которые родители собираются отправиться с
# Женей в июле и в августе.
# Формат вывода
# Выводится «ДА», если предложенная последовательность городов удовлетворяет
# требованиям Жени, и «НЕТ», если не удовлетворяет.

# ДА
# Москва Пенза
# Тула Москва

# НЕТ
# Тула Тула
# Пенза Пенза
# Москва Тула
# Пенза Москва
# Москва Омск

# gor1 = input()
# gor2 = input()
# if gor1 == ('тула') and gor2 != ('пенза') or gor1 != ('тула') and gor2 == ('пенза'):
#     if gor1 != gor2 :
#         print ('да')
#     else:
#         print('нет')
# else:
#     print ('нет')

# # сложить два числа
# Напишите программу, которая считывает с клавиатуры одно за другим два целых числа
# и выводит их сумму.

# a = int(input())
# b = int(input())
# print(a + b)

# # сложить еще два числа
# Напишите программу, которая считывает с клавиатуры одно за другим два дробных
# числа и выводит их сумму.

# a = float(input())
# b = float(input())
# print(a + b)



# # Телеграммы
# Сейчас каждый второй житель земли в возрасте от 12 до 64 лет использует мессенджеры.
# Мы иногда даже не задумываемся, что и кому мы пишем. Переписка с родителями,
# чаты с друзьями - все это происходит мгновенно и всегда доступно, конечно,
# если у вас не сел телефон. А во времена ваших бабушек и дедушек все было совсем по-другому.
# Для того чтобы быстро сообщить какую-то новость, надо было идти на почту и отправлять
# телеграмму. Телеграфный аппарат посимвольно передавал ваше сообщение на другой узел связи,
# из-за этого плата производилась за каждый знак отдельно. Именно поэтому в старых
# телеграммах очень часто не ставили знаки препинания.
# А теперь представьте на мгновение, что каждый напечатанный вами символ (в том числе и пробел)
# стоит 40 коп. и посчитайте, сколько бы вы тратили на повседневную переписку.

# text = input()
# summa = len(text) * 40
# print('стоимость', summa // 100, 'рублей', summa % 100, 'копеек')

# Плюс-минус
# Напишите программу, которая считывает с клавиатуры одно дробное число,
# после чего выводит «+», «-» или «0», если это число – положительное,
# отрицательное или ноль, соответственно.

# a = float(input())
# if a < 0:
#     print('-')
# elif a == 0:
#     print('0')
# elif a > 0:
#     print('+')

# # Собери число
# Вася испугался, что Петя подсмотрит все его пароли в записной книжке, и решил их зашифровать.
# Для этого он берет изначальный пароль – трехзначное число – и по нему строит новое число
# по следующим правилам:
# Находится сумма цифр, стоящих в двух старших разрядах (сотни и десятки)
# Находится сумма цифр, стоящих в двух младших разрядах (десятки и единицы)
# Эти две суммы, записанные друг за другом, в порядке не возрастания, формируют новое число.
# Например, было введено число 167. Строим сумму старших разрядов – 1 + 6 = 7,
# строим сумму младших разрядов – 6 + 7 = 13.
# Полученные две суммы 7 и 13 записываем друг за другом в порядке не возрастания, те 137.
# Искомое число – 137.

# shifr = int(input())
# c1 = (shifr // 100 + (shifr // 10) % 10)
# c2 = ((shifr // 10) % 10 + shifr % 10)
# if c1 >= c2:
#     print(c1, c2, sep='')
# if c2 >= c1:
#     print(c2, c1, sep='')

# На раз-два-три, рассчитайсь!
# Боря, Вова и Дима спорят, кто из них выше и в каком порядке они должны стоять в шеренге
# на уроке физкультуры. Напишите программу, которая упорядочивает рост мальчиков по невозрастанию.

# r1 = int(input('рост бори'))
# r2 = int(input('рост Вовы'))
# r3 = int(input('рост димы'))
# if r1 > r2 and r1 >r3:
#     if r2 > r3:
#         print('боря вова дима')
#     if r3 > r2:
#         print('боря дима вова')
# if r2 > r1 and r2 >r3:
#     if r1 > r3:
#         print('вова боря дима')
#     if r3 > r1:
#         print('вова дима боря')
# if r3 > r1 and r3 >r2:
#     if r1 > r2:
#         print('дима вова боря')
#     if r2 > r1:
#         print('дима боря вова')

# Даны три целых числа. Найдите наибольшее из них (программа должна вывести
# ровно одно целое число). Под наибольшим в этой задаче понимается число, которое не меньше,
# чем любое другое.



# Даны три натуральных числа A, B, C. Определите, существует ли треугольник с такими сторонами.
# Если треугольник существует, выведите строку YES, иначе выведите строку NO.
# Треугольник — это три точки, не лежащие на одной прямой.
# 3 4 5 -> YES

num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print('yes')
else:
    print('no')

# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).



# Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски,
# определите, может ли ладья попасть с первой клетки на вторую одним ходом.
# 4 4 5 5 -> NO



# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
# Даны две различные клетки шахматной доски, определите, может ли король попасть
# с первой клетки на вторую одним ходом.
# 4 4 5 5 -> YES



# Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите,
# может ли слон попасть с первой клетки на вторую одним ходом.
# 4 4 5 5 -> YES



# Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
# Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.
# 1 1 2 2 -> YES
# 1 1 2 3 -> NO



# Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении
# и на одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски,
# определите, может ли конь попасть с первой клетки на вторую одним ходом.
# 1 1 2 4 -> NO
# 1 1 8 8 -> NO



# Шоколадка имеет вид прямоугольника, разделенного на N×M долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки ровно K долек.
# 4 2 6 -> YES
# 2 10 7 -> NO



# Яша плавал в бассейне размером N×M метров и устал. В этот момент он обнаружил,
# что находится на расстоянии X метров от одного из длинных бортиков
# (не обязательно от ближайшего) и Y метров от одного из коротких бортиков.
# Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?
# 23 52 8 43 -> 8


