The [Adapter Design Pattern](https://www.youtube.com/watch?v=hvpXKZhNINc) can be used, for example in the StarCraft game, to insert an external character in the game.

The pattern consists in having a wrapper class that will adapt the code from the external source.

## Your Task
The adapter receives an instance of the object that it is going to adapt and handles it in a way that works with our application.

In this example we have the pre-loaded classes:
```
public class Target
{
    public int Health { get; set; }
}
public interface IUnit
{
    void Attack(Target target);
}

public class Marine : IUnit
{
    public void Attack(Target target)
    {
        target.Health -= 6;
    }
}

public class Zealot : IUnit
{
    public void Attack(Target target)
    {
        target.Health -= 8;
    }
}

public class Zergling : IUnit
{
    public void Attack(Target target)
    {
        target.Health -= 5;
    }
}

public class Mario
{
    public int jumpAttack()
    {
        Console.WriteLine("Mamamia!");
        return 3;
    }
}
```
Complete the code so that we can create a `MarioAdapter` that can attack as other units do.

**Note** to calculate how much damage `mario` is going to do you have to call the `jumpAttack` method (`jump_attack` in Python).

## Resources
- [PatternCraft > Adapter](https://www.youtube.com/watch?v=hvpXKZhNINc)
- [SourceMaking > Adapter](https://sourcemaking.com/design_patterns/adapter)
- [Wikipedia > Adapter](https://en.wikipedia.org/wiki/Adapter_pattern)
# PatternCraft series
- [State Pattern](http://www.codewars.com/kata/patterncraft-state/)
- [Strategy Pattern](http://www.codewars.com/kata/patterncraft-strategy/)
- [Visitor Pattern](http://www.codewars.com/kata/patterncraft-visitor/)
- [Decorator Pattern](http://www.codewars.com/kata/patterncraft-decorator/)
- **Adapter Pattern**
- [Command Pattern](http://www.codewars.com/kata/patterncraft-command/)
The original [PatternCraft series (by John Lindquist)](https://www.youtube.com/playlist?list=PL8B19C3040F6381A2) is a collection of Youtube videos that explains some of the design patterns and how they are used (or could be) on StarCraft.
