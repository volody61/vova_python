# # Бит или не бит?

# Из разговора двух программистов:
# – Ну вот представь, что у тебя есть 1000 рублей...
# – Не-е-е, давай уж округлим... пусть у меня есть 1024 рубля.
# Этот программистский анекдот шокирует людей, далеких от компьютерной тематики.
# Действительно, довольно сложно понять почему число 1024 круглое?
# Все дело в том, что компьютер работает с двоичной системой счисления,
# а 1024 в двоичном коде - это единица с десятью нулями: 10000000000,
# для компьютера оно круглое. Именно поэтому производные единицы измерения в
# информатике связаны не с 1000,
# как это принято (1 кг = 1000 гр, 1 км = 1000 м и т.д.), а с числом 1024.
# Организуйте вывод памятки для начинающего программиста.
# Вам нужно написать программу так, чтобы расчет значения
# в последней строке выполнялся непосредственно перед ее выводом и подставлялся вместо ХХХХ.
#
# 1 бит - минимальная единица количества информации.
# 1 байт = 8 бит.
# 1 Килобит = 1024 бита.
# 1 Килобайт = 1024 байта.
# 1 Килобайт = ХХХХ бит.

print('1 байт -', '8 бит')
print('1 килобит -', 1024 // 8, 'байт или ', '1024 бита')
print('1 килобайт - ', 8 * 1024, 'бит или ', '1024 байта')

# # # Гороскоп

# У нас есть бизнес-план!
# Пункт первый: надо написать программу-гороскоп, которая по некоторым простым вопросам
# выдаёт строго индивидуальный анализ личностных качеств.
# Мы будем делать это по передовым астрологическим методикам.
# Напишите программу, которая считывает с клавиатуры последовательно:
# имя, фамилию, любимое животное, знак зодиака.

# После этого программа выводит:
# Индивидуальный гороскоп для пользователя [имя] [фамилия]
# Кем вы были в прошлой жизни: [любимое животное]
# Ваш знак зодиака - [знак зодиака] , поэтому вы - тонко чувствующая натура.
# Уточнение: слова про тонко чувствующую натуру выводятся абсолютно всегда, независимо от того,
# что именно вводил пользователь (это пародия на процесс составления «реального» гороскопа).
# В один и тот же фиксированный текст подставляются те слова, которые вводил пользователь.
# Пробел перед запятой по правилам, конечно, не ставится, но здесь пусть стоит.

# Индивидуальный гороскоп для пользователя Вася Пупкин
# Кем вы были в прошлой жизни: конь
# Ваш знак зодиака - козерог, поэтому вы - тонко чувствующая натура.

im = input('имя')
fam = input('фамилия')
an = input('любимое животное')
zn = input('знак зодиака')

print('Индивидуальный гороскоп для пользователя', im, fam,)
print('Кем вы были в прошлой жизни:', an,)
print('Ваш знак зодиака -',zn,)
print('поэтому вы - тонко чувствующая натура.')

# # билетная касса
# Напишите программу, которая считывает с клавиатуры последовательно три строки:
# название фильма, название кинотеатра и время, после чего выводит на экран
# «Билет на " [название фильма] " в " [название кинотеатра] " на [время] забронирован.» .

film = input('название фильма')
pl = input('название кинотеатра')
time = input('время')

print('Билет на', film, 'в', pl, 'на', time, 'забронирован')