// ex2_7.cpp
#include <iostream>
using namespace std;

int main() {
  float temp;
  cout << "Enter temperature in Celsius: ";
  cin >> temp;
  cout << "Temperature in Fahrenheit: " << (temp * 9.0 / 5.0 + 32) << endl;
  return 0;
}