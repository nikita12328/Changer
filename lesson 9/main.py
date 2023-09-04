import random

from csv_generator import generate_csv_file
from decorators import save_to_json, quadratic_equation_solver_decorator


@quadratic_equation_solver_decorator
@save_to_json("quadratic_equation_results.json")
def process_csv(input_filename, output_filename):
    pass


if __name__ == "__main__":
    input_filename = "random_data.csv"
    output_filename = "roots_data.csv"
    num_rows = random.randint(100, 1000)

    generate_csv_file(input_filename, num_rows)
    print(f"Сгенерирован CSV файл '{input_filename}' с {num_rows} строками.")

    process_csv(input_filename, output_filename)
    print(f"Результаты записаны в файл '{output_filename}' и в JSON файл 'quadratic_equation_results.json'.")
