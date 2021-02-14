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

# ___________________________________________________________________________

inf_que1 = {1: 'У исполнителя Калькулятор две команды, которым присвоены номера:'
               '\n1.  прибавь 2,'
               '\n2.  умножь на 5.'
               '\nВыполняя первую из них, Калькулятор прибавляет к числу на экране 2, а выполняя вторую, умножает '
               'го на 5.\nНапример, программа 2121 – это программа\n\nумножь на 5,\n\nприбавь 2,\n\nумножь на 5,\n\nприбавь '
               '2,\nкоторая преобразует число 1 в число 37. \nЗапишите порядок команд в программе, которая преобразует '
               'число 2 в число 24 и содержит не более четырёх команд.',
            2: '3*1',
            3: '3-1'}
inf_ans1 = {1: '1211', 2: '3', 3: '2'}

inf_que2 = {1: '3+1', 2: '3*1', 3: '3-1'}
inf_ans2 = {1: '4', 2: '3', 3: '2'}

inf_que3 = {1: '3+1', 2: '3*1', 3: '3-1'}
inf_ans3 = {1: '4', 2: '3', 3: '2'}

inf_que4 = {1: '3+1', 2: '3*1', 3: '3-1'}
inf_ans4 = {1: '4', 2: '3', 3: '2'}

inf_que5 = {1: '3+1', 2: '3*1', 3: '3-1'}
inf_ans5 = {1: '4', 2: '3', 3: '2'}

inf_que6 = {1: '3+1', 2: '3*1', 3: '3-1'}
inf_ans6 = {1: '4', 2: '3', 3: '2'}

inf_que7 = {1: '3+1', 2: '3*1', 3: '3-1'}
inf_ans7 = {1: '4', 2: '3', 3: '2'}

inf_que8 = {1: '3+1', 2: '3*1', 3: '3-1'}
inf_ans8 = {1: '4', 2: '3', 3: '2'}

inf_que9 = {1: '3+1', 2: '3*1', 3: '3-1'}
inf_ans9 = {1: '4', 2: '3', 3: '2'}

inf_que10 = {1: '3+1', 2: '3*1', 3: '3-1'}
inf_ans10 = {1: '4', 2: '3', 3: '2'}

inf_que = {1: inf_que1, 2: inf_que2, 3: inf_que3, 4: inf_que4, 5: inf_que5, 6: inf_que6, 7: inf_que7, 8: inf_que8,
           9: inf_que9, 10: inf_que10}
inf_ans = {1: inf_ans1, 2: inf_ans2, 3: inf_ans3, 4: inf_ans4, 5: inf_ans5, 6: inf_ans6, 7: inf_ans7, 8: inf_ans8,
           9: inf_ans9, 10: inf_ans10}

# inf_que1 = {1: '4',
#             2: '3*1',
#             3: '3-1'}
# inf_ans1 = {1: '1211', 2: '3', 3: '2'}
#
# inf_que2 = {1: '3+1', 2: '3*1', 3: '3-1'}
# inf_ans2 = {1: '4', 2: '3', 3: '2'}
#
# inf_que3 = {1: '3+1', 2: '3*1', 3: '3-1'}
# inf_ans3 = {1: '4', 2: '3', 3: '2'}
#
# inf_que4 = {1: '3+1', 2: '3*1', 3: '3-1'}
# inf_ans4 = {1: '4', 2: '3', 3: '2'}
#
# inf_que5 = {1: '3+1', 2: '3*1', 3: '3-1'}
# inf_ans5 = {1: '4', 2: '3', 3: '2'}
#
# inf_que6 = {1: '3+1', 2: '3*1', 3: '3-1'}
# inf_ans6 = {1: '4', 2: '3', 3: '2'}
#
# inf_que7 = {1: '3+1', 2: '3*1', 3: '3-1'}
# inf_ans7 = {1: '4', 2: '3', 3: '2'}
#
# inf_que8 = {1: '3+1', 2: '3*1', 3: '3-1'}
# inf_ans8 = {1: '4', 2: '3', 3: '2'}
#
# inf_que9 = {1: '3+1', 2: '3*1', 3: '3-1'}
# inf_ans9 = {1: '4', 2: '3', 3: '2'}
#
# inf_que10 = {1: '3+1', 2: '3*1', 3: '3-1'}
# inf_ans10 = {1: '4', 2: '3', 3: '2'}
#
# inf_que = {1: inf_que1, 2: inf_que2, 3: inf_que3, 4: inf_que4, 5: inf_que5, 6: inf_que6, 7: inf_que7, 8: inf_que8,
#            9: inf_que9, 10: inf_que10}
# inf_ans = {1: inf_ans1, 2: inf_ans2, 3: inf_ans3, 4: inf_ans4, 5: inf_ans5, 6: inf_ans6, 7: inf_ans7, 8: inf_ans8,
#            9: inf_ans9, 10: inf_ans10}

# ___________________________________________________________________________


def exam():
    for ev in longpoll.listen():
        if ev.type == VkEventType.MESSAGE_NEW:
            if ev.to_me:
                text1 = ev.text.lower()

                if text1 == 'информатика':
                    test_ = {'question': inf_que, 'answer': inf_ans}
                    break
                else:
                    write_msg(event.user_id, 'Такого предмета нет! :(')

    write_msg(event.user_id, 'Тест содержит в себе 10 вопросов, внимательно читай задания и отвечай на вопросы без '
                             'пробелов и дополнительных символов: точек, запятых и т.д.')
    right_wrong = []

    for task_num in range(1, 11):
        rnd = random.randint(1, 3)
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

            elif request == "а":
                photo = 'photo-200366169_457239017'
                msg_with_attachment(event.user_id, '', photo)

            elif request == "проверить знания":
                write_msg(event.user_id, "Выбери предмет, по которому хочешь пройти тест:")
                exam()

            else:
                write_msg(event.user_id, "Извините, я не понимаю! Пожалуйста, используйте одну из предложенных комманд:")


