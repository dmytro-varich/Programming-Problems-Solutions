from operator import itemgetter

class Character:
    def __init__(self, name='Hero', strength=10, dexterity=10, intelligence=10):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.arms = 'limbs'
        self.damage = strength + dexterity + intelligence
        self.inventory = [[self.arms, self.damage, 1, 1, 1, self.damage, '']]
        self.events = str()
    
    def character_info(self) -> str:
        self.inventory = sorted(self.inventory, key=itemgetter(0), reverse=True)
        self.inventory = sorted(self.inventory, key=itemgetter(1))
        
        message = f"{self.name}\nstr {self.strength}\ndex {self.dexterity}\nint {self.intelligence}" \
        f"\n{self.inventory[-1][0]}{self.inventory[-1][-1]} {self.inventory[-1][1]} dmg"
        
        return message
        
    def event_log(self) -> str:
        return self.events.rstrip('\n')
    
    def arms_enhancement(self, arms, str, dex, int, dmg) -> None:
        enhancement = ''
        for arms, damage, strength, dexterity, intelligence, init_dmg, _ in sorted(self.inventory, key=itemgetter(1, 0)):
                if self.arms in arms:
                    enhancement = '(enhanced)' 
                    str, dex, int, dmg = max([str, strength]), max([dex, dexterity]), max([int, intelligence]), max([dmg, init_dmg])
                    self.inventory.remove([arms, damage, strength, dexterity, intelligence, init_dmg, _])
                    break
        self.damage = str * self.strength + dex * self.dexterity + int * self.intelligence + dmg
        self.inventory.append([self.arms, self.damage, str, dex, int, dmg, enhancement])
    
    def add_random_events(self, event, strength, dexterity, intelligence) -> None:
        stats = [
            f"strength {'+' if strength > 0 else ''}{strength}",
            f"dexterity {'+' if dexterity > 0 else ''}{dexterity}",
            f"intelligence {'+' if intelligence > 0 else ''}{intelligence}"
        ]
            
        stats = [stat for stat in stats if "0" not in stat]
        self.events += f"{event}: " + ", ".join(stats) + '\n'
        
    def __getattr__(self, attr):
        method_name = attr.replace('_', ' ').capitalize()
        if ' of ' in method_name:
            self.arms = method_name
            self.events += f"{self.name} finds '{self.arms}'\n"
            def weapon_method(*args):
                strength, dexterity, intelligence, damage = args[0], args[1], args[2], args[3]
                self.arms_enhancement(self.arms, strength, dexterity, intelligence, damage)
            return weapon_method
        else: 
            event = method_name
            def event_method(*args):
                strength, dexterity, intelligence = args[0], args[1], args[2]
                self.strength += strength
                self.dexterity += dexterity
                self.intelligence += intelligence 
                for i, [arms, damage, str, dex, int, init_dmg, enhancement] in enumerate(sorted(self.inventory, key=itemgetter(1, 0))):
                    if arms != 'limbs':
                        damage = self.strength * str + self.dexterity * dex + self.intelligence * int + init_dmg
                    else:
                        damage = self.strength * str + self.dexterity * dex + self.intelligence * int
                    self.inventory[i] = [arms, damage, str, dex, int, init_dmg, enhancement]
                self.add_random_events(event, strength, dexterity, intelligence)
            return event_method
