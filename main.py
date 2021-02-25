import modules.functions_files as functions
file_name = 'source/recipes.txt'

print(functions.with_file(file_name))
functions.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
functions.sorted_files(['source/1.txt', 'source/2.txt', 'source/3.txt'])