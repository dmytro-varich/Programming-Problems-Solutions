using System;

public class Guesser
{
    private int number;
    private int lives;
    public Guesser(int number, int lives)
    {
        this.number = number;
        this.lives = lives;
    }

    public bool Guess(int n)
    {
        if (lives == 0)
          throw new Exception("You guess more than the limit");
      
        if (n == number) 
          return true; 
        else 
          lives -= 1;
        
        return false;
    }
}
