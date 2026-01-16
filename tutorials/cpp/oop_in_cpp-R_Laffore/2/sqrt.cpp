// sqrt.cpp
// вычисление квадратного корня
// используя библиотечную функцию
#include <iostream>
#include <cmath>    // для функции sqrt
using namespace std;

int main() {
  double number, answer;
  cout << "Enter a positive number: ";
  cin >> number;
  answer = sqrt(number);
  cout << "Square root of " << number << " is " << answer << endl;
  return 0;
}