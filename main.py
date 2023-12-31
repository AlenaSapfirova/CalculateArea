import math


class CalculateArea:
    """
    Класс вычисления площади для коуга по радиусу и
    треугольника по длинам его сторон.

    . . .

    Атрибуты: отсутствуют
    метод: calculate_area(): возвращает площадь круга или треугольника
    (в зависимости от количества аргументов определяется фигура) и определяет,
    является ли треугольник прямоугольным.
    """
    @staticmethod
    def calculate_area(*args, **kwargs):
        """
        В качестве параметров указаны и позиционные, и именнованные аргументы,
        чтобы можно было обработать ошибку.
        Т.к. стояла задача создать возможность вычисление площади фигуры без знания
        типа фигуры, был выбран способ определения фигуры через количество передаваемых
        аргументов.Также добавление формул для вычисления площади другиих фигур не будет
        сложным.
        """
        if args:
            params = list(args)
            if not any(map(lambda x: isinstance(x, (int, float)), params)):
                return 'Неверно введены параметры. Это должны быть цифры.'
            if any(map(lambda x: x <= 0, params)):
                return 'Неверно введены параметры.Значения должны быть больше нуля.'

            if len(params) == 1:
                r = params[0]
                area = 2 * math.pi * pow(r, 2)
                return f'Площадь круга {round(area, 2)}'
            if len(params) == 3:
                a, b, c = params[0], params[1], params[2]
                if not (a + b > c and b + c > a and a + c > b):
                    return 'Такого треугольника не существует.'
                perimetr = a + b + c
                p = perimetr / 2
                area = round((math.sqrt(p * (p - a) * (p - b) * (p - c))), 2)
                max_params = params.pop(params.index(max(params)))
                if (max_params * params[0]) / 2 == (
                        params[1] * params[1]
                ) / 2:
                    shape = 'треугольный прямоугольный'
                else:
                    shape = 'треугольник непрямоугольный'
                return ''.join(f'{area}, {shape}')
            else:
                return ('Пока эта библиотека умеет вычислять площадь только круга и треугольника.'
                        'Но мы научим ее работать и с другими фигурами, если Вам это будет полезно.')
        return 'Данные не введены или введены неверно. Это должны быть цифры.'


if __name__ == '__main__':
    CalculateArea.calculate_area()
