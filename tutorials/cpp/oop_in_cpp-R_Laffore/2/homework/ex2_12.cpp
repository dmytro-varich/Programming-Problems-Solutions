// ex2_12.cpp
#include <iostream>
using namespace std;

int main()
{
    float decpounds, decfrac;
    int pounds;
    cout << "Enter number of decimal pounds: ";
    cin >> decpounds;
    pounds = static_cast<int>(decpounds);
    decfrac = decpounds - pounds;
    float deshillings = decfrac * 20;
    int shillings = static_cast<int>(deshillings);
    float decpence = (deshillings - shillings) * 12;
    int pence = static_cast<int>(decpence);
    cout << "Eqivalent amount in the old fprm of recording: "
         << "\xA3" << pounds << "." << shillings << "." << pence << endl;
    return 0;
}