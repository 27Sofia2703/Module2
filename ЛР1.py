# TODO Написать 3 класса с документацией и аннотацией типов


class MusicalInstrument:
    """
    Абстрактный класс, описывающий музыкальный инструмент.
    """

    def __init__(self, name: str, num_strings: int, weight_kg: float):
        """
        Инициализация музыкального инструмента.

        :param name: Название инструмента.
        :param num_strings: Количество струн (0 для бесструнных инструментов).
        :param weight_kg: Вес инструмента в килограммах.

        :raises ValueError: Если параметры не удовлетворяют ограничениям.

        >>> guitar = Guitar("Classical", 6, 2.5)  # Дочерний класс
        >>> guitar.name
        """
        if not name.strip():
            raise ValueError("Название инструмента не может быть пустым")
        if num_strings < 0:
            raise ValueError("Количество струн не может быть отрицательным")
        if weight_kg <= 0:
            raise ValueError("Вес инструмента должен быть положительным")

        self.name = name
        self.num_strings = num_strings
        self.weight_kg = weight_kg
        self._is_tuned = False

    def play_note(self, note: str, duration: float) -> str:
        """
        Воспроизвести ноту на инструменте.

        :param note: Название ноты (например, 'C', 'D#', 'F').
        :param duration: Длительность ноты в секундах.
        :return: Описание воспроизведенной ноты.

        >>> guitar = Guitar("Classical", 6, 2.5)  # Дочерний класс
        >>> sound = guitar.play_note("A", 1.5)
        >>> "A" in sound
        """
    def tune_instrument(self, reference_frequency: float = 440.0) -> bool:
        """
        Настроить инструмент.

        :param reference_frequency: Эталонная частота для настройки (Гц).
        :return: True, если инструмент успешно настроен, иначе False.

        >>> guitar = Guitar("Classical", 6, 2.5)  # Дочерний класс
        >>> guitar.tune_instrument(440.0)
        True
        >>> guitar._is_tuned
        """

    def get_available_notes(self) -> List[str]:
        """
        Получить список доступных нот для инструмента.

        :return: Список названий нот.

        >>> guitar = Guitar("Classical", 6, 2.5)  # Дочерний класс
        >>> notes = guitar.get_available_notes()
        >>> len(notes) > 0
        True
        """


class SocialNetwork:
    """
    Абстрактный класс, описывающий социальную сеть.
    """

    def __init__(self, name: str, max_friends: int, is_public: bool):
        """
        Инициализация социальной сети.

        :param name: Название социальной сети.
        :param max_friends: Максимальное количество друзей/подписчиков.
        :param is_public: Публичная ли сеть (True) или закрытая (False).

        :raises ValueError: Если параметры не удовлетворяют ограничениям.

        >>> network = SocialNetworkImpl("MyNetwork", 5000, True)  # Дочерний класс
        >>> network.name
        """
        if not name.strip():
            raise ValueError("Название социальной сети не может быть пустым")
        if max_friends < 0:
            raise ValueError("Максимальное количество друзей не может быть отрицательным")

        self.name = name
        self.max_friends = max_friends
        self.is_public = is_public
        self._users_count = 0

    def add_friend(self, user_id: str, friend_id: str) -> bool:
        """
        Добавить друга/подписчика.

        :param user_id: Идентификатор пользователя, который добавляет друга.
        :param friend_id: Идентификатор друга для добавления.
        :return: True, если друг успешно добавлен, иначе False.

        >>> network = SocialNetworkImpl("MyNetwork", 5000, True)  # Дочерний класс
        >>> network.add_friend("user123", "friend456")
        """

    def create_post(self, user_id: str, content: str, privacy: str) -> str:
        """
        Создать новый пост.

        :param user_id: Идентификатор пользователя, создающего пост.
        :param content: Текст поста.
        :param privacy: Уровень приватности ('public', 'friends', 'private').
        :return: Идентификатор созданного поста.

        >>> network = SocialNetworkImpl("MyNetwork", 5000, True)  # Дочерний класс
        >>> post_id = network.create_post("user123", "Hello world!", "public")
        >>> len(post_id) > 0
        """

    def get_feed(self, user_id: str, limit: int = 10) -> List[str]:
        """
        Получить ленту новостей пользователя.

        :param user_id: Идентификатор пользователя.
        :param limit: Максимальное количество постов в ленте.
        :return: Список идентификаторов постов.

        >>> network = SocialNetworkImpl("MyNetwork", 5000, True)  # Дочерний класс
        >>> feed = network.get_feed("user123", 5)
        >>> isinstance(feed, list)
        """


class StorageDevice:
    """
    Абстрактный класс, описывающий устройство хранения данных.
    """

    def __init__(self, capacity_gb: float, read_speed_mbs: float, write_speed_mbs: float):
        """
        Инициализация устройства хранения данных.

        :param capacity_gb: Объем памяти в гигабайтах. Должен быть положительным числом.
        :param read_speed_mbs: Скорость чтения в МБ/с. Должна быть неотрицательной.
        :param write_speed_mbs: Скорость записи в МБ/с. Должна быть неотрицательной.

        :raises ValueError: Если параметры не удовлетворяют ограничениям.

        >>> hdd = HardDiskDrive(1000, 150, 120)  # Дочерний класс
        >>> hdd.capacity_gb
        """
        if capacity_gb <= 0:
            raise ValueError("Емкость устройства должна быть положительной")
        if read_speed_mbs < 0 or write_speed_mbs < 0:
            raise ValueError("Скорости чтения и записи не могут быть отрицательными")

        self.capacity_gb = capacity_gb
        self.read_speed_mbs = read_speed_mbs
        self.write_speed_mbs = write_speed_mbs
        self._used_space_gb = 0.0

    def store_data(self, data_size_gb: float, filename: str) -> bool:
        """
        Записать данные на устройство.

        :param data_size_gb: Размер данных в гигабайтах для записи.
        :param filename: Имя файла для сохранения.
        :return: True, если данные успешно записаны, иначе False.

        >>> hdd = HardDiskDrive(500, 100, 80)  # Дочерний класс
        >>> hdd.store_data(50, "backup.zip")
        """

    def read_data(self, filename: str) -> Optional[bytes]:
        """
        Прочитать данные с устройства.

        :param filename: Имя файла для чтения.
        :return: Данные в виде байтов или None, если файл не найден.

        >>> hdd = HardDiskDrive(500, 100, 80)  # Дочерний класс
        >>> data = hdd.read_data("backup.zip")
        >>> data is None or isinstance(data, bytes)
        """

    def format_device(self) -> None:
        """
        Отформатировать устройство (очистить все данные).

        >>> hdd = HardDiskDrive(500, 100, 80)  # Дочерний класс
        >>> hdd.format_device()
        >>> hdd._used_space_gb == 0
        True
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
