from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_config import group_token_vk, user_token_vk,V,group_id
from function_vk import VK_USER
import sqlite3 as sql



# Запускаем бот
vk_session = VkApi(token=group_token_vk, api_version=V)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=group_id)


keyboard_1 = VkKeyboard(one_time=False, inline=True)
# добавление кнопки на клавиатуру
keyboard_1.add_callback_button(label='Дальше', color=VkKeyboardColor.PRIMARY, payload={"type": "1"})

n = 0
l = 0

for event in longpoll.listen():
    # отправляем кнопку при текстовом сообщении от пользователя содержащее id
    if event.type == VkBotEventType.MESSAGE_NEW:
        if len(event.obj.message['text']) == 10 or len(event.obj.message['text']) == 11:
            id_user = event.obj.message['text']
            if event.from_user:
                ya = VK_USER(group_token_vk=group_token_vk, user_token_vk=user_token_vk, id=id_user)
                ya.request_parameters_user(id=id_user)
                ya.request_users()
                ya.request_users2()
                ya.users_foto_vk()
                ya.users_ban()
                vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard=keyboard_1.get_keyboard(),
                        message=f"Для просмотра  пользователей нажмите кнопку 'Дальше'")
        else:
            if event.from_user:
                vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        message=f"Для поиска пары введите свой id(Пример:id23408991)")
    # обработка кликов по кнопке
    elif event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload.get('type') == '1':
            connection = sql.connect('VKinder.db')
            with connection:
                cur = connection.cursor()
                value1 = (cur.execute("SELECT * FROM 'searching_results'").fetchall())
                value2 = value1[n]
                id_users = f'{value2[0]}\n'
                link_users = f'{value2[1]}\n'
                foto1 = f'{value2[2]}\n'
                foto2 = f'{value2[3]}\n'
                foto3 = f'{value2[4]}\n'
            connection.commit()
            cur.close()
            last_id = vk.messages.edit(
                      peer_id=event.obj.peer_id,
                      message=(id_users, link_users),
                      attachment=(foto1, foto2, foto3),
                      conversation_message_id=event.obj.conversation_message_id,
                      keyboard=keyboard_1.get_keyboard())
        n = n + 1
        l = len(value1)
        if n == l:
            n = 0


if __name__ == '__main__':
    print()