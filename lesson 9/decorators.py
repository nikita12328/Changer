import csv
import json
import os
from functools import wraps

from quadratic_equation_solver import solve_quadratic_equation


def save_to_json(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            data_to_save = {
                "parameters": {
                    "args": args,
                    "kwargs": kwargs
                },
                "result": result
            }

            with open(filename, 'w') as json_file:
                json.dump(data_to_save, json_file, indent=4)

            return result

        return wrapper

    return decorator


def quadratic_equation_solver_decorator(func):
    def wrapper(input_filename, output_filename):
        try:
            with open(input_filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)

                with open(output_filename, 'w', newline='') as output_file:
                    csv_writer = csv.writer(output_file)

                    for row in csv_reader:
                        if len(row) == 3:
                            a, b, c = map(float, row)
                            roots = solve_quadratic_equation(a, b, c)
                            csv_writer.writerow([a, b, c, *roots])
                        else:
                            print(f"Пропуск строки: {row}")
        except FileNotFoundError:
            print(f"Файл '{input_filename}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")

    return wrapper
