# en_dict = '/dictionaries/english_noun.txt'
# ee_dict = '/dictionaries/estonian_nouns.txt'
# ru_dict = '/dictionaries/russian_nouns.txt'


# Проверка в словаре 
def word_in_dict_control(word, lang):
    d = " "
    if lang == "Estonian":
        d = "./dictionaries/estonian_nouns.txt"
    elif lang == "Russian":
        d = "./dictionaries/russian_nouns.txt"
    else:
        d = "./dictionaries/english_nouns.txt"

    with open(d, 'r', encoding="utf-8") as your_dict: # открываем файл на чтение
        words = your_dict.readlines()    # читаем файл построчно и делаем массив строк
    w = 0
    for line in words:
        if line.strip('\n') == word: # проверяем есть ли слово в словаре, удаляем из слов в словаре перенос строки
            print(f'Grats')
            w += 1
            return True
    if w == 0:
        print(f"Sorry {word}")
        return False

