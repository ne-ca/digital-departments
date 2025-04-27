import doctest


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title:
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        if not author:
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def open_page(self, page_number: int) -> str:
        """
        Открытие книги на определенной странице.

        :param page_number: Номер страницы
        :raise ValueError: Если номер страницы выходит за пределы книги
        :return: Содержимое страницы (заглушка)

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.open_page(100)
        """
        if not isinstance(page_number, int):
            raise TypeError("Номер страницы должен быть типа int")
        if page_number <= 0 or page_number > self.pages:
            raise ValueError("Номер страницы вне допустимого диапазона")
        ...

    def get_book_info(self) -> dict:
        """
        Получение информации о книге.

        :return: Словарь с информацией о книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_book_info()
        """
        ...


class Smartphone:
    def __init__(self, brand: str, model: str, battery_level: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param battery_level: Уровень заряда батареи (в процентах)

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 13", 80)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть типа str")
        if not brand:
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        if not model:
            raise ValueError("Модель не может быть пустой")
        self.model = model

        if not isinstance(battery_level, int):
            raise TypeError("Уровень заряда должен быть типа int")
        if battery_level < 0 or battery_level > 100:
            raise ValueError("Уровень заряда должен быть в диапазоне 0-100%")
        self.battery_level = battery_level

    def charge(self, percent: int) -> None:
        """
        Зарядка смартфона.

        :param percent: Процент, на который увеличивается заряд
        :raise ValueError: Если процент выходит за допустимые границы

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 13", 80)
        >>> phone.charge(20)
        """
        if not isinstance(percent, int):
            raise TypeError("Процент должен быть типа int")
        if percent <= 0:
            raise ValueError("Процент должен быть положительным числом")
        ...

    def make_call(self, number: str) -> bool:
        """
        Совершение звонка.

        :param number: Номер телефона
        :return: Успешность звонка
        :raise ValueError: Если номер не соответствует формату

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 13", 80)
        >>> phone.make_call("+1234567890")
        """
        if not isinstance(number, str):
            raise TypeError("Номер должен быть типа str")
        if not number.startswith("+"):
            raise ValueError("Номер должен начинаться с '+'")
        ...


class Tree:
    def __init__(self, species: str, age: int, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param age: Возраст дерева (в годах)
        :param height: Высота дерева (в метрах)

        Примеры:
        >>> tree = Tree("Oak", 50, 25.5)  # инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть типа str")
        if not species:
            raise ValueError("Вид дерева не может быть пустым")
        self.species = species

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def grow(self, years: int) -> None:
        """
        Рост дерева с течением времени.

        :param years: Количество лет для роста
        :raise ValueError: Если количество лет отрицательное

        Примеры:
        >>> tree = Tree("Oak", 50, 25.5)
        >>> tree.grow(10)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть типа int")
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным числом")
        ...

    def get_info(self) -> dict:
        """
        Получение информации о дереве.

        :return: Словарь с информацией о дереве

        Примеры:
        >>> tree = Tree("Oak", 50, 25.5)
        >>> tree.get_info()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации