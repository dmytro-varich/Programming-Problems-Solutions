// ex2_1.cpp
#include <iostream>
using namespace std;

int main() {
  const float gallon = 7.481F; // 1 cubic foot = 7.481 gallons
  float gallons;
  cout << "Enter the number of gallons of water: ";
  cin >> gallons;
  float cubicFeet = gallons / gallon;
  cout << gallons << " gallons is equivalent to " << cubicFeet << " cubic feet." << endl;
  return 0;
  }