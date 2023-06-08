import random


class Matrix:
    def __init__(self, num_col: int, num_row: int):
        self.matrix = self.create_new_matrix(num_col, num_row)      #при инициализации класса автоматически создается матрица


    def create_new_matrix(self, num_col: int, num_row: int) -> list:
        """Это метод создает новую матрицу
            arg:    num_col - кол-во столбцов в матрице
                    num_row - кол-во строчек в матрице
            return: готовую матрицу
         """
        matrix = []     #пустой список в который будем добавлять списки для создания матрицы
        for row in range(num_row):
            one_row_list = []   #пустой список в которые мы будем добавлять элементы, является элементом матрицы
            for col in range(num_col):
                one_row_list.append(random.randint(0, 999))     #добавляем в список рандомные числа num_col раз
            matrix.append(one_row_list)     #добавляем в матрицу список созданные в предыдущем цикле
               
        for row in range(num_row):
            print(matrix[row])

        return matrix


    def print_matrix_len(self) -> None:
        """Данные метод выводит длину матрицы"""
        num_row = len(self.matrix)
        num_col = len(self.matrix[0])
        print(f"Число строк матрицы: {num_row}. Число столбцов: {num_col}")

    def change_value(self, num_col: int, num_row: int, new_value: int) -> None:
        """Этот метод заменяет значение в матрице по номеру колонки и строки
            arg:    num_col - столбец в котором требуется замена (делаем минус 1 т.к. нумерация начинается с 0)
                    num_row - строка в которой требуется замена (делаем минус 1 т.к. нумерация начинается с 0)
                    new_value - значение на которое требуется заменить
         """
        try:
            self.matrix[num_row - 1][num_col - 1] = new_value
        except IndexError:
            print("Неверно задан номер колонки и номер строки!")
            

if __name__ == '__main__':
    obj = Matrix(10, 10)
    matrix = obj.matrix
    obj.print_matrix_len()
    obj.change_value(5, 10, 1)