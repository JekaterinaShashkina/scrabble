# Проверка в словаре 
def word_in_dict_control(word):
    with open('./dictionaries/english_noun.txt', 'r') as en_dict: # открываем файл на чтение
        words = en_dict.readlines()    # читаем файл построчно и делаем массив строк
    w = 0
    for line in words:
        if line.strip('\n') == word: # проверяем есть ли слово в словаре, удаляем из слов в словаре перенос строки
            print(f'Grats')
            w += 1
            return True
    if w == 0:
        print(f"Sorry {word}")
        return False

# word_in_dict_control("river")