def read_file(file_):
    lines_ = []
    for line in file_:
        lines_.append(line.strip())
    return lines_


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ing_all_params in cook_book[dish]:
                if ing_all_params['ingredient_name'] in result:
                    result[ing_all_params['ingredient_name']]['quantity'] += ing_all_params['quantity'] * person_count
                else:
                    result[ing_all_params['ingredient_name']] = {'quantity': ing_all_params['quantity'] * person_count, 'measure': ing_all_params['measure']}
        else:
            print(f'блюдо {dish} не найдено в рцептах!\n')
    return result


cook_book = {}
lines = read_file(open('recipes.txt', 'r', encoding='utf-8'))

current_dish_ing_quantity = 0
current_dish_quantity = 0

cook_book[lines[0]] = []
current_dish_ing_quantity = int(lines[1])
current_dish_str = 0

for i in range(len(lines) - 3):
    if i == current_dish_str + current_dish_ing_quantity + 3 or i == 0:
        cook_book[lines[i]] = []
        current_dish_ing_quantity = int(lines[i + 1])
        for j in range(i + 2, i + 2 + current_dish_ing_quantity):
            ing_list = lines[j].split('|')
            current_ing_dict = {'ingredient_name': ing_list[0].strip(), 'quantity': int(ing_list[1]), 'measure': ing_list[2].strip()}
            cook_book[lines[i]].append(current_ing_dict)
        current_dish_str = i

res = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for ing in res:
    print(f'{ing}: {res[ing]}')
