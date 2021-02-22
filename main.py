import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


def msg_with_attachment(user_id, message, photo):
    vk.method('messages.send', {'user_id': user_id, "message": message,
                                "attachment": photo, "random_id": random.randint(0, 2048)})


token = "f161b7f89fb33f6f4340094b3bf2ceff2d64e3ca72d15551286659a81d2b21846ceb6ef34fb2c5726dc83"
# API-ключ

vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# _____________________________________________________________________________________________________________________

# ______________________________________ ИНФОРМАТИКА __________________________________________________________________

inf_que1 = {1: 'У исполнителя Калькулятор две команды, которым присвоены номера:'
               '\n1.  прибавь 2,'
               '\n2.  умножь на 5.'
               '\nВыполняя первую из них, Калькулятор прибавляет к числу на экране 2, а выполняя вторую, умножает '
               'го на 5.\nНапример, программа 2121 – это программа\n\nумножь на 5,\n\nприбавь '
               '2,\n\nумножь на 5,\n\nприбавь 2,\nкоторая преобразует число 1 в число 37. \nЗапишите порядок команд '
               'в программе, которая преобразует число 2 в число 24 и содержит не более четырёх команд.',
            2: 'У исполнителя УТРОИТЕЛЬ две команды, которым присвоены номера: \n\n1. вычти 1 \n2. умножь на 3 '
               '\n\nПервая из них уменьшает число на экране на 1, вторая – увеличивает его в три раза. \n\nЗапишите '
               'порядок команд в программе получения из числа 3 числа 16, содержащей не более 5 команд, указывая лишь '
               'номера команд. \n\n(Например, программа 21211 это программа\n\nумножь на 3 \nвычти 1 \nумножь на 3 '
               '\nвычти 1 \nвычти 1 \n\nкоторая преобразует число 1 в 4.)',
            3: 'Исполнитель КАЛЬКУЛЯТОР имеет только две команды, которым присвоены номера: \n\n1. умножь на 3 \n2. '
               'вычти 2 \n\nВыполняя команду номер 1, КАЛЬКУЛЯТОР умножает число на экране на 3, а выполняя команду '
               'номер 2, вычитает из числа на экране 2. Напишите программу, содержащую не более 5 команд, которая из '
               'числа 1 получает число 23. Укажите лишь номера команд. \nНапример, программа 11221 – это '
               'программа:\n\nумножь на 3 \nумножь на 3 \nвычти 2 \nвычти 2 \nумножь на 3, \n\nкоторая преобразует '
               'число 1 в число 15.'}
inf_ans1 = {1: '1211',
            2: '12211',
            3: '11122'}

inf_que2 = {1: ('2. На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице содержатся '
                'сведения о длинах этих дорог (в километрах).\n\nТак как таблицу и схему рисовали независимо друг от '
                'друга, то нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на '
                'графе. Определите, какова длина дороги из пункта Г в пункт Е. В ответе запишите целое число – так, '
                'как оно указано в таблице.', 'photo-200366169_457239040'),
            2: ('2. На рисунке схема дорог изображена в виде графа, в таблице содержатся сведения о длине этих дорог в '
                'километрах.\n\nТак как таблицу и схему рисовали независимо друг от друга, то нумерация населённых '
                'пунктов в таблице никак не связана с буквенными обозначениями на графе. Определите длину дороги из '
                'пункта Б в пункт Г. В ответе запишите целое число. \n\nВНИМАНИЕ. Длины отрезков на схеме не отражают '
                'длины дорог.', 'photo-200366169_457239041'),
            3: ('2. На рисунке схема дорог изображена в виде графа, в таблице содержатся сведения о длине этих дорог в '
                'километрах.\n\nТак как таблицу и схему рисовали независимо друг от друга, то нумерация населённых '
                'пунктов в таблице никак не связана с буквенными обозначениями на графе. Укажите кратчайший путь из '
                'пункта А в пункт К. В ответе перечислите все населённые пункты, через которые проходит путь. '
                'Например, путь из Г в Д через Е и К записывается как ГЕКД.', 'photo-200366169_457239042')}
