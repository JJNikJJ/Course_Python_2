import doctest


class Car:
    """
    Класс, описывающий объект "Автомобиль".

    Атрибуты:
    1. brand (str): Марка автомобиля.
    2. fuel_type (str): Тип топлива автомобиля.

    Методы:
    1. start_engine(self) -> str:
        Запускает двигатель автомобиля.
        >>> car = Car(brand="Toyota", fuel_type="Бензин")
        >>> car.start_engine()
        'Двигатель автомобиля Toyota запущен.'

    2. drive(self, distance: float) -> str:
        Производит поездку на указанное расстояние.
        >>> car = Car(brand="Toyota", fuel_type="Бензин")
        >>> car.drive(50.5)
        'Автомобиль Toyota проехал 50.5 километров.'
    """

    def __init__(self, brand: str, fuel_type: str):
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Марка автомобиля должна быть непустой строкой.")
        self.brand = brand

        if not isinstance(fuel_type, str) or not fuel_type.strip():
            raise ValueError("Тип топлива должен быть непустой строкой.")
        self.fuel_type = fuel_type

    def start_engine(self) -> str:
        return f"Двигатель автомобиля {self.brand} запущен."

    def drive(self, distance: float) -> str:
        return f"Автомобиль {self.brand} проехал {distance} километров."


class Smartphone:
    """
    Класс, описывающий объект "Смартфон".

    Атрибуты:
    1. model (str): Модель смартфона.
    2. os (str): Операционная система смартфона.

    Методы:
    1. make_call(self, number: str) -> str:
        Выполняет звонок по указанному номеру.
        >>> smartphone = Smartphone(model="iPhone", os="iOS")
        >>> smartphone.make_call("123-456-7890")
        'Вызов номера 123-456-7890 с использованием смартфона iPhone.'

    2. send_message(self, recipient: str, message: str) -> str:
        Отправляет сообщение указанному получателю.
        >>> smartphone = Smartphone(model="iPhone", os="iOS")
        >>> smartphone.send_message("John", "Привет!")
        'Отправка сообщения John с смартфона iPhone: Привет!'
    """

    def __init__(self, model: str, os: str):
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Модель смартфона должна быть непустой строкой.")
        self.model = model

        if not isinstance(os, str) or not os.strip():
            raise ValueError("Операционная система смартфона должна быть непустой строкой.")
        self.os = os

    def make_call(self, number: str) -> str:
        return f"Вызов номера {number} с использованием смартфона {self.model}."

    def send_message(self, recipient: str, message: str) -> str:
        return f"Отправка сообщения {recipient} с смартфона {self.model}: {message}"


class Animal:
    """
    Класс, описывающий объект "Животное".

    Атрибуты:
    1. species (str): Вид животного.
    2. sound (str): Звук, издаваемый животным.

    Методы:
     1. make_sound(self) -> str:
        Издает звук.
        >>> animal = Animal(species="Собака", sound="Лай")
        >>> animal.make_sound()
        'Собака издаёт звук: Лай.'

    2. sleep(self) -> str:
        Животное засыпает.
        >>> animal = Animal(species="Собака", sound="Лай")
        >>> animal.sleep()
        ' Собака спит.'
    """

    def __init__(self, species: str, sound: str):
        if not isinstance(species, str) or not species.strip():
            raise ValueError("Вид животного должен быть непустой строкой.")
        self.species = species

        if not isinstance(sound, str) or not sound.strip():
            raise ValueError("Звук животного должен быть непустой строкой.")
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.species} издаёт звук: {self.sound}."

    def sleep(self) -> str:
        return f" {self.species} спит."


if __name__ == "__main__":
    doctest.testmod()
