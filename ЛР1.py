# TODO Написать 3 класса с документацией и аннотацией типов


class Furniture:
    def __init__(self, material: str, color: str):
        """
        Класс, описывающий мебель.

        :param material: Материал, из которого изготовлена мебель. Не должен быть пустым.
        :param color: Цвет мебели. Не должен быть пустым.

        :raises ValueError: Если material или color пустые строки.
        """
        if not material or not color:
            raise ValueError("Material and color must not be empty.")

        self.material = material
        self.color = color

    def use(self) -> str:
        """Определяет, как использовать мебель."""

    def clean(self) -> str:
        """Определяет, как чистить мебель."""


class Plant:
    def __init__(self, species: str, height: float):
        """
        Конструктор класса растений.

        :param species: Вид растения. Не должен быть пустым.
        :param height: Высота растения в сантиметрах. Должна быть положительным числом.

        :raises ValueError: Если species пустая строка или height не положительное число.
        """
        if not species or height <= 0:
            raise ValueError("Species must not be empty and height must be positive.")

        self.species = species
        self.height = height

    def water(self) -> str:
        """Определяет, как поливать растение."""

    def prune(self) -> str:
        """Определяет, как обрезать растение."""


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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
