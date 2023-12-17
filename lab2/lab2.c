#include <stdio.h>
#include <math.h>

int main() {
    FILE *gnuplotPipe = popen("gnuplot -persistent", "w");

    // Диапазон значений x
    double x;

    // Вычисление и вывод значений функции для -1 <= x <= 2
    for (x = -1; x <= 2; x += 0.1) {
        double result;

        // Вычисление функции f(x)
        if (x >= -1 && x <= 1) {
            result = exp(-2 * sin(x));
        } else {
            result = x * x - 1.0 / tan(x);
        }

        // Вывод в консоль и в файл для gnuplot
        printf("%lf %lf\n", x, result);
        fprintf(gnuplotPipe, "%lf %lf\n", x, result);
    }

    // Закрытие гнуплота
    fprintf(gnuplotPipe, "exit \n");
    pclose(gnuplotPipe);

    return 0;
}