inf_ans2 = {1: '40',
            2: '56',
            3: 'АБВЕК'}

inf_que3 = {1: ('3.', 'photo-200366169_457239043'),
            2: ('3.', 'photo-200366169_457239044'),
            3: ('3.', 'photo-200366169_457239045')}
inf_ans3 = {1: 'yzwx',
            2: 'zyxw',
            3: 'xzwy'}

inf_que4 = {1: ('4. Даны фрагменты двух таблиц из базы данных. Каждая строка таблицы 2 содержит информацию о ребёнке '
                'и об одном из его родителей. Информация представлена значением поля ID в соответствующей строке '
                'таблицы 1. На основании имеющихся данных определите ID человека, у которого в момент достижения 50 '
                'полных лет было наибольшее количество внуков и внучек. При вычислении ответа учитывайте только '
                'информацию из приведённых фрагментов таблиц.', 'photo-200366169_457239046'),
            2: ('4. Даны фрагменты двух таблиц из базы данных. Каждая строка таблицы 2 содержит информацию о ребёнке '
                'и об одном из его родителей. Информация представлена значением поля ID в соответствующей строке '
                'таблицы 1. На основании имеющихся данных определите, у скольких детей отец старше матери, '
                'но не более чем на 2 года. При вычислении ответа учитывайте только информацию из приведённых '
                'фрагментов таблиц.', 'photo-200366169_457239047'),
            3: ('4. Даны фрагменты двух таблиц из базы данных. Каждая строка таблицы 2 содержит информацию о ребёнке '
                'и об одном из его родителей. Информация представлена значением поля ID в соответствующей строке '
                'таблицы 1. На основании имеющихся данных определите, у скольких людей из списка первый внук или '
                'внучка появились после достижения 60 полных лет. При вычислении ответа учитывайте только информацию '
                'из приведённых фрагментов таблиц.', 'photo-200366169_457239048')}
inf_ans4 = {1: '849',
            2: '3',
            3: '1'}

inf_que5 = {1: '5. Для какого наименьшего целого неотрицательного числа A выражение\n\n(2m + 3n > 43) ∨ (m < A) ∨ (n '
               '≤ A)\n\nтождественно истинно при любых целых неотрицательных m и n?',
            2: '5. Для какого наименьшего целого неотрицательного числа A выражение \n\n(3x + 4y ≠ 60) ∨ ((A ≥ x) ∧ ('
               'A ≥ y)) \n\nтождественно истинно при любых целых неотрицательных x и y?',
            3: 'Элементами множеств А, P, Q являются натуральные числа, причём P = {2, 4, 6, 8, 10, 12, 14, 16, 18, '
               '20}, Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}. \n\nИзвестно, что выражение \n\n((x ∈ P) → (x ∈ A)) ∨ '
               '(¬(x ∈ A) → ¬(x ∈ Q)) \n\nистинно (т. е. принимает значение 1) при любом значении переменной х. '
               'Определите наименьшее возможное значение суммы элементов множества A.'}
inf_ans5 = {1: '9',
            2: '20',
            3: '36'}

inf_que6 = {1: ('6. Определите, при каком наибольшем введённом значении переменной s программа выведет число 64.',
                'photo-200366169_457239049'),
            2: ('6. Определите, что будет напечатано в результате работы следующего фрагмента программы:',
                'photo-200366169_457239050'),
            3: ('6. Запишите число, которое будет напечатано в результате выполнения следующей программы.',
                'photo-200366169_457239051')}
inf_ans6 = {1: '259',
            2: '65',
            3: '390'}

