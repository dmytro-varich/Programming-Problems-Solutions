#include <iostream>
#include <string>
using namespace std;

string reverse_words(string str)
{
  string str1 = str + ' ';
  string res;
  int len = str1.length();
  for (int i=0; i < len; i++){
    if (str[i] == ' ' || i == len-1) {
      for (int j = i-1; j >= 0; j--) {
         if (str[j] == ' ') {
           break;
         }
         res += str[j];
      }
      if (i == len - 1) {break;}
      res += str[i];
    }
  }
  return res;
}