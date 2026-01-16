// cast.cpp
// работа со знаковыми и безнаковыми переменными 
#include <iostream>
using namespace std;

int main()
{
    int intVar = 1500000000;
    intVar = (intVar * 10) / 10;
    cout << "Integer variable equal to " << intVar << endl;

    intVar = 1500000000;
    intVar = (static_cast<double>(intVar) * 10) / 10;
    cout << "Integer variable equal to " << intVar << "\n";
    return 0;
}