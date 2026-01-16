// fahren.cpp
// программа для преобразования градусов Фаренгейта в градусы Цельсия
#include <iostream>
using namespace std;

int main()
{
  int tempF; // объявление переменной для температуры в градусах Фаренгейта
  cout << "Enter temperature in Fahrenheit: ";
  cin >> tempF; // ввод значения температуры в градусах Фаренгейта

  int ctemp; // объявление переменной для температуры в градусах Цельсия
  ctemp = (tempF - 32) * 5 / 9; // преобразование Фаренгейта в Цельсий
  cout << "Temperature in Celsius: " << ctemp
       << endl; // вывод результата
  return 0;
}