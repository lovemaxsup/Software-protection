from admin_functions import *
from authentication import *







def vikno_vhodu(): #базовий інтерфейс програми через який можна буде залогінитися.

    if check_file_in_current_dir() == True:
        pass
    else:
        create_db()

    chu_vidprazivalo = 0
    print("Вітаю вас у програмі! ")
    while True:
        if chu_vidprazivalo == 0:
            print("Вам доступні такі опції: 1 - Увійти; 2 - Про програму; 3 - Завершити роботу")
            print()
            basic_command = input("Виберіть дію (впишіть цифру наприклад: 1): ")
            if basic_command == '2':
                print("*"*100)
                dispaly_info()
                print("*"*100)
                print()
            elif basic_command == '3':
                break
            #перевіряємо чи юзер взагалі існує і якщо так починаємо процес аутентифікації для нього
            elif basic_command == "1": #починаємо цикл для юзера з 3 попиток вгадати валідний username
                    username_counter = 1
                    while True:
                        if username_counter < 3: #даємо можливість юзеру 3 рази вгадати пароль
                            print()
                            username = input("Введіть ваш username:")
                            if check_if_user_already_exist(username) == False:
                                print("Даний юзер не зареєстрований. Спробуйте ще раз, у вас залишилося {0} спроби".format(3-username_counter))
                                username_counter += 1

                            elif checking_for_block(username):
                                print()
                                print("Вибачте, але адміністратор вас заблокував")
                                print()
                                break
                            elif check_if_user_already_exist(username) == True:

                                #Починаємо автентифікацію
                                print()
                                password_counter = 1
                                while True:
                                    if password_counter < 4:
                                        password = input("Введіть ваш пароль: ")
                                        if Authentication(username, password) == True:
                                            print()

                                            main(username)
                                            username_counter += 10  # Примітивний костиль, але без нього не працює. Типу вже не треба потім вводити юзернейм
                                            chu_vidprazivalo = 1
                                            break
                                        else:
                                            print()
                                            print('Пароль введено невірно. У вас залишилися {0} спроби'.format(3-password_counter))
                                            password_counter += 1
                                    else:
                                        print()
                                        print("Всі спроби вчичерпалися, на жаль.")
                                        print()
                                        break
                        elif username_counter > 7:
                            break # Ще один костиль, щоб воно як-небудь робило
                        else:
                            print("Всі спроби завершилися, на жаль.")
                            break


            else:
                print()
                print("Такої команди не існує. Спробуйте ще раз!")
        else:
            break

def main(username):
    df = read_csv_to_dataframe()
    index = find_row_index(df, 'username', username)
    usertype = get_dataframe_value(df, 'type', index)
    #Розмежовуємо доступ відповідно до типу юзера
    while True:
        if usertype == 'admin':
            print()
            print('Вітаю вас, {0}'.format(username))
            print()
            print("Вам доступні такі опції:")
            print("1 - Змінити власний пароль;")
            print("2 - Перегляд інформації про зареєстрованих користувачів;")
            print("3 - Додати нового юзера;")
            print("4 - Заблокувати вибраного користувача;")
            print("5 - Додати парольні обмеження певному користувачеві;")
            print("6 - Зняти парольні обмеження для певного користувача; ")
            print("7 - Завершити роботу;")
            command = int(input("Виберіть дію (впишіть цифру наприклад: 1): "))

            if command == 1:
                change_password(username)
            elif command == 2:
                view_all_userinfo()
            elif command == 3:
                add_user()
            elif command == 4:
                block_user()
            elif command == 5:
                enable_passwd_constraints()
            elif command == 6:
                disable_passwd_constraints()
            elif command == 7:
                break
            else:
                print()
                print("Такої команди не існує. Спробуйте ще раз!")





        elif usertype == 'user':
            print()
            print('Вітаю вас, {0}'.format(username))
            print()
            print("Вам доступні такі опції:")
            print("1 - Змінити власний пароль;")
            print("2 - Завершити роботу;")
            command = int(input("Виберіть дію (впишіть цифру наприклад: 1): "))
            if command == 1:
                change_password(username)
            elif command == 2:
                break

            else:
                print()
                print("Такої команди не існує. Спробуйте ще раз!")






vikno_vhodu() #запускаємо програму
