// circarea.cpp
// программа для вычисления площади круга
#include <iostream>
using namespace std;

int main() {
    float rad;                  // объявление переменной для радиуса круга
    const float PI = 3.14159F;  // объявление константы для числа Пи
    cout << "Enter radius of the circle: ";  // запрос ввода радиуса
    cin >> rad;             // ввод значения радиуса

    float area = PI * rad * rad;  // вычисление площади круга
    cout << "Area of the circle: " << area << endl;  // вывод результата
    return 0;
}