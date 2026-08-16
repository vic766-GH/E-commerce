import json
import os

from src.classes_create import Category, Product


def get_data_json(path: str) -> list:
    """Функция чтения данных из json-файла"""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def product_by_categories(data: list) -> list:
    """Функция преобразования списка словарей продуктов по категориям в список объектов класса"""
    categories = []
    for category in data:
        product_lists = []
        for product in category["products"]:
            product_lists.append(Product(**product))
        category["products"] = product_lists
        categories.append(Category(**category))
    return categories
