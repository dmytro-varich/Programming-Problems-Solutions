// ex2_2.cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  int year1 = 1990, year2 = 1991, year3 = 1992, year4 = 1993;
  int count1 = 135, count2 = 7290, count3 = 11300, count4 = 16200;
  cout << setw(4) << year1 << setw(10) << count1 << endl
       << setw(4) << year2 << setw(10) << count2 << endl
       << setw(4) << year3 << setw(10) << count3 << endl
       << setw(4) << year4 << setw(10) << count4 << endl;
  return 0;
}