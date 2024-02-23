To solve this kata, you need to create a character class that can be used for a roguelike game. Instances of this class must have the characteristics strength, dexterity and intelligence and can call some test-generated methods that will change these characteristics or give the character a new weapon.

The Character class must have 2 mandatory instance methods - one will display character information and the other will display the event log. Only these output methods will be checked by tests The names of the properties or how the user stores any values is entirely up to the user and individual properties will not be checked.

# Character
The character has a `name` and 3 main characteristics: `strength`, `dexterity`, `intelligence`. Name and characteristics are set randomly when creating a character; if some characteristic is not specified, then the default value is taken equal to `10`, name default value is `'Hero'`. Initially, the character is armed only with his `'limbs'`(lowercase), the damage from which is equal to the sum of his characteristics.
```
ch = Character(name='Kroker', strength=15, intelligence=7)
```
The method giving the character's info returns a multiline string. Let's check, the missing characteristic will be equal to 10, and the weapon will be `'limbs'`
```
print(ch.character_info()) #=> "Kroker\nstr 15\ndex 10\nint 7\nlimbs 32 dmg"
```
```
Kroker
str 15
dex 10
int 7
limbs 32 dmg
```

# The character finds a weapon
Weapons can be found using an instance method, the name of which is the name of the weapon. The name of the weapon method can be anything, but always consists of 3 words: the type of weapon (for example, "axe"), the word "of" and the property of the weapon (for example, "fire").
```
ch.axe_of_fire(3, 1, 0, 20) # weapon method name can be anything as long as it matches weapon_of_something
```
Weapon damage is set by parameters passed to the method, which give damage depending on characteristics and additional damage.(always the order: strength, dexterity, intellect, extra damage), the number of parameters are always 4.

In this case, the Axe of fire has parameters `3, 1, 0, 20`. This means that the damage from this weapon will be calculated according to the formula

$$
3 \times \text{strength} + 1 \times \text{dexterity} + 0 \times \text{intelligence} + 20 = 3 \times 15 + 1 \times 10 + 0 \times 7 + 20 = 75
$$

The weapon and its total damage should appear in the character info output. Damage computation calculation, hence the output of the character info thing is done with the stats of the Character at call time. Since the `'Axe of fire'`, unlike the `'limbs'`, is a name, it must be capitalized.
```
Kroker
str 15
dex 10
int 7
Axe of fire 75 dmg
```
All events with found weapons go into the event log
```
print(ch.event_log())
```
```
Kroker finds 'Axe of fire'
```

# The character finds another weapon that will do more damage
The character should always choose the weapon with the highest damage, if he received a stronger weapon, If 2 weapons have the same damage, then choose the first one in alphabetical order.
```
ch.staff_of_water(1, 0, 2, 60)
```
Staff of water has 89 damage`(1 * 15 + 0 * 10 + 7 * 2 + 60)` this is more than the 'Axe of fire', which means we need to change weapons.
```
Kroker
str 15
dex 10
int 7
Staff of water 89 dmg
```
The character retains all the weapons found, that is, although we replaced the 'Axe of fire' with the 'Staff of water', the 'Axe of fire' will remain in the character’s inventory.

# Enhancement
If a character has 2 weapons with the same name, then he enhances one of them and destroys the other.
```
ch.axe_of_fire(1, 2, 1, 10)
```
Now there are 2 'Axe of fire', so let’s enhance one of them by destroying the other one. The enhancement will make each damage parameter maximum from those of the 2 original weapons.

$$
(3,1,0,20)and(1,2,1,10)⇒(max(3,1),max(1,2),max(0,1),max(20,10))⇒(3,2,1,20)
$$

The character info output shows enhanced weapons. In the output, `'(enhanced)'` is added to the name of the improved weapon.
```
Kroker
str 15
dex 10
int 7
Axe of fire(enhanced) 92 dmg
```
For the new enhancement, an `'(enhanced)'` weapon is considered the same as a non-enhanced weapon with the same name. For example: from `'Axe of fire(enhanced)'` and new `'Axe of fire'` we will make an enhancement and get new `'Axe of fire(enhanced)'`.

# Random events that changes characteristics
Character characteristics can be affected by random events. An event occurs using an instance method, the name of which is the name of the event, and the parameters (the order is always: strength, dexterity, intelligence; quantity is always 3) are stat modifiers.
```
ch.strange_fruit(-2, 0, 2)
```
The 'Strange fruit' does not change dexterity, as the 2nd coefficient is 0, but it adds -2 strength and +2 intelligence.

The character should always choose the weapon with the highest damage; if a random event changed characteristics so that some weapon from the previously found one became stronger than the one equipped, then you need to change to a stronger one from the inventory. Accordingly, we change the 'Axe of fire(enhanced)' back to the 'Staff of water'.
```
Kroker
str 13
dex 10
int 9
Staff of water 91 dmg
```
All random events end up in the event log. For random events, you do not need to specify modifiers equal to 0, but only those that changed the character's characteristics.

# Event log displays all events in order
Event log method returns all events as a string. Each event on a new line.
```
print(ch.event_log())
```
```
Kroker finds 'Axe of fire'
Kroker finds 'Staff of water'
Kroker finds 'Axe of fire'
Strange fruit: strength -2, intelligence +2
```
