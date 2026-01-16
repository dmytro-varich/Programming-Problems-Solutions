// ex2_11.cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  cout << setiosflags(ios::left) << setw(10) << "Surname"
       << setiosflags(ios::left) << setw(10) << "Name"
       << setiosflags(ios::left) << setw(10) << "Adress"
       << setiosflags(ios::left) << setw(10) << "City" << endl;
  cout << "------------------------------------------" << endl;
  cout << setiosflags(ios::left) << setw(10) << "Ivanov"
       << setiosflags(ios::left) << setw(10) << "Ivan"
       << setiosflags(ios::left) << setw(10) << "Street1"
       << setiosflags(ios::left) << setw(10) << "Kiev" << endl;
  cout << setiosflags(ios::left) << setw(10) << "Petrov"
       << setiosflags(ios::left) << setw(10) << "Vasiliy"
       << setiosflags(ios::left) << setw(10) << "Street2"
       << setiosflags(ios::left) << setw(10) << "Odessa" << endl;
  cout << setiosflags(ios::left) << setw(10) << "Sidorov"
       << setiosflags(ios::left) << setw(10) << "Petr"
       << setiosflags(ios::left) << setw(10) << "Street2"
       << setiosflags(ios::left) << setw(10) << "Odessa" << endl;  
  return 0; 
}