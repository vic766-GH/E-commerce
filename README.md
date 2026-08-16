# <font size="6">E-commerce </font><font size="4"><span style="color: green">***(подготовка ядра для интернет-магазина)***</font>
<span style="color: orange">Репозиторий проекта на GitHub  
- на стадии разработки</font> (https://github.com/vic766-GH/E-commerce/tree/develop)

<span style="color: orange">Установленные зависимости приведены в </font>[<font size="3"><span style="color: SkyBlue">**<u>requirements.
txt</u>**</font>](requirements.txt)
###
### <font size="5"><u>Модули:</u></font>

<span style="color: orange">Проверка работоспособности модулей выполняется запуском модуля [<font size="4"><span style="color: SkyBlue"><u>***main.
py</u>***</font>](main.py) в корневом каталоге проекта</font>

[<span style="color: white">1. </font> <font size="4"><span style="color: SkyBlue"><u>classes_create.
py:</u></font>](src/classes_create.py)

<font size="3">**class Product:**</font>
    - класс «Продукты» описывает характеристики продукта.

<font size="3">**class Category:**</font>
    - класс «Категории» описывает список товаров.

[<font size="4"><span style="color: white">2. <span style="color: SkyBlue"><u>read_products_json.py:</u></font>](src/read_products_json.py)

<font size="3">**get_data_json**(path: str) -> list:</font>
    - Функция чтения данных из json-файла

<font size="3">**product_by_categories**(data: list) -> list:</font>
    - Функция преобразования списка словарей продуктов по категориям в список объектов класса.
###
### <font size="5"><u>Тестирование</u></font>

[<font size="4"><span style="color: white">1. <span style="color: SkyBlue"><u>conftest.py:</u></font>](tests/conftest.py)
Содержит фикстуры, необходимые для проведения тестов

[<font size="4"><span style="color: white">2. <span style="color: SkyBlue"><u>test_classes_create.py:</u></font>](tests/test_classes_create.py)

- Тестирование инициализации класса "Продукты"
- Тестирование инициализации класса "Категории" для одной категории товаров
- Тестирование инициализации класса "Категории" для двух категорий товаров
- Тестирование получения списка словарей товаров по категориям из json-файла
- Тестирование преобразования списка объектов класса "Категории" из списка словарей
