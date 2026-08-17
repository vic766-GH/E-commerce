from pathlib import Path

from src.read_products_json import get_data_json, product_by_categories


# Тестирование инициализации класса "Продукты"
def test_product_init(product_true_1):
    assert product_true_1.name == "Samsung Galaxy S23 Ultra"
    assert product_true_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_true_1.price == 180000.0
    assert product_true_1.quantity == 5


# Тестирование инициализации класса "Категории" для одной категории товаров
def test_category_init_1(category_true_1):
    assert category_true_1.name == "Смартфоны"
    assert category_true_1.description == (
        "Смартфоны, как средство не только коммуникации, но и получение"
        " дополнительных функций для удобства жизни"
    )
    assert len(category_true_1.products) == 3
    assert category_true_1.product_count == 3
    assert category_true_1.category_count == 1


# Тестирование получения списка словарей товаров по категориям из json-файла
def test_get_data_json():
    path_0 = str(Path.cwd())[-6:]
    if path_0 == "\\tests":
        path_1 = "../data/products.json"
    else:
        path_1 = "data/products.json"
    in_json = get_data_json(path_1)
    category_quantity = len(in_json)
    assert category_quantity == 2


# Тестирование преобразования списка объектов класса "Категории" из списка словарей
def test_product_by_categories(indata):
    data_object = product_by_categories(indata)
    assert len(data_object) == 2
    assert data_object[0].name == "Смартфоны"
    assert data_object[1].name == "Телевизоры"
