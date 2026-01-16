// ex2_10.cpp
#include <iostream>
#include <cmath>
using namespace std;

double roundTo(double value, int decimals) {
    double factor = pow(10, decimals);
    return round(value * factor) / factor;
}

int main()
{
    cout << "Enter number of pounds: ";
    int pounds;
    cin >> pounds;
    cout << "Enter number of shillings: ";
    int shillings;
    cin >> shillings;
    cout << "Enter number of pence: ";
    int pence;
    cin >> pence;

    int total_pence = (pounds * 20 * 12) + (shillings * 12) + pence;
    float total_decimal_pounds = roundTo(total_pence / 240.0F, 2);
    cout << "Total in decimal pounds: " << "\xA3" << total_decimal_pounds << endl;
    return 0;
}