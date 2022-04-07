import math


class TaylorSeries:
    def __init__(self, degree, n):
        self.degree = degree
        self.n = n

    def convert_degree_to_radiant(self):
        """
        для того щоб конвертувати кут у градусах у
        радіани
        слід скласти пропорцію виду
        180  degree
          π  x
        Виходячи з цього x = (π * degree)/180
        """

        converter = (math.pi * self.degree) / 180

        return converter

    def sin(self):
        """
        Для того щоб обрахувати синус чи косинус
        використовується ряд Тейлора
        чи Маклорена
        """

        x = self.convert_degree_to_radiant()

        result = 0

        for i in range(0, self.n + 1):
            first_part_of_formula = ((-1) ** i) * (x **
                                                   ((2 * i) + 1))

            second_part_of_formula = math.factorial((2 * i) + 1)

            result += (first_part_of_formula /
                       second_part_of_formula)

        return result

    def cos(self):

        x = self.convert_degree_to_radiant()

        result = 0

        for i in range(0, self.n + 1):
            first_part_of_formula = x ** (2 * i)

            second_part_of_formula = math.factorial(2 * i)

            result += ((-1) ** i) * (first_part_of_formula /
                                     second_part_of_formula)

        return result

    def ln(self, x):
        """Функція для натурального логарифму виду ln(1 + x)"""

        result = 0

        for i in range(1, self.n + 1):
            if x > -1 or x < 1:
                first_part_of_formula = x ** i
                second_part_of_formula = i
                result = ((-1) ** (i - 1)) * (first_part_of_formula / second_part_of_formula)

        return result

    def arctan(self):

        x = self.convert_degree_to_radiant()

        result = 0

        for i in range(0, self.n + 1):
            if x > -1 or x < 1:
                first_part_of_formula = ((-1) ** i) * (x ** ((2 * i) + 1))

                second_part_of_formula = (2 * i) + 1

                result += (first_part_of_formula / second_part_of_formula)

        return result