inf_que7 = {1: '7. У исполнителя, который работает с положительными однобайтовыми двоичными числами, две команды, '
               'которым присвоены номера: \n\n1. сдвинь влево \n\n2. вычти 1 \n\nВыполняя первую из них, исполнитель '
               'сдвигает число на один двоичный разряд влево, причём на место освободившегося бита ставится 0. '
               'Выполняя вторую команду исполнитель вычитает из числа 1. Исполнитель начал вычисления с числа 91 и '
               'выполнил цепочку команд 112112. Запишите результат в десятичной системе.',
            2: '7. Исполнитель Вычислитель работает с целыми положительными однобайтными числами. Он может выполнять '
               'две команды: \n\n1. сдвинь биты числа влево на одну позицию \n\n2. прибавь 1 \n\nНапример, '
               'число 7 (000001112) преобразуется командой 1 в 14 (000011102). Для заданного числа 14 выполнена '
               'последовательность команд 11222. Запишите полученный результат в десятичной системе счисления.',
            3: '7. Исполнитель КУЗНЕЧИК живёт на числовой оси. Начальное положение КУЗНЕЧИКА – точка 0. Система '
               'команд Кузнечика: \n\nВперед 5 – Кузнечик прыгает вперёд на 5 единиц, \n\nНазад 3 – Кузнечик прыгает '
               'назад на 3 единицы. \n\nКакое наименьшее количество раз должна встретиться в программе команда «Назад '
               '3», чтобы Кузнечик оказался в точке 21?'}
inf_ans7 = {1: '171',
            2: '59',
            3: '3'}

inf_que8 = {1: '8. Сколько существует шестизначных чисел, делящихся на 5, в которых каждая цифра может встречаться '
               'только один раз, при этом никакие две чётные и две нечётные цифры не стоят рядом.',
            2: '8. Ольга составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё '
               'кодовое слово. В качестве кодовых слов Ольга использует 4-буквенные слова, в которых есть только '
               'буквы A, B, C, D, E, X, причём буква X появляется ровно 1 раз и только на первом или последнем месте. '
               'Каждая из других допустимых букв может встречаться в кодовом слове любое количество раз или не '
               'встречаться совсем. Сколько различных кодовых слов может использовать Ольга?',
            3: '8. Найдите количество пятизначных восьмеричных чисел, в которых все цифры различны и никакие две четные'
               ' или нечетные не стоят рядом.'}
inf_ans8 = {1: '1296',
            2: '250',
            3: '504'}

inf_que9 = {1: '9. Запишите натуральное число, десятичная запись которого состоит из двух цифр, шестнадцатеричная '
               'запись заканчивается цифрой B, а пятеричная — цифрой 3.',
            2: '9. Запись числа в девятеричной системе счисления заканчивается цифрой 4. Какой будет последняя цифра '
               'в записи этого числа в троичной системе счисления?',
            3: '9. К записи натурального числа в восьмеричной системе счисления справа приписали два нуля. Во сколько '
               'раз увеличилось число? Ответ запишите в десятичной системе счисления.'}
inf_ans9 = {1: '43',
            2: '1',
            3: '64'}

