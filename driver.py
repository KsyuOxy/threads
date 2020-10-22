class TXTDriver:
    def __init__(self, path):
        self.__path = path

    def get_nums(self) -> list:  # ->  получает числа из файла
        with open(self.__path, 'r', encoding='utf-8') as f:  # ->
            result = f.read().split()  # ->
            return result

    def get_negative(self) -> list:  # -> выбирает отрицательные
        negative = [num for num in self.get_nums() if '-' in num]
        return negative

    def get_positive(self) -> list:  # ->  # -> выбирает положительные
        positive = [num for num in self.get_nums() if '-' not in num]
        return positive
