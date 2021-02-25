cook_book = {}


def with_file(filename):
    # функция получение из файла, словаря
    with open(filename, encoding='utf-8') as f:
        for line in f:
            cook_name = line.strip()
            cook_counter = int(f.readline())
            ingridient = []
            for item in range(cook_counter):
                ingridient_list = f.readline().strip().split(' | ')
                ingridient_dict = {
                    'ingredient_name': ingridient_list[0],
                    'quantity': int(ingridient_list[1]),
                    'measure': ingridient_list[2]
                }
                ingridient.append(ingridient_dict)
            cook_book[cook_name] = ingridient
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    # функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
    if dishes:
        if person_count >= 1:
            for cook_name_key, item_cook_value in cook_book.items():
                if cook_name_key in dishes:
                    for item_ingridient in item_cook_value:
                        print(f"'{item_ingridient['ingredient_name']}': "
                              f"{{'measure: '{item_ingridient['measure']}', "
                              f"'quantity': {int(item_ingridient['quantity']) * person_count}}},")
        else:
            print(f"Укажите корректное количество персон, у вас {person_count}")
    else:
        print(f"Введите блюдо, у вас {dishes}")


def sorted_files(files):
    count_list = []
    for item_file in files:
        with open(item_file, encoding='utf-8') as fl:
            text = fl.readlines()
            len_text = len(text)
            name = fl.name
            count_list.append([text, name, len_text])
    count_list.sort(reverse=True)

    with open("out/text.txt", "w", encoding='utf-8') as ff:
        for item in count_list[:]:
            new_path = item[1].replace("source/", "")
            ff.write(new_path + "\n")
            ff.write(str(item[2]) + "\n")
            for j in item[0]:
                ff.write(j.strip() + "\n")
    print("файл сохранен /out/text.txt")
