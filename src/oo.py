class Student:
    def __init__(self, name: str, gpa: float, year: int):
        if not name:
            raise ValueError("Имя не может быть пустым")
        if not (0.0 <= gpa <= 5.0):
            raise ValueError("GPA должен быть от 0 до 5")
        self._name = name
        self._gpa = gpa
        self._year = year

    @property
    def name(self):
        return self._name

    @property
    def gpa(self):
        return self._gpa

    def __str__(self):
        return f"{self._name}, курс {self._year}, GPA: {self._gpa}"


class MasterStudent(Student):
    def __init__(self, name, gpa, year, thesis_topic, supervisor):
        super().__init__(name, gpa, year)
        if not isinstance(thesis_topic, str):
            raise TypeError("тема диплома должна быть строкой")
        if not isinstance(supervisor, str):
            raise TypeError("научный руководитель должен быть строкой")
        self._thesis_topic = thesis_topic
        self._supervisor = supervisor

    @property
    def thesis_topic(self):
        return self._thesis_topic

    @property
    def supervisor(self):
        return self._supervisor

    def get_status(self):
        return f"магистрант: {self.name}, тема: {self.thesis_topic}"

    def __str__(self):
        return super().__str__() + f", тема диплома: {self._thesis_topic}"


"""
принцип SRP заключается в том,, что для каждой логики в коде
должны быть разные функции, тк  в дальнейшем при переиспользовании легче 
использовать метод который отвечает за чтото одно, 
а не изменяет сразу несколько параметров 
например нарушение SRP: если функция обработки обращений будет сортировать их, перенапрявлять для ответа и отправлять ответ.
если через время изменятся условия сортировки, то иизменяя можно случайно сломать отправку ответа.
для исправления нужно разделить это всё на 3 функции и всё будет замечательно.
"""
