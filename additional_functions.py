import csv
import pandas as pd
import os




def check_file_in_current_dir():
    current_dir = os.getcwd() # Отримати поточний каталог
    file_path = os.path.join(current_dir, 'db.csv') # Скласти шлях до файлу

    return os.path.isfile(file_path)


def checking_for_block(username):
    conclusion = False
    df = read_csv_to_dataframe()
    index = find_row_index(df, 'username', username)
    is_blocked = get_dataframe_value(df, 'is_blocked', index)
    if is_blocked == True:
        conclusion = True

    return conclusion


def append_to_db(username):

    user = create_user(username)

    # Відкриття CSV файлу для допису
    with open('db.csv', mode='a', newline='') as file:
        # Створення об'єкту для запису даних
        writer = csv.writer(file)
        # Запис нового рядка з даними
        writer.writerow(user)

def create_db():

    # Відкриття CSV файлу для запису
    with open('db.csv', mode='w', newline='') as file:
        # Створення об'єкту для запису даних
        writer = csv.writer(file)

        # Запис рядка з заголовками
        writer.writerow(['username', 'type', 'password', 'is_blocked', 'is_passwd_policy_exist']) #заголовочний рядок
        writer.writerow(['ADMIN', 'admin', '', False, False])


def write_dataframe_to_csv(df):
    df.to_csv('db.csv', index=False)

def create_user(username):
    user_info = [username, 'user', '', False, False]
    return user_info


def read_csv_to_dataframe():
    # Зчитування даних з CSV файлу та створення DataFrame
    df = pd.read_csv('db.csv')
    return df


def find_row_index(df, column_name, value):
    # Пошук індексу рядка за назвою колонки та значенням
    return df.loc[df[column_name] == value].index[0]


def change_dataframe_value(df, column_name, index, new_value):
    df.at[index, column_name] = new_value


def get_dataframe_value(df, column_name, index):
    return df.at[index, column_name]

def display_columns_without_first_row(df, columns):
    print(df.iloc[1:].loc[:, columns])

def check_if_user_already_exist(username):
    exist = False
    df = read_csv_to_dataframe()


    for i in df.index:
        if df['username'][i] == username:
           exist = True
    return exist

def check_password_for_compliance(input_pass): # функція яка перевіряє наявність рядкових і прописних латинських букв, цифр і символів кирилиці.
    is_ok = False # змінна яка показує чи парль задовольняє обмеження

    latin_lower = set('abcdefghijklmnopqrstuvwxyz')
    latin_upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digits = set('0123456789')
    cyrillic = set('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
    has_latin_lower = False
    has_latin_upper = False
    has_digits = False
    has_cyrillic = False
    for char in input_pass:
        if char in latin_lower:
            has_latin_lower = True
        elif char in latin_upper:
            has_latin_upper = True
        elif char in digits:
            has_digits = True
        elif char in cyrillic:
            has_cyrillic = True
    if has_latin_lower and has_latin_upper and has_digits and has_cyrillic:
        is_ok = True
    return is_ok # повертаємо значення чи пароль задовільнив парольну політику

def check_user_for_password_constraints(username): #перевірка чи на юзера накладені парольні обмеження
    is_pass_constraints_exist = False
    if check_if_user_already_exist(username) == True:
        df = read_csv_to_dataframe()
        index = find_row_index(df, 'username', username)
        const = get_dataframe_value(df, 'is_passwd_policy_exist', index)
        if const == True:
            is_pass_constraints_exist = True
        else:
            is_pass_constraints_exist = False
        return is_pass_constraints_exist #Повертає тру або фолс в залежності чи є обмеження

def dispaly_info():
    #Функція виводу інформації про Програму
    print("Довідка: ")
    print("Автор - ФБ-05 Супрун Максим")
    print("Варант 19: Наявність рядкових і прописних латинських букв, цифр і символів кирилиці.")