inf_que10 = {1: '10. Сотрудникам компании выдают электронную карту, на которой записаны их личный код, '
                'номер подразделения (целое число от 1 до 1200) и дополнительная информация. Личный код содержит 17 '
                'символов и может включать латинские буквы из 26-символьного латинского алфавита (заглавные и '
                'строчные буквы различаются), десятичные цифры и специальные знаки из набора @#$%^&*(). Для хранения '
                'кода используется посимвольное кодирование, все символы кодируются одинаковым минимально возможным '
                'количеством битов, для записи кода отводится минимально возможное целое число байтов. Номер '
                'подразделения кодируется отдельно и занимает минимально возможное целое число байтов. Известно, '
                'что на карте хранится всего 48 байтов данных. Сколько байтов занимает дополнительная информация?',
             2: '10. Каждый сотрудник предприятия получает электронный пропуск, на котором записаны личный код '
                'сотрудника, код подразделения и некоторая дополнительная информация. Личный код состоит из 13 '
                'символов, каждый из которых может быть одной из 12 допустимых заглавных букв или одной из 10 цифр. '
                'Для записи личного кода на пропуске отведено минимально возможное целое число байт. При этом '
                'используют посимвольное кодирование, все символы кодируют одинаковым минимально возможным '
                'количеством бит. Код подразделения состоит из двух трёхзначных чисел, каждое из которых кодируется '
                'как двоичное число и занимает минимально возможное целое число байт. Всего на пропуске хранится 32 '
                'байт данных. Сколько байт выделено для хранения дополнительных сведений об одном сотруднике? В '
                'ответе запишите только целое число — количество байт.',
             3: '10. Каждый сотрудник предприятия получает электронный пропуск, на котором записаны личный код '
                'сотрудника, код подразделения и некоторая дополнительная информация. Личный код состоит из 18 букв. '
                'Для формирования кодов используется 15 различных букв, каждая из которых может быть заглавной или '
                'строчной. Для записи кода на пропуске отведено минимально возможное целое число байт. При этом '
                'используют посимвольное кодирование, все символы кодируют одинаковым минимально возможным '
                'количеством бит. Код подразделения — целое трёхзначное число, он записан на пропуске как двоичное '
                'число и занимает минимально возможное целое число байт. Всего на пропуске хранится 30 байт данных. '
                'Сколько байт выделено для хранения дополнительных сведений об одном сотруднике? В ответе запишите '
                'только целое число — количество байт.'}
inf_ans10 = {1: '31',
             2: '19',
             3: '16'}

inf_que = {1: inf_que1, 2: inf_que2, 3: inf_que3, 4: inf_que4, 5: inf_que5, 6: inf_que6, 7: inf_que7, 8: inf_que8,
           9: inf_que9, 10: inf_que10}
inf_ans = {1: inf_ans1, 2: inf_ans2, 3: inf_ans3, 4: inf_ans4, 5: inf_ans5, 6: inf_ans6, 7: inf_ans7, 8: inf_ans8,
           9: inf_ans9, 10: inf_ans10}

# ______________________________________ МАТЕМАТИКА: _________________________________________________________________

math_que1 = {1: '1. Держатели дисконтной карты книжного магазина получают при покупке скидку 4 %. Книга стоит 150 '
                'рублей. Сколько рублей заплатит держатель дисконтной карты за эту книгу?',
             2: '1. Аня купила проездной билет на месяц и сделала за месяц 41 поездку. Сколько рублей она сэкономила, '
                'если проездной билет на месяц стоит 580 рублей, а разовая поездка — 20 рублей?',
             3: '1. На день рождения полагается дарить букет из нечетного числа цветов. Тюльпаны стоят 35 рублей за '
                'штуку. У Вани есть 160 рублей. Из какого наибольшего числа тюльпанов он может купить букет Маше на '
                'день рождения?'}
math_ans1 = {1: '144',
             2: '240',
             3: '3'}

math_que2 = {1: ('2. Когда самолет находится в горизонтальном полете, подъемная сила, действующая на крылья, '
                 'зависит только от скорости. На рисунке изображена эта зависимость для некоторого самолета. На оси '
                 'абсцисс откладывается скорость (в километрах в час), на оси ординат – сила (в тоннах силы). В '
                 'некоторый момент подъемная сила равнялась одной тонне силы. Определите по рисунку, на сколько '
                 'километров в час надо увеличить скорость, чтобы подъемная сила увеличилась до 4 тонн силы?',
                 'photo-200366169_457239018'),
             2: ('2. На рисунке жирными точками показана среднесуточная температура воздуха в Бресте каждый день с 6 '
                 'по 19 июля 1981 года. По горизонтали указываются числа месяца, по вертикали — температура в градусах '
                 'Цельсия. Для наглядности жирные точки соединены линией. Определите по рисунку разность между '
                 'наибольшей и наименьшей среднесуточными температурами за указанный период. Ответ дайте в градусах '
                 'Цельсия.', 'photo-200366169_457239019'),
             3: ('2. На диаграмме показано распределение выплавки меди в 11 странах мира(в тысячах тонн) за 2006 год. '
                 'Среди представленных стран первое место по выплавке меди занимала Папуа — Новая Гвинея, '
                 'одиннадцатое место — Индия. Какое место занимала Аргентина?', 'photo-200366169_457239020')}
