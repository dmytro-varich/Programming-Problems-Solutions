// signtest.cpp
// работа со знаковыми и беззнаковыми переменными
#include <iostream>
using namespace std;

int main()
{
    int signedVar = 1500000000;
    unsigned int unsignVar = 1500000000;
    
    signedVar = (signedVar * 2) / 3;    // выход за границу диапазона
    unsignVar = (unsignVar * 2) / 3;    // остается в диапазоне
    
    cout << "Signed variable equal to " << signedVar << endl;
    cout << "Unsigned variable equal to " << unsignVar << endl;
    return 0;
}