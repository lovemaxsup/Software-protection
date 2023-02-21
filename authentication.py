from additional_functions import *

def Authentication(username, password):  # аутентифікація юзера за паролем

    access = False  # по дефолту забороняємо вхід
    df = read_csv_to_dataframe()

    index = find_row_index(df, 'username', username)

    password_in_db = str(get_dataframe_value(df, 'password', index))


    if password == password_in_db or password_in_db == 'nan':  # перевіряємо чи паролі сходяться
        access = True  # надаємо доступ до додатку
        print()
    else:
        print("Пароль невірний")
    return access
