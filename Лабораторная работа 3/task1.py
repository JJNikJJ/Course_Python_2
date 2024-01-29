class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive integer.")
        self._pages = value

    def __str__(self):
        return super().__str__() + f". Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Duration must be a positive number.")
        self._duration = value

    def __str__(self):
        return super().__str__() + f". Продолжительность: {self.duration} часов"


if __name__ == "__main__":
    paper_book = PaperBook("Грозовой перевал", "Эмили Бронте", 416)
    audio_book = AudioBook("Атлант расправил плечи", "Айн Рэнд", 65.5)

    print(paper_book)
    print(audio_book)
