using System;

public class MarioAdapter : IUnit
{
    public int attack;

    public MarioAdapter(Mario mario)
    {
        this.attack = mario.jumpAttack();
    }

    public void Attack(Target target)
    {
        target.Health -= attack;
    }
}
