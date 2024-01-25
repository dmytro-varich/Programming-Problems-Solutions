In this Kata you will need to fill out the missing components of a class as described below. The behaviour of the various components is not being assessed, instead the validy of declaration (for example, are things private/public).

The class you are creating (DemoClass) needs:

- A private int field, called _privateField.

- A public string field, called PublicField, with a default value of "None".

- An integer property (called LimitedProperty), that has a public get, and private set.

- A constructor that take exactly 1 integer argument and uses it as the default value for _privateField.

Valid use of this class would be:
```
var instance = new DemoClass(4);
instance.PublicField = 15; //legal, because an int will cast to a string automatically
Console.WriteLine("Property + PublicField: " + (instance.LimitedProperty+instance.PublicField));
```
> *Property + PublicField: 015*

(Notice there is no way to set LimitedProperty from outside the class)

Invalid use:
```
var instance = new DemoClass(4);
instance.LimitedProperty = 6; //setter is private
Console.WriteLine(instance._privateField);//everything about _privateField is private;
```
> *Compile time error*

You don't need any extra methods or fields.

This example isn't highly functional, but it serves to test knowledge of Object Oriented terminology such as Field, Property, Constructor, and Argument.

Hint: there are at least 2 different ways to declare LimitedProperty - one is much easier than the other at just a single line of code.

An aside: the tests use reflection to ensure the final class is structured correctly, this is somewhat advanced C# code, so don't feel overwhelmed if you don't understand them.
