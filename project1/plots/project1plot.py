import numpy as np
import matplotlib.pyplot as plt
import sys


class Rowling:
    def hermione(self, filename, variable1 = 0, variable2 = 1, variable3= 2):
        """
        Function that automatically reads a file and
        makes a plot.
        The name? Because Hermione reads.
        """

        filename = "../benchmarks/%s.txt" %filename

        x = []
        y1 = []
        y2 = []
    
        f = open(filename, "r")
        f.readline() #skips first line
        for line in f:
            data = line.split(',')
            for j in range(1, len(data)):
                data[j] = ''.join(data[j].split())
            x.append(float(data[variable1]))
            y1.append(float(data[variable2]))
            y2.append(float(data[variable3]))
        return x, y1, y2

    def harry_plotter(self, x, y1, y2, filename, xlab = 'x', ylab='y'
                      , plotlab1 = ' ', plotlab2 = '',
                      d=1, title = ' '):
        """
        The name? Because it's funny.
        """
        plt.plot(x, y1, '-b', label = '%s' %plotlab1)
        plt.plot(x, y2, '--g', label = '%s' %plotlab2)
        plt.xlabel('%s' %xlab)
        plt.ylabel('%s' %ylab)
        plt.legend(loc=d)
        plt.title('%s' %title)
        plt.savefig('%s.png' %filename)
        plt.show()


if __name__ == '__main__':
    a = Rowling()
    x, y1, y2 = a.hermione("task_b_N_10", 0, 1, 2)
    a.harry_plotter(x, y1, y2, "task_b_N_10",
                    xlab = 'x-values', ylab = 'u- and v-values',
                    title = 'N = 10', plotlab1 = 'u(x)', plotlab2 = 'v(x)')
    x1, y3, y4 = a.hermione("task_b_N_100", 0, 1, 2)
    a.harry_plotter(x1, y3, y4, "task_b_N_100",
                    xlab = 'x-values', ylab = 'u- and v-values',
                    title = 'N = 100',plotlab1 = 'u(x)', plotlab2 = 'v(x)')
    x2, y5, y6 = a.hermione("task_b_N_1000", 0, 1, 2)
    a.harry_plotter(x2, y5, y6, "task_b_N_1000",
                    xlab = 'x-values', ylab = 'u- and v-values',
                    title = 'N = 1000', plotlab1 = 'u(x)', plotlab2 = 'v(x)')
