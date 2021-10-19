from pprint import pprint
import os


def create_cook_book_task1():
    path = os.path.join(os.getcwd(), 'recipes.txt')

    with open(path, encoding="utf-8") as file:
        result = {}
        for dish in file:
            dish_name = dish.strip()
            counter = int(file.readline().strip())
            temp_data = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_data.append(
                    {"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "measure": measure.strip()}
                )
            result[dish_name] = temp_data
            file.readline()
        return result


def get_shop_list_by_dishes_task2(dishes, person_count):
    result_dict = {}
    quantity_dict = {}
    for dish in dishes:
        if dish in quantity_dict.keys():
            quantity_dict[dish] += 1
        else:
            quantity_dict[dish] = 1
    for name_dish, value in quantity_dict.items():
        for ingredient_dict in cook_book[name_dish]:
            if not (ingredient_dict["ingredient_name"] in result_dict.keys()):
                temp_dict = \
                    {
                        "measure": ingredient_dict["measure"],
                        "quantity": ingredient_dict["quantity"] * value * person_count
                    }
                result_dict[ingredient_dict["ingredient_name"]] = temp_dict
            else:
                result_dict[ingredient_dict["ingredient_name"]]["quantity"] += ingredient_dict[
                                                                                   "quantity"] * value * person_count
    return result_dict


cook_book = create_cook_book_task1()
random = get_shop_list_by_dishes_task2(['Запеченный картофель', 'Омлет'], 2)
pprint(cook_book)
print()
pprint(random)
