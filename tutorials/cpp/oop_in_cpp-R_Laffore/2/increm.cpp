// increm.cpp
// применение операций инкрементирования
#include <iostream>
using namespace std;

int main() {
  int count = 10;
  cout << "count=" << count << endl;   // вывод числа 10
  cout << "count=" << ++count << endl; // вывод числа 11 (префиксная форма)
  cout << "count=" << count << endl;   // вывод числа 11 
  cout << "count=" << count++ << endl; // вывод числа 11 (постфиксная форма)
  cout << "count=" << count << endl;   // вывод числа 12
  return 0;
}
