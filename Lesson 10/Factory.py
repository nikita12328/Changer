from 1.Person import Person
from 1.Animal import Animal
from 1.Circle import Circle
from 1.Worker import Employee
from 1.Fish import Fish


class Factory:
    @staticmethod
    def create_instance(class_type, *args, **kwargs):
        if class_type == 'Person':
            return Person(*args, **kwargs)
        elif class_type == 'Animal':
            return Animal(*args, **kwargs)
        elif class_type == 'Circle':
            return Circle(*args, **kwargs)
        elif class_type == 'Employee':
            return Employee(*args, **kwargs)
        elif class_type == 'Fish':
            return Fish(*args, **kwargs)
        else:
            raise ValueError(f"Unknown class type: {class_type}")


if __name__ == '__main__':
    person = Factory.create_instance('Person', 'John', 'Doe', 'Smith', 30)
    animal = Factory.create_instance('Animal', 50, 100, True)
    circle = Factory.create_instance('Circle', 5.0)
    worker = Factory.create_instance('Employee', "Константин", "Ситников", "Ситников", 29, 12345)
    fish = Factory.create_instance('Fish', 5, 6, False, 'desc.')
