import csv


class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.isalpha() or not value[0].isupper():
            raise ValueError("Invalid name format")
        instance._name = value


class GradeDescriptor:
    def __get__(self, instance, owner):
        return instance._grade

    def __set__(self, instance, value):
        if not (2 <= value <= 5):
            raise ValueError("Grade must be between 2 and 5")
        instance._grade = value


class TestResultDescriptor:
    def __get__(self, instance, owner):
        return instance._test_result

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Test result must be between 0 and 100")
        instance._test_result = value


class Subject:
    def __init__(self):
        self.exam_grade = GradeDescriptor()
        self.test_result = TestResultDescriptor()


class Student:
    name = NameDescriptor()

    def __init__(self, name, surname, patronymic, subjects_file):
        self.name = name
        self._surname = surname
        self._patronymic = patronymic
        self._subjects = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        subjects = set()
        with open(subjects_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row:  # Проверяем, что строка не пустая
                    subject = row[0]
                    subjects.add(subject)
        return subjects

    def __getattr__(self, subject):
        if subject not in self._subjects:
            raise AttributeError(f"{subject} is not a valid subject")
        return Subject()

    def get_subject_average_test_grade(self, subject):
        if subject not in self._subjects:
            raise ValueError(f"{subject} is not a valid subject")
        total_test_results = 0
        total_test_count = 0
        for test_subject, descriptor in self.__dict__.items():
            if isinstance(descriptor, Subject):
                total_test_results += descriptor.test_result
                total_test_count += 1
        if total_test_count == 0:
            return 0  # Если нет предметов с результатами тестов, средний балл 0
        return total_test_results / total_test_count

    def get_overall_average_test_grade(self):
        total_test_results = 0
        total_test_count = 0
        for test_subject, descriptor in self.__dict__.items():
            if isinstance(descriptor, Subject):
                total_test_results += descriptor.test_result
                total_test_count += 1
        if total_test_count == 0:
            return 0  # Если нет предметов с результатами тестов, средний балл 0
        return total_test_results / total_test_count


if __name__ == '__main__':
    student = Student("Иван", "Иванов", "Иванович", "subjects.csv")
    student.math.exam_grade = 4
    student.math.test_result = 85
    print(student.math.exam_grade)
    print(student.math.test_result)
