// assign.cpp
// применение арифметических операций с присваиванием
#include <iostream>
using namespace std;

int main() {
  int ans = 27;
  ans += 3; // эквивалентно ans = ans + 3
  cout << ans << ", ";
  ans -= 6; // эквивалентно ans = ans - 6
  cout << ans << ", ";
  ans *= 5; // эквивалентно ans = ans * 5
  cout << ans << ", ";
  ans /= 3; // эквивалентно ans = ans / 3
  cout << ans << ", ";
  return 0;
}