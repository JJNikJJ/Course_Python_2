
class Vehicle:
    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Конструктор базового класса Vehicle.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand: str = brand
        self._model: str = model  # Инкапсулированный атрибут
        self._year: int = year  # Инкапсулированный атрибут
    def start_engine(self) -> None:
        """
        Метод запуска двигателя транспортного средства.
        """
        pass

    def maintenance(self) -> None:
        """
        Регулярное техническое обслуживание.
        """
        pass

    def __str__(self) -> str:
        """
        Метод для представления объекта в виде строки.
        """
        return f"{self._year} {self.brand} {self._model}"

    def __repr__(self) -> str:
        """
        Метод для представления объекта в виде строки при отладке.
        """
        return f"{self.__class__.__name__}({self.brand}, {self._model}, {self._year})"


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, num_doors: int) -> None:
        """
        Конструктор дочернего класса Car.

        :param num_doors: Количество дверей у легкового автомобиля. Инкапсулированный атрибут
        """
        super().__init__(brand, model, year)
        self._num_doors: int = num_doors

    def start_engine(self) -> None:
        """
        Перегруженный метод запуска двигателя для легкового автомобиля.

        Обоснование: Запуск двигателя у легкового автомобиля может включать
        дополнительные шаги.
        """
        pass

    def drive(self) -> None:
        """
        Метод для движения легкового автомобиля.
        """
        pass


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, payload_capacity: float) -> None:
        """
        Конструктор дочернего класса Truck.

        :param payload_capacity: Грузоподъемность грузового автомобиля.
        """
        super().__init__(brand, model, year)
        self.payload_capacity: float = payload_capacity

    def maintenance(self) -> None:
        """
        Перегруженный метод регулярного технического обслуживания грузового автомобиля.

        Обоснование: Грузовой автомобиль может иметь специфичные шаги для
        технического обслуживания, такие как проверка состояния грузового отсека и системы
        перевозки груза.
        """
        pass
    def unload_cargo(self) -> None:
        """
        Метод разгрузки грузового автомобиля.
        """
        pass

    def start_engine(self) -> None:
        """
        Перегруженный метод запуска двигателя для грузового автомобиля.

        Обоснование перегрузки: Запуск двигателя у грузового автомобиля может требовать
        дополнительных проверок состояния двигателя и системы охлаждения.
        """
        pass


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 4)
    truck = Truck("Ford", "F-150", 2022, 2000.0)

    print(car)
    print(truck)
