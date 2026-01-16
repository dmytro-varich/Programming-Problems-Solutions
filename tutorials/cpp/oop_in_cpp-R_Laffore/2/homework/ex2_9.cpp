// ex2_9.cpp
#include <iostream>
using namespace std;

int main() {
  int a1, b1, a2, b2;
  char dummychar;
  cout << "Enter the first fraction: ";
  cin >> a1 >> dummychar >> b1;
  cout << "Enter the second fraction: ";
  cin >> a2 >> dummychar >> b2;
  int numerator = (a1 * b2) + (a2 * b1);
  int denominator = b1 * b2;
  cout << "Sum of fractions: " << numerator << "/" << denominator << endl;
  return 0;
}