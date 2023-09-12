class Matrix:
    """
    Класс для работы с матрицами.
    """

    def __init__(self, rows, cols):
        """
        Инициализирует матрицу с заданным числом строк и столбцов.

        :param rows: Количество строк в матрице.
        :param cols: Количество столбцов в матрице.
        """
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        :return: Строковое представление матрицы.
        """
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        """
        Сравнивает текущую матрицу с другой матрицей.

        :param other: Другая матрица для сравнения.
        :return: True, если матрицы равны, иначе False.
        """
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        """
        Выполняет сложение двух матриц.

        :param other: Другая матрица для сложения.
        :return: Новая матрица, являющаяся результатом сложения.
        :raises ValueError: Если размеры матриц не совпадают.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must be the same for addition")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        """
        Выполняет умножение двух матриц.

        :param other: Другая матрица для умножения.
        :return: Новая матрица, являющаяся результатом умножения.
        :raises ValueError: Если размеры матриц не совпадают.
        """
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


if __name__ == '__main__':
    # Пример использования класса Matrix:
    matrix1 = Matrix(2, 2)
    matrix1.data = [[1, 2], [3, 4]]

    matrix2 = Matrix(2, 2)
    matrix2.data = [[5, 6], [7, 8]]

    print("Matrix 1:")
    print(matrix1)

    print("Matrix 2:")
    print(matrix2)

    print("Matrix 1 == Matrix 2:", matrix1 == matrix2)

    matrix3 = matrix1 + matrix2
    print("Matrix 1 + Matrix 2:")
    print(matrix3)

    matrix4 = Matrix(2, 3)
    matrix4.data = [[1, 2, 3], [4, 5, 6]]

    matrix5 = Matrix(3, 2)
    matrix5.data = [[7, 8], [9, 10], [11, 12]]

    matrix6 = matrix4 * matrix5
    print("Matrix 4 * Matrix 5:")
    print(matrix6)
