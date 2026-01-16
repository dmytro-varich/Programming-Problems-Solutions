// width.cpp
// работа с установкой ширины вывода
#include <iostream>
#include <iomanip> // подключение библиотеки манипуляторов
using namespace std;

int main()
{
  long pop1 = 8425785, pop2 = 47, pop3 = 9761;
  cout << setw(8) << "Country " << setw(12)
       << "Populations:" << endl; // установка ширины вывода
  cout << setw(8) << "USA" << setw(12) << pop1 << endl;
  cout << setw(8) << "UK" << setw(12) << pop2 << endl;
  cout << setw(8) << "France" << setw(12) << pop3 << endl;
  return 0; // успешное завершение программы
}