#include <string>
using namespace std;

string reverseString(const string &str)
{
    string res;
    for (int i = str.length() - 1; i >= 0; i--) {
      res += str[i];
    }
    return res;
}