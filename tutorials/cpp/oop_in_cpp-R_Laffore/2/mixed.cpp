// mixed.cpp
// работа с переменными разных типов
#include <iostream>
using namespace std;

int main()
{
    int count = 7;
    float avgWeight = 155.5F;
    double totalWeight = count * avgWeight;

    cout << "Total weight of " << count << " items is " << totalWeight
         << " units." << endl;
    return 0;
}