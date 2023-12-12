import numpy as np
import matplotlib.pyplot as plt


class GraphWorker:
    def __init__(self, start_x, start_y):
        self.y_list_step_2 = []
        self.x_list_step_2 = []
        self.y_list_step_1 = []
        self.x_list_step_1 = []
        self.start_x = start_x
        self.start_y = start_y
        self.start_segment = 0
        self.end_segment = 1
        self.step_1 = 0.1
        self.step_2 = 0.01

    @staticmethod
    def get_equation(x, y):
        return np.cos(1.5 * x + y) + 1.5 * (x - y)

    def get_initial_values(self):
        return self.start_x, self.start_y

    def set_x_list_step_1(self, value):
        self.x_list_step_1 = value

    def set_y_list_step_1(self, value):
        self.y_list_step_1 = value

    def set_x_list_step_2(self, value):
        self.x_list_step_2 = value

    def set_y_list_step_2(self, value):
        self.y_list_step_2 = value

    def get_x_list_step_1(self):
        return self.x_list_step_1

    def get_y_list_step_1(self):
        return self.y_list_step_1

    def get_x_list_step_2(self):
        return self.x_list_step_2

    def get_y_list_step_2(self):
        return self.y_list_step_2

    def calc_with_coefficients(self, coord_x, coord_y, step):
        coefficient_1 = step * self.get_equation(coord_x, coord_y)
        coefficient_2 = step * self.get_equation(coord_x + step/2, coord_y + coefficient_1/2)
        coefficient_3 = step * self.get_equation(coord_x + step/2, coord_y + coefficient_2/2)
        coefficient_4 = step * self.get_equation(coord_x + step, coord_y + coefficient_3)

        result = coord_y + (coefficient_1 + 2*coefficient_2 + 2*coefficient_3 + coefficient_4)/6

        return result

    def calc(self):
        self.set_x_list_step_1(np.arange(self.start_segment, self.end_segment + self.step_1, self.step_1))
        self.set_x_list_step_2(np.arange(self.start_segment, self.end_segment + self.step_2, self.step_2))

        tmp_x, tmp_y = self.get_initial_values()
        initial_length = len(self.get_x_list_step_1())
        for i in range(initial_length):
            prev_y_list = self.get_y_list_step_1()
            prev_y_list.append(tmp_y)
            self.set_y_list_step_1(prev_y_list)
            tmp_y = self.calc_with_coefficients(tmp_x, tmp_y, self.step_1)
            tmp_x += self.step_1

        tmp_x, tmp_y = self.get_initial_values()
        initial_length = len(self.get_x_list_step_2())
        for i in range(initial_length):
            prev_y_list = self.get_y_list_step_2()
            prev_y_list.append(tmp_y)
            self.set_y_list_step_2(prev_y_list)
            tmp_y = self.calc_with_coefficients(tmp_x, tmp_y, self.step_2)
            tmp_x += self.step_2

    def draw_figure(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.get_x_list_step_1(), self.get_y_list_step_1(), label=f'Step size: {self.step_1}')
        plt.plot(self.get_x_list_step_2(), self.get_y_list_step_2(), label=f'Step size: {self.step_2}')
        plt.title('Метод Рунге-Кутты')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    graph = GraphWorker(0, 0)
    graph.calc()
    graph.draw_figure()