math_ans2 = {1: '200',
             2: '10',
             3: '2'}

math_que3 = {1: ('3. Найдите площадь треугольника, изображенного на клетчатой бумаге с размером клетки 1 см * 1 см '
                 '(см. рис.). Ответ дайте в квадратных сантиметрах.', 'photo-200366169_457239021'),
             2: ('3. На клетчатой бумаге изображены два круга. Площадь внутреннего круга равна 8. Найдите площадь '
                 'заштрихованной фигуры.', 'photo-200366169_457239022'),
             3: ('3. Найдите площадь параллелограмма, изображенного на рисунке.', 'photo-200366169_457239023')}
math_ans3 = {1: '9',
             2: '10',
             3: '6'}

math_que4 = {1: '4. На чемпионате по прыжкам в воду выступают 30 спортсменов, среди них 10 прыгунов из Великобритании '
                'и 3 прыгуна из Канады. Порядок выступлений определяется жеребьёвкой. Найдите вероятность того, '
                'что двадцать девятым будет выступать прыгун из Канады.',
             2: '4. Вероятность того, что новый электрический чайник прослужит больше года, равна 0,93. Вероятность '
                'того, что он прослужит больше двух лет, равна 0,87. Найдите вероятность того, что он прослужит '
                'меньше двух лет, но больше года.',
             3: '4. На борту самолёта 22 места рядом с запасными выходами и 11 мест за перегородками, разделяющими '
                'салоны. Остальные места неудобны для пассажира высокого роста. Пассажир В. высокого роста. Найдите '
                'вероятность того, что на регистрации при случайном выборе места пассажиру В. достанется удобное '
                'место, если всего в самолёте 300 мест.'}
math_ans4 = {1: '0.1',
             2: '0.06',
             3: '0.11'}

math_que5 = {1: ('5. Решите уравнение:', 'photo-200366169_457239024'),
             2: ('5. Найдите корень уравнения:', 'photo-200366169_457239025'),
             3: ('5. Найдите корень уравнения:', 'photo-200366169_457239026')}
math_ans5 = {1: '-3',
             2: '-29',
             3: '8.75'}

math_que6 = {1: ('6. Острый угол ромба равен 30°. Радиус вписанной в этот ромб окружности равен 9. Найдите '
                 'сторону ромба.', 'photo-200366169_457239027'),
             2: '6. В треугольнике ABC AC=BC=27, AH - высота, sinBAC = 2/3. Найдите BH.',
             3: ('6. Периметр прямоугольника равен 54, а диагональ равна 26. Найдите площадь этого прямоугольника.',
                 'photo-200366169_457239028')}
math_ans6 = {1: '36',
             2: '30',
             3: '26.5'}

math_que7 = {1: ('7.', 'photo-200366169_457239037'),
             2: ('7.', 'photo-200366169_457239038'),
             3: ('7.', 'photo-200366169_457239039')}
math_ans7 = {1: '1',
             2: '11',
             3: '5'}

math_que8 = {1: '8. Высота конуса равна 5, а диаметр основания – 24. Найдите образующую конуса.',
             2: ('8. В правильной четырехугольной пирамиде высота равна 8, боковое ребро равно 10. Найдите ее объем.',
                 'photo-200366169_457239035'),
             3: ('8. Во сколько раз увеличится объем куба, если все его рёбра увеличить в 5 раз?',
                 'photo-200366169_457239036')}
