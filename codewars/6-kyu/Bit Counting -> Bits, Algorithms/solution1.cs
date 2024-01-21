using System;


public class Kata
{
  public static int CountBits(int n)
  {    
    int[] bits = new int[31];
    string binary_number = "";
    int result;
    
    for (int b = 0; b <= 30; b++) {
      bits[b] = b;
    }
    
    for (int i = bits.Length - 1; i >= 0; i--)
    {
        if (n == 0) {
          break;
        } 
        else if (n >= (int)Math.Pow(2, bits[i])) 
        {
            binary_number += "1";
            n -= (int)Math.Pow(2, bits[i]);
        } else {
          continue;
        } 
    }
    
    result = binary_number.Length;
    return result;
  }
}
