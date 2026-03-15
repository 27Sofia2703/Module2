class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self._brand = brand
        self._model = model
        self._year = year

    def get_info(self) -> str:
        """
        Получить информацию о транспортном средстве.
        """
        return f"{self._year} {self._brand} {self._model}"

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.
        """
        return self.get_info()

    def __repr__(self) -> str:
        """
        Возвращает неформальное строковое представление транспортного средства.
        """
        return f"Vehicle(brand={self._brand}, model={self._model}, year={self._year})"


class Car(Vehicle):
    """
    Класс для легковых автомобилей, наследуется от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        :param brand: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в легковом автомобиле.
        """
        super().__init__(brand, model, year)
        self._doors = doors

    def get_info(self) -> str:
        """
        Получить информацию о легковом автомобиле.

        Переопределяет метод родительского класса для добавления информации о количестве дверей.
        """
        return f"{super().get_info()}, Doors: {self._doors}"

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.

        Переопределяет метод родительского класса для включения информации о количестве дверей.
        """
        return f"Car: {super().__str__()}"

    def __repr__(self) -> str:
        """
        Возвращает неформальное строковое представление легкового автомобиля.

        Переопределяет метод родительского класса для включения информации о количестве дверей.
        """
        return f"Car(brand={self._brand}, model={self._model}, year={self._year}, doors={self._doors})"


class Truck(Vehicle):
    """
    Класс для грузовых автомобилей, наследуется от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        :param brand: Марка грузового автомобиля.
        :param model: Модель грузового автомобиля.
        :param year: Год выпуска грузового автомобиля.
        :param capacity: Грузоподъемность грузового автомобиля (в тоннах).
        """
        super().__init__(brand, model, year)
        self._capacity = capacity

    def get_info(self) -> str:
        """
        Получить информацию о грузовом автомобиле.

        Переопределяет метод родительского класса для добавления информации о грузоподъемности.
"""
        return f"{super().get_info()}, Capacity: {self._capacity} tons"

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.

        Переопределяет метод родительского класса для включения информации о грузоподъемности.
        """
        return f"Truck: {super().__str__()}"

    def __repr__(self) -> str:
        """
        Возвращает неформальное строковое представление грузового автомобиля.

        Переопределяет метод родительского класса для включения информации о грузоподъемности.
        """
        return f"Truck(brand={self._brand}, model={self._model}, year={self._year}, capacity={self._capacity})"


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, 4)
    truck = Truck("Volvo", "FH", 2019, 18.0)

    print(car)
    print(repr(car))
    print(truck)
    print(repr(truck))
    # Write your solution here
    pass
