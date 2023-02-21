from additional_functions import *
import time


def change_password(username):
    column_name = 'password'
    df = read_csv_to_dataframe()
    index = find_row_index(df, 'username', username)

    #Перевірка чи юзер ввів правильний старий пароль

    sproba = 0 #лічільник, який показує скільки було спроб
    while sproba < 3:
        print()
        old_password = input("Введіть, будь ласка, старий пароль: ")
        check_passwd = str(get_dataframe_value(df, column_name, index))

        if check_passwd == old_password or check_passwd == 'nan':
            print()
            #Тут перевіряємо чи нема обмежень на пароль
            if check_user_for_password_constraints(username) == False:

                new_password = input('Введіть новий пароль: ')
                print()
                change_dataframe_value(df, column_name,index, new_password)
                write_dataframe_to_csv(df)
                print("Вітаю! Пароль змінено!")
                break
            else:
                print("На вас діють парольні обмеження")
                print("Парольні обмеження: Наявність рядкових і прописних латинських букв, цифр і символів кирилиці.")
                print()
                new_password = input('Введіть новий пароль: ')
                print()
                if check_password_for_compliance(new_password):
                    change_dataframe_value(df, column_name, index, new_password)
                    write_dataframe_to_csv(df)
                    print("Вітаю! Пароль змінено!")
                    time.sleep(2)
                    break
                else:
                    print("Пароль не відповідає обмеженням.")
        else:
            print('Старий пароль введено неправильно, поіторіть спробу, у вас залишилося {0} спроб'.format(2-sproba))
            sproba +=1
            if sproba == 3:
                print("Спроби вичерпано ((. Приходьте коли згадаєте пароль! Слава Україні!!")
                print()





def view_all_userinfo():
    columns = ['username', 'type', 'password', 'is_blocked', 'is_passwd_policy_exist']
    df = read_csv_to_dataframe()
    if  df.shape[0] < 2:
        print()
        print("Список юзерів поки пустий.")
    else:
        display_columns_without_first_row(df,columns)
        print()


def add_user():
    print()
    while True:
        username = input("Введіть username нового user(a): ")
        if check_if_user_already_exist(username) == False:
            append_to_db(username) #додали юзера до бази даних
            print("Вітаю, новий user - {0} додано!".format(username))
            print()
            break
        else:
            print("username - {0} вже використовується, спробуйте інший".format(username))
            print()


def block_user():
    while True:
        print()
        user = input("Введіть ім'я користувача, якого хочете заблокувати: ")
        if check_if_user_already_exist(user) == False:
            print("Даного юзера не існує, спробуй ще раз!")
        else:
            df = read_csv_to_dataframe()
            index = find_row_index(df, 'username', user)
            change_dataframe_value(df, 'is_blocked', index, True)
            write_dataframe_to_csv(df)
            print()
            print("Вітаю, тепер user - {0} успішно заблокований!".format(user))
            print()
            break


def enable_passwd_constraints():  # функція, яка назначає парольні обмеження
    print()
    while True:
        user = input("Введіть ім'я юзера на пароль якого хочете накласти обмеження: ")
        if check_if_user_already_exist(user) == True:
            df = read_csv_to_dataframe()
            index = find_row_index(df, 'username', user)
            change_dataframe_value(df, 'is_passwd_policy_exist', index, True)
            write_dataframe_to_csv(df)
            print()
            print("Вітаю, на юзера {0} накладенні парольні обмеження".format(user))
            break
        else:
            print()
            print("Даного юзера не існує, спробуйте ще раз!")




def disable_passwd_constraints(): #Функція яка знімає парольні обмеження
    print()
    while True:
        user = input("Введіть ім'я юзера на пароль якого хочете зняти обмеження: ")
        if check_if_user_already_exist(user) == True:
            df = read_csv_to_dataframe()
            index = find_row_index(df, 'username', user)
            change_dataframe_value(df, 'is_passwd_policy_exist', index, False)
            write_dataframe_to_csv(df)
            print()
            print("Вітаю, з юзера {0} знято парольні обмеження".format(user))
            break
        else:
            print()
            print("Даного юзера не існує, спробуйте ще раз!")