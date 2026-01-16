// ex2_5.cpp
#include <iostream>
#include <ctype.h>
using namespace std;

int main() 
{
  char ch;
  cout << "Enter a character: ";
  cin >> ch;
  bool is_lower = islower(ch);
  cout << "Is the character lowercase? " << (is_lower ? "true" : "false") << endl;
  return 0;
}