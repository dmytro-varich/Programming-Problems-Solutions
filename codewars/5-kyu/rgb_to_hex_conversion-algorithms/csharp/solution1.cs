using System;
using System.Collections.Generic;

public class Kata
{
  public static string Rgb(int r, int g, int b) 
  {
    if (r == 0 && b == 0 && g == 0) { return "000000"; } 
    
    Dictionary<int, string> table = new Dictionary<int, string>();
    table.Add(10, "A");
    table.Add(11, "B");
    table.Add(12, "C");
    table.Add(13, "D");
    table.Add(14, "E");
    table.Add(15, "F");
  
    int[] rgb = {r, g, b};
    int rmd;
    string result = "";
    
    for (int i = 0; i < 3; i++)
    {
        if (rgb[i] > 255) { rgb[i] = 255; }
        if (rgb[i] < 0) { rgb[i] = 0; } 
        if (rgb[i] == 0) { result += "00"; }
        while (rgb[i] > 0)
        { 
            rmd = rgb[i];
            rgb[i] /= 16;
            rmd %= 16;
          
            if (table.ContainsKey(rmd))
            {
              result += table[rmd];
            }
            else 
            {
              result += rmd;
            }
        }
      
        if (result.Length % 2 != 0)
        {
          result += "0";
        }
    }
    
    char tmp;
    char[] reverse_section = result.ToCharArray();
    for (int i = 1; i < reverse_section.Length; i+=2)
    {
        tmp = reverse_section[i];    
        reverse_section[i] = reverse_section[i-1];
        reverse_section[i - 1] = tmp;
    }
    
    return new string(reverse_section);
  }
}
