#include <stdio.h>

// Функция для нахождения суммы цифр числа
int findDigitSum(int number) {
    int sum = 0;
    while (number != 0) {
        sum += number % 10;
        number /= 10;
    }
    return sum;
}

int main() {
    // Переменные для параметров a, b
    int a, b;

    // Ввод параметров a и b
    printf("Введите параметр a: ");
    scanf("%d", &a);

    printf("Введите параметр b: ");
    scanf("%d", &b);

    // Находим суммы цифр параметров
    int sum_a = findDigitSum(a);
    int sum_b = findDigitSum(b);

    // Находим сумму цифр второго параметра
    int sum_second_param = findDigitSum(sum_b);

    // Сравниваем суммы и находим наименьшую
    int min_sum = sum_a < sum_b ? (sum_a < sum_second_param ? sum_a : sum_second_param) : (sum_b < sum_second_param ? sum_b : sum_second_param);

    // Вычисляем частное наименьшей суммы и второго параметра
    float result = (float)min_sum / sum_b;

    // Вывод результата
    printf("Частное наименьшей суммы цифр и второго параметра: %.2f\n", result);

    return 0;
}