math_ans8 = {1: '13',
             2: '192',
             3: '125'}

math_que9 = {1: ('9. Найдите значение выражения:', 'photo-200366169_457239032'),
             2: ('9. Найдите значение выражения:', 'photo-200366169_457239033'),
             3: ('9. Найдите значение выражения:', 'photo-200366169_457239034')}
math_ans9 = {1: '1',
             2: '12',
             3: '-5'}

math_que10 = {1: ('10.', 'photo-200366169_457239029'),
              2: ('10.', 'photo-200366169_457239030'),
              3: ('10.', 'photo-200366169_457239031')}
math_ans10 = {1: '6.72',
              2: '0.036',
              3: '3'}

math_que = {1: math_que1, 2: math_que2, 3: math_que3, 4: math_que4, 5: math_que5, 6: math_que6, 7: math_que7, 8: math_que8,
            9: math_que9, 10: math_que10}
math_ans = {1: math_ans1, 2: math_ans2, 3: math_ans3, 4: math_ans4, 5: math_ans5, 6: math_ans6, 7: math_ans7, 8: math_ans8,
            9: math_ans9, 10: math_ans10}

# _____________________________________________________________________________________________________________________


def exam():
    for ev in longpoll.listen():
        if ev.type == VkEventType.MESSAGE_NEW:
            if ev.to_me:
                text1 = ev.text.lower()

                if text1 == 'информатика':
                    test_ = {'question': inf_que, 'answer': inf_ans}
                    break
                elif text1 == 'математика':
                    test_ = {'question': math_que, 'answer': math_ans}
                    break
                else:
                    write_msg(event.user_id, 'Такого предмета нет! :(')

    write_msg(event.user_id, 'Тест содержит в себе 10 вопросов, внимательно читай задания и отвечай на вопросы без '
                             'пробелов и дополнительных символов: точек, запятых и т.д. (дробные числа через точку, '
                             'отрицательные с -)\nЗадания взяты с образовательного портала https://ege.sdamgia.ru/')
    right_wrong = []

    for task_num in range(1, 11):
        rnd = random.randint(1, 3)
        if type(test_['question'][task_num][rnd]) == tuple:
            msg_with_attachment(event.user_id, *test_['question'][task_num][rnd])
        else:
            write_msg(event.user_id, test_['question'][task_num][rnd])

        for ev in longpoll.listen():
            if ev.type == VkEventType.MESSAGE_NEW:
                if ev.to_me:
                    text_1 = ev.text.lower()

                    if text_1 == test_['answer'][task_num][rnd]:
                        right_wrong += ['Верно!']
                        break
                    else:
                        right_wrong += ['Неверно!']
                        break

    write_msg(event.user_id, f' Твои результаты:\nВопрос 1: {right_wrong[0]}\nВопрос 2: {right_wrong[1]}\nВопрос '
                             f'3: {right_wrong[2]}\nВопрос 4: {right_wrong[3]}\nВопрос 5: {right_wrong[4]}\nВопрос '
                             f'6: {right_wrong[5]}\nВопрос 7: {right_wrong[6]}\nВопрос 8: {right_wrong[7]}\nВопрос '
                             f'9: {right_wrong[8]}\nВопрос 10: {right_wrong[9]}')

# ___________________________________________________________________________


print("Бот запущен")


# Основной цикл
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            # Сообщение от пользователя
            request = event.text.lower()

            if request == "привет":
                write_msg(event.user_id, "Привет!")

            elif request == "пока":
                write_msg(event.user_id, "До скорого!")

            elif request == "проверить знания" or request == "проверка знаний":
                write_msg(event.user_id, "Выбери предмет, по которому хочешь пройти тест:\n- Математика\n- "
                                         "Информатика")
                exam()

            else:
                write_msg(event.user_id, "Извините, я не понимаю! Пожалуйста, используйте одну из предложенных "
                                         "комманд: привет, пока, проверка знаний.")


