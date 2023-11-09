# import math
import unittest

from main import CalculateArea

# calculate = CalculateArea()


class TestCalculateArea(unittest.TestCase):

    def test_calculate_area(self):
        call = CalculateArea.calculate_area(1)
        result = 'Площадь круга 6.28'
        self.assertEqual(call, result, 'Функция calculate_area не работает с числами.')

    def test_calculate_area_empty(self):
        call = CalculateArea.calculate_area()
        result = 'Данные не введены или введены неверно. Это должны быть цифры.'
        self.assertEqual(call, result, 'Функция calculate_area неправильно обрабатывает'
                                       'остутствие аргументов.')

    def test_calculate_area_str(self):
        call = CalculateArea.calculate_area('')
        result = 'Неверно введены параметры. Это должны быть цифры.'
        self.assertEqual(call, result, 'Функция calculate_area неправильно обрабатывает строки.')

    def test_calculate_area_kwargs(self):
        call = CalculateArea.calculate_area(a=1)
        result = 'Данные не введены или введены неверно. Это должны быть цифры.'
        self.assertEqual(call, result, 'Функция calculate_area неправильно обрабатывает'
                                       'именнованные аргументы.')

    def test_calculate_area_zero(self):
        call = CalculateArea.calculate_area(0)
        result = 'Неверно введены параметры.Значения должны быть больше нуля.'
        self.assertEqual(call, result, 'Функция calculate_area неправиильно обрабатыет ноль.')

    def test_calculate_area_negative(self):
        call = CalculateArea.calculate_area(-1)
        result = 'Неверно введены параметры.Значения должны быть больше нуля.'
        self.assertEqual(call, result, 'Функция calculate_area неправильно обрабатывает'
                                       ' отрицательные значения.')

    def test_calculate_area_empty_list(self):
        call = CalculateArea.calculate_area([])
        result = 'Неверно введены параметры. Это должны быть цифры.'
        self.assertEqual(call, result, 'Функция calculate_area неправильно обрабатывет'
                                       'пустой список.')

    def test_calculate_area_empty_dict(self):
        call = CalculateArea.calculate_area(1, 2)
        result = ('Пока эта библиотека умеет вычислять площадь только круга и треугольника.'
                  'Но мы научим ее работать и с другими фигурами, если Вам это будет полезно.')

        self.assertEqual(call, result, 'Функция calculate_area неправильно обрабатывает'
                                       'количество аргументов, несоответствующее ожидаемому.')

    def test_calculate_area_triangle(self):
        call = CalculateArea.calculate_area(1, 2, 3)
        result = 'Такого треугольника не существует.'
        self.assertEqual(call, result, 'Функция calculate_area неправильно определяет,'
                                       'существует ли треугольник с заявленными параметрами или нет.')

    def test_calculate_area_triangle_type(self):
        call = CalculateArea.calculate_area(2, 2, 3)
        result = '1.98, треугольник непрямоугольный'
        self.assertEqual(call, result, 'Функция calculate_area неправильно определяет тип треугольника.')


if __name__ == '__main__':
    unittest.main()
