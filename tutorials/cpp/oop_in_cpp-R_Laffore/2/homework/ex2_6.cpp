// ex2_6.cpp
#include <iostream>
using namespace std;

int main() {
  float pound = 1.487F, franc = 0.172F, mark = 0.584F, yen = 0.00955F;
  float dollars;
  cout << "Enter the amount in U.S. dollars: ";
  cin >> dollars;
  cout << "Equivalent in pounds: " << dollars * pound << endl;
  cout << "Equivalent in francs: " << dollars * franc << endl;
  cout << "Equivalent in marks: " << dollars * mark << endl;
  cout << "Equivalent in yen: " << dollars * yen << endl;
  return 0;
}