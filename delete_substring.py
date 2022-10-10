# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def create_file(text):
    """Принимает текст и создаёт файл с этим текстом.
    """
    name = input('Задайте путь к файлу: ')
    with open(name, 'a') as f:
        f.writelines(text)
        

def read_file(name):
    """Принимает путь к файлу и
    читает его содержимое
    """
    with open(name, 'r') as f:
        f_string = f.read()
    return f_string   
        
 
def delete_substr(user_str, sub_str):
    """Принимает исходную строку и подстроку удаления.
    Возвращает строку без подстроки.
    """
    edit_str = user_str.replace(sub_str, '')
    return edit_str
    
                
# user_string = input('Введите текст: \n')
# create_file(user_string)    

input_string = read_file('qwerty.txt')
print('Входная строка: ', input_string)

sub_string = input('Введите подстоку для удаления: ')

if sub_string not in input_string:
    print('Нет такой подстроки')
else:    
    edit_string = delete_substr(input_string, sub_string)
    print(edit_string)
    create_file(edit_string)
    