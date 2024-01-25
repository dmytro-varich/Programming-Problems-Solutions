using System;
using System.Collections.Generic;

public static class Kata {
  public static IEnumerable<string> FriendOrFoe (string[] names) {
    
    List<string> FriendsList = new List<string>(); 
    
    for (int i = 0; i < names.Length; i++)
    {
      if (names[i].Length == 4){
        FriendsList.Add(names[i]);
      }  
    }
    
    return FriendsList;
  }
}
