# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC


class Tree(ABC):
    def __init__(self, height: float, age: int, tree_type: str):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах
        :param tree_type: Вид дерева

        Примеры:
        >>> tree = Tree(10.5, 25, "Дуб")  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = float(height)

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть типа int")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным")
        self.age = age

        if not isinstance(tree_type, str):
            raise TypeError("Вид дерева должен быть типа str")
        if not tree_type.strip():
            raise ValueError("Вид дерева не может быть пустой строкой")
        self.tree_type = tree_type.strip()

    def grow(self, growth_per_year: float) -> float:
        """
        Рост дерева за год.

        :param growth_per_year: Прирост высоты за год в метрах
        :return: Новая высота дерева

        Примеры:
        >>> tree = Tree(10.5, 25, "Дуб")
        >>> tree.grow(0.5)  # doctest: +SKIP
        11.0
        """

    def estimate_wood_volume(self) -> float:
        """
        Оценка объема древесины в дереве.

        :return: Оценочный объем древесины в кубических метрах

        Примеры:
        >>> tree = Tree(10.5, 25, "Дуб")
        >>> tree.estimate_wood_volume()  # doctest: +SKIP
        15.75
        """

    def is_fruit_tree(self) -> bool:
        """
        Проверка, является ли дерево плодовым.

        :return: True если дерево плодовое, False в противном случае

        Примеры:
        >>> tree = Tree(10.5, 25, "Дуб")
        >>> tree.is_fruit_tree()  # doctest: +SKIP
        False
        """


class Smartphone(ABC):
    def __init__(self, brand: str, battery_capacity: int, storage_gb: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param battery_capacity: Емкость аккумулятора в мАч
        :param storage_gb: Объем встроенной памяти в ГБ

        Примеры:
        >>> phone = Smartphone("Apple", 4000, 128)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть типа str")
        if not brand.strip():
            raise ValueError("Бренд не может быть пустой строкой")
        self.brand = brand.strip()

        if not isinstance(battery_capacity, int):
            raise TypeError("Емкость аккумулятора должна быть типа int")
        if battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным числом")
        self.battery_capacity = battery_capacity

        if not isinstance(storage_gb, int):
            raise TypeError("Объем памяти должен быть типа int")
        if storage_gb <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")
        self.storage_gb = storage_gb

    def make_call(self, phone_number: str, duration_minutes: int) -> bool:
        """
        Совершение телефонного звонка.

        :param phone_number: Номер телефона для звонка
        :param duration_minutes: Продолжительность звонка в минутах
        :return: True если звонок успешно совершен, False в противном случае

        Примеры:
        >>> phone = Smartphone("Apple", 4000, 128)
        >>> phone.make_call("+79001234567", 10)  # doctest: +SKIP
        True
        """

    def check_battery_level(self) -> float:
        """
        Проверка уровня заряда батареи.

        :return: Уровень заряда в процентах (от 0 до 100)

        Примеры:
        >>> phone = Smartphone("Apple", 4000, 128)
        >>> phone.check_battery_level()  # doctest: +SKIP
        85.5
        """

    def install_app(self, app_name: str, app_size_gb: float) -> bool:
        """
        Установка приложения на смартфон.

        :param app_name: Название приложения
        :param app_size_gb: Размер приложения в ГБ
        :return: True если установка успешна, False в противном случае

        Примеры:
        >>> phone = Smartphone("Apple", 4000, 128)
        >>> phone.install_app("Telegram", 0.5)  # doctest: +SKIP
        True
        """


class BankAccount(ABC):
    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер счета
        :param owner_name: Имя владельца счета
        :param initial_balance: Начальный баланс счета

        Примеры:
        >>> account = BankAccount("40817810099910004312", "Иванов Иван Иванович", 1000.0)
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть типа str")
        if len(account_number) < 5:
            raise ValueError("Номер счета должен содержать минимум 5 символов")
        self.account_number = account_number

        if not isinstance(owner_name, str):
            raise TypeError("Имя владельца должно быть типа str")
        if not owner_name.strip():
            raise ValueError("Имя владельца не может быть пустой строкой")
        self.owner_name = owner_name.strip()

        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Начальный баланс должен быть типа int или float")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.balance = float(initial_balance)

    def deposit(self, amount: float) -> float:
        """
        Внесение денег на счет.

        :param amount: Сумма для внесения
        :return: Новый баланс счета

        Примеры:
        >>> account = BankAccount("40817810099910004312", "Иванов Иван", 1000.0)
        >>> account.deposit(500.0)  # doctest: +SKIP
        1500.0
        """

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия
        :return: Новый баланс счета

        Примеры:
        >>> account = BankAccount("40817810099910004312", "Иванов Иван", 1000.0)
        >>> account.withdraw(300.0)  # doctest: +SKIP
        700.0
        """
    def transfer(self, target_account: 'BankAccount', amount: float) -> bool:
        """
        Перевод денег на другой счет.

        :param target_account: Целевой счет для перевода
        :param amount: Сумма перевода
        :return: True если перевод успешен, False в противном случае

        Примеры:
        >>> account1 = BankAccount("40817810099910004312", "Иванов Иван", 1000.0)
        >>> account2 = BankAccount("40817810099910004313", "Петров Петр", 500.0)
        >>> account1.transfer(account2, 200.0)  # doctest: +SKIP
        True
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
