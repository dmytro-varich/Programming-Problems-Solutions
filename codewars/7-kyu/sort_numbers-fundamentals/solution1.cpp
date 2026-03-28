#include <iostream>
#include <vector>
using namespace std;

vector<int> solution(vector<int> nums) {
  if (!nums.size()) return {};
  
  unsigned long i, j;
  for (i=0; i < nums.size() + 1; i++) 
  {
    for (j=i+1; j < nums.size(); j++) 
    {
      if (nums[i] > nums[j]) 
      {
        long temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;  
      }  
    }
  }
  return nums;
}