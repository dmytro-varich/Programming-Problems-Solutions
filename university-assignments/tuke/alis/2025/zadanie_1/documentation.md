# Zebra puzzle 

Four houses are located beside each other in a row. Each house has unique characteristics (e.g.,
inhabitants’ preferences, name, etc.). Your objective is to identify which house has which
characteristics.

| Property     | House #1 | House #2 | House #3 | House #4 |
|--------------|----------|----------|----------|----------|
| **Color**        |          |          |          |          |
| **Nationality**  |          |          |          |          |
| **Animal**       |          |          |          |          |
| **Sport**        |          |          |          |          |


<b>Color:</b> black, blue, red, white.<br>
<b>Nationality:</b> American, British, Canadian, Irish.<br>
<b>Animal:</b> butteries, dolphins, horses, turtles.<br>
<b>Sport:</b> bowling, handball, swimming, tennis.<br>

## Rules

1. There are two houses between the person who likes **Bowling** and the person who likes **Swimming**.
2. There is one house between the **Irish** person and the person who likes **Handball**, with the Irish person on the **left**.
3. The **second house** is **Black**.
4. There is one house between the person who likes **Horses** and the **Red** house, with the Red house on the **right**.
5. The **American** lives directly to the **left** of the person who likes **Turtles**.
6. There are two houses between the person who likes **Horses** and the person who likes **Butterflies**, with the Butterflies person on the **right**.
7. The person who likes **Bowling** lives somewhere to the **right** of the person who likes **Tennis**.
8. There is one house between the person who likes **Handball** and the **White** house, with the White house on the **right**.
9. The **British** lives in the **first house**.

---

# SAT-based Solution

## Contents

1. **Formulation of the task as a constraint problem**
   - 1.1 Definition of variables and their domains  
   - 1.2 Definition of constraints over domains  
   - 1.3 Analysis of redundant constraints  
   - 1.4 Selection of a minimal set of constraints  
   - 1.5 Formal representation of constraints  

2. **Creation of a logical model**
   - 2.1 Method of variable representation  
   - 2.2 Formal constraints to logical clauses  
   - 2.3 Final CNF model  
   - 2.4 CNF clause count estimation  

3. **Transformation of the model into the DIMACS format**
   - 3.1 Logical variable indexing  
   - 3.2 DIMACS format requirements  
   - 3.3 Final DIMACS file  

4. **Use of a SAT solver**
   - 4.1 About CryptoMiniSat5  
   - 4.2 SAT solver output  
   - 4.3 Final assignment of properties to houses

## 1. Formulation of the task as a constraint problem.

The problem involves four houses arranged sequentially. 
Each house is described by four property types: **color**, **nationality**, **animal**, and **sport**. For each attribute type, one variable is introduced per house.

### 1.1 Definition of variables and their domains

1) **Color Variables**<br>
Represents the color of each house.
<br><br>
For each $i ∈ \{1,2,3,4\}$

   - ${Color}_i$ <br>
    **Domain**(${Color}_i$) = {black, blue, red, white}

2) **Nationality Variables**<br>
Represents the nationality of the resident in each house.
<br><br>
For each $i ∈ \{1,2,3,4\}$

   - ${Nationality}_i$ <br>
     **Domain**(${Nationality}_i$) = {American, British, Canadian, Irish}

3) **Animal Variables**<br>
Represents the pet/animal associated with each house.
<br><br>
For each $i ∈ \{1,2,3,4\}$

   - ${Animal}_i$ <br>
     **Domain**(${Animal}_i$) = {butterflies, dolphins, horses, turtles}

4) **Sport Variables**<br>
Represents the favorite sport of the resident in each house.
<br><br>
For each $i ∈ \{1,2,3,4\}$

   - ${Sport}_i$ <br>
     **Domain**(${Sport}_i$) = {bowling, handball, swimming, tennis}

### 1.2 Definition of constraints over domains

#### A. Basic domain constraints

1. Each house has **exactly one value** for each property.
2. Each property value is used **exactly once** among all houses.

#### B. Problem-specific constraints

* There are **two houses** between the person who likes **Bowling** and the person who likes **Swimming**.
* There is **one house** between the **Irish** person and the person who likes **Handball** on the left.
* The **second house** is **Black**.
* There is **one house** between the person who likes **Horses** and the **Red** house on the right.
* The **American** lives **directly to the left** of the person who likes **Turtles**.
* There are **two houses** between the person who likes **Horses** and the person who likes **Butterflies** on the right.
* The person who likes **Bowling** lives somewhere **to the right** of the person who likes **Tennis**.
* There is **one house** between the person who likes **Handball** and the **White** house on the right.
* The **British** lives in the **first house**.

### 1.3 Analysis of redundant constraints

All constraints are **unique** and there are **no redundancies**.

### 1.4 Selection of a minimal set of constraints

All constraints used are **only those required by the problem conditions**.
This includes:

* The **two basic domain constraints** described in section A.
* The **nine problem-specific rules** described in section B.

> No constraint is a **logical consequence** of a combination of the others.
The domain constraints have been chosen in a **minimal form** (exactly-one).

### 1.5 Formal representation of constraints

The constraints of the problem are expressed using standard first-order predicate logic.

We denote:

- $H = \{1,2,3,4\}$ – the set of houses

- $\text{Domain(Color)} = \{\text{black}, \text{blue}, \text{red}, \text{white}\}$

- $\text{Domain(Nationality)} = \{\text{American}, \text{British}, \text{Canadian}, \text{Irish}\}$

- $\text{Domain(Animal)} = \{\text{butterflies}, \text{dolphins}, \text{horses}, \text{turtles}\}$

- $\text{Domain(Sport)} = \{\text{bowling}, \text{handball}, \text{swimming}, \text{tennis}\}$

#### A. Basic domain constraints

1. Each house has **exactly one value** for each property.<br>
   For every property $X ∈ \{Color, Nationality, Animal, Sport\}$ 
   and every house $i ∈ H$:<br><br>
   **At least one value:**

   $$
   \bigvee_{v \in Domain(X)} (X(i) = v)
   $$

   **At most one value:**

   $$
   \forall\, u, v \in Domain(X),\; u \neq v:\;
   \neg\big( (X(i)=u) \land (X(i)=v) \big)
   $$

2. Each property value is used **exactly once** among all houses.<br>
   For every property value $v ∈ Domain(X)$:<br>
   $$
   \forall\, i, j \in H,\; i \neq j:\;
   \neg\big( (X(i)=v) \land (X(j)=v) \big)
   $$

#### B. Problem-specific constraints

1. There are **two houses** between the person who likes **Bowling** and the person who likes.<br>
   $$
   (Sport(i) = \text{bowling} \wedge Sport(i+3) = \text{swimming}) \lor
   (Sport(i) = \text{swimming} \wedge Sport(i+3) = \text{bowling})
   $$

   for all valid $i \in \{1\}$.
2.  There is **one house** between the **Irish** person and the person who likes **Handball** on the left.<br>
    $$
    (Sport(i) = \text{handball} \wedge Nationality(i+2) = \text{Irish})
    $$
    for all valid $i \in \{1,2\}$.
3. The **second house** is **Black**.<br>
   $$
   Color(2) = \text{black}
   $$
4. There is **one house** between the person who likes **Horses** and the **Red** house on the right.
   <br>
   $$
   (Animal(i) = \text{horses} \wedge Color(i+2) = \text{red})
   $$

   for all valid $i \in \{1,2\}$.
5. The **American** lives **directly to the left** of the person who likes **Turtles**.<br>
   $$
   (Nationality(i) = \text{American} \wedge Animal(i+1) = \text{turtles})
   $$

   for all valid $i \in \{1,2,3\}$.
6. There are **two houses** between the person who likes **Horses** and the person who likes **Butterflies** on the right.<br>
   $$
   (Animal(i) = \text{horses} \wedge Animal(i+3) = \text{butterflies})
   $$

   for all valid $i \in \{1\}$.
7. The person who likes **Bowling** lives somewhere **to the right** of the person who likes **Tennis**.<br>
   $$
   Sport(j) = \text{tennis} \wedge Sport(i) = \text{bowling} \Rightarrow j > i
   $$
8. There is **one house** between the person who likes **Handball** and the **White** house on the right.<br>
   $$
   (Sport(i) = \text{handball} \wedge Color(i+2) = \text{white})
   $$

   for all valid $i \in \{1,2\}$.
9.  The **British** lives in the **first house**.<br>
    $$
    Nationality(1) = \text{British}
    $$

## 2. Creation of a logical model

To construct the logical model, we use Boolean encoding, where **one fact corresponds to one variable**.
Thus, each variable has the form:

```
X_i_property
```

where:

- $X \in \{C, N, A, S\}$<br>
  (Color, Nationality, Animal, Sport)
- $i \in \{1, 2, 3, 4\}$ – the house number
- $property \in \{property₁, property₂, property₃, property₄\}$ – the value of the attribute

### Example:

- `C_1_black = house 1 is black`
- `N_3_Irish = house 3 is Irish`
- `A_2_horses = house 2 has horses`
- `S_4_handball = house 4 plays handball`

### 2.1 Method of variable representation

After converting all properties into logical variables, the total number of variables becomes:

**4 attribute types × 4 houses × 4 values = 64 SAT variables.**

1) **Color Varibles**

   ```text
   C_1_black,     C_2_black,     C_3_black,     C_4_black
   C_1_blue,      C_2_blue,      C_3_blue,      C_4_blue
   C_1_red,       C_2_red,       C_3_red,       C_4_red
   C_1_white,     C_2_white,     C_3_white,     C_4_white
   ```

2) **Nationality Varibles**
   ```text
   N_1_American,  N_2_American,  N_3_American,  N_4_American
   N_1_British,   N_2_British,   N_3_British,   N_4_British
   N_1_Canadian,  N_2_Canadian,  N_3_Canadian,  N_4_Canadian
   N_1_Irish,     N_2_Irish,     N_3_Irish,     N_4_Irish
   ```

3) **Animal Variables**
   ```text
   A_1_butterflies, A_2_butterflies, A_3_butterflies, A_4_butterflies
   A_1_dolphins,    A_2_dolphins,    A_3_dolphins,    A_4_dolphins
   A_1_horses,      A_2_horses,      A_3_horses,      A_4_horses
   A_1_turtles,     A_2_turtles,     A_3_turtles,     A_4_turtles
   ```

4) **Sport Variables**
   ```text
   S_1_bowling,   S_2_bowling,   S_3_bowling,   S_4_bowling
   S_1_handball,  S_2_handball,  S_3_handball,  S_4_handball
   S_1_swimming,  S_2_swimming,  S_3_swimming,  S_4_swimming
   S_1_tennis,    S_2_tennis,    S_3_tennis,    S_4_tennis
   ```

### 2.2 Formal constraints to logical clauses

1. Each house has **exactly one value** for each property:<br>
   - At least one: 
      ```
      (C_1_black      ∨ C_1_blue      ∨ C_1_red      ∨ C_1_white)      ∧
      (C_2_black      ∨ C_2_blue      ∨ C_2_red      ∨ C_2_white)      ∧
      (C_3_black      ∨ C_3_blue      ∨ C_3_red      ∨ C_3_white)      ∧
      (C_4_black      ∨ C_4_blue      ∨ C_4_red      ∨ C_4_white)      ∧
      (N_1_American   ∨ N_1_British   ∨ N_1_Canadian ∨ N_1_Irish)      ∧
      (N_2_American   ∨ N_2_British   ∨ N_2_Canadian ∨ N_2_Irish)      ∧
      (N_3_American   ∨ N_3_British   ∨ N_3_Canadian ∨ N_3_Irish)      ∧
      (N_4_American   ∨ N_4_British   ∨ N_4_Canadian ∨ N_4_Irish)      ∧
      (A_1_butterflies ∨ A_1_dolphins ∨ A_1_horses   ∨ A_1_turtles)    ∧
      (A_2_butterflies ∨ A_2_dolphins ∨ A_2_horses   ∨ A_2_turtles)    ∧
      (A_3_butterflies ∨ A_3_dolphins ∨ A_3_horses   ∨ A_3_turtles)    ∧
      (A_4_butterflies ∨ A_4_dolphins ∨ A_4_horses   ∨ A_4_turtles)    ∧
      (S_1_bowling     ∨ S_1_handball ∨ S_1_swimming ∨ S_1_tennis)     ∧
      (S_2_bowling     ∨ S_2_handball ∨ S_2_swimming ∨ S_2_tennis)     ∧
      (S_3_bowling     ∨ S_3_handball ∨ S_3_swimming ∨ S_3_tennis)     ∧
      (S_4_bowling     ∨ S_4_handball ∨ S_4_swimming ∨ S_4_tennis) 
      ``` 
   - At most one: 
     ```
     (¬C_1_black ∨ ¬C_1_blue)      ∧
     (¬C_1_black ∨ ¬C_1_red)       ∧
     (¬C_1_black ∨ ¬C_1_white)     ∧
     (¬C_1_blue  ∨ ¬C_1_red)       ∧
     (¬C_1_blue  ∨ ¬C_1_white)     ∧
     (¬C_1_red   ∨ ¬C_1_white)     ∧

     (¬C_2_black ∨ ¬C_2_blue)      ∧
     (¬C_2_black ∨ ¬C_2_red)       ∧
     (¬C_2_black ∨ ¬C_2_white)     ∧
     (¬C_2_blue  ∨ ¬C_2_red)       ∧
     (¬C_2_blue  ∨ ¬C_2_white)     ∧
     (¬C_2_red   ∨ ¬C_2_white)     ∧

     (¬C_3_black ∨ ¬C_3_blue)      ∧
     (¬C_3_black ∨ ¬C_3_red)       ∧ 
     (¬C_3_black ∨ ¬C_3_white)     ∧
     (¬C_3_blue  ∨ ¬C_3_red)       ∧
     (¬C_3_blue  ∨ ¬C_3_white)     ∧ 
     (¬C_3_red   ∨ ¬C_3_white)     ∧

     (¬C_4_black ∨ ¬C_4_blue)      ∧
     (¬C_4_black ∨ ¬C_4_red)       ∧
     (¬C_4_black ∨ ¬C_4_white)     ∧
     (¬C_4_blue  ∨ ¬C_4_red)       ∧
     (¬C_4_blue  ∨ ¬C_4_white)     ∧
     (¬C_4_red   ∨ ¬C_4_white)     ∧

     (¬N_1_American ∨ ¬N_1_British)   ∧
     (¬N_1_American ∨ ¬N_1_Canadian)  ∧
     (¬N_1_American ∨ ¬N_1_Irish)     ∧
     (¬N_1_British  ∨ ¬N_1_Canadian)  ∧
     (¬N_1_British  ∨ ¬N_1_Irish)     ∧
     (¬N_1_Canadian ∨ ¬N_1_Irish)     ∧

     (¬N_2_American ∨ ¬N_2_British)   ∧
     (¬N_2_American ∨ ¬N_2_Canadian)  ∧
     (¬N_2_American ∨ ¬N_2_Irish)     ∧
     (¬N_2_British  ∨ ¬N_2_Canadian)  ∧
     (¬N_2_British  ∨ ¬N_2_Irish)     ∧
     (¬N_2_Canadian ∨ ¬N_2_Irish)     ∧

     (¬N_3_American ∨ ¬N_3_British)   ∧
     (¬N_3_American ∨ ¬N_3_Canadian)  ∧
     (¬N_3_American ∨ ¬N_3_Irish)     ∧
     (¬N_3_British  ∨ ¬N_3_Canadian)  ∧
     (¬N_3_British  ∨ ¬N_3_Irish)     ∧
     (¬N_3_Canadian ∨ ¬N_3_Irish)     ∧

     (¬N_4_American ∨ ¬N_4_British)   ∧
     (¬N_4_American ∨ ¬N_4_Canadian)  ∧
     (¬N_4_American ∨ ¬N_4_Irish)     ∧
     (¬N_4_British  ∨ ¬N_4_Canadian)  ∧
     (¬N_4_British  ∨ ¬N_4_Irish)     ∧
     (¬N_4_Canadian ∨ ¬N_4_Irish)     ∧

     (¬A_1_butterflies ∨ ¬A_1_dolphins) ∧
     (¬A_1_butterflies ∨ ¬A_1_horses)   ∧
     (¬A_1_butterflies ∨ ¬A_1_turtles)  ∧
     (¬A_1_dolphins    ∨ ¬A_1_horses)   ∧ 
     (¬A_1_dolphins    ∨ ¬A_1_turtles)  ∧
     (¬A_1_horses      ∨ ¬A_1_turtles)  ∧

     (¬A_2_butterflies ∨ ¬A_2_dolphins) ∧
     (¬A_2_butterflies ∨ ¬A_2_horses)   ∧
     (¬A_2_butterflies ∨ ¬A_2_turtles)  ∧
     (¬A_2_dolphins    ∨ ¬A_2_horses)   ∧
     (¬A_2_dolphins    ∨ ¬A_2_turtles)  ∧
     (¬A_2_horses      ∨ ¬A_2_turtles)  ∧

     (¬A_3_butterflies ∨ ¬A_3_dolphins) ∧
     (¬A_3_butterflies ∨ ¬A_3_horses)   ∧
     (¬A_3_butterflies ∨ ¬A_3_turtles)  ∧
     (¬A_3_dolphins    ∨ ¬A_3_horses)   ∧
     (¬A_3_dolphins    ∨ ¬A_3_turtles)  ∧
     (¬A_3_horses      ∨ ¬A_3_turtles)  ∧

     (¬A_4_butterflies ∨ ¬A_4_dolphins) ∧
     (¬A_4_butterflies ∨ ¬A_4_horses)   ∧
     (¬A_4_butterflies ∨ ¬A_4_turtles)  ∧
     (¬A_4_dolphins    ∨ ¬A_4_horses)   ∧
     (¬A_4_dolphins    ∨ ¬A_4_turtles)  ∧
     (¬A_4_horses      ∨ ¬A_4_turtles)  ∧

     (¬S_1_bowling   ∨ ¬S_1_handball) ∧
     (¬S_1_bowling   ∨ ¬S_1_swimming) ∧
     (¬S_1_bowling   ∨ ¬S_1_tennis)   ∧
     (¬S_1_handball  ∨ ¬S_1_swimming) ∧
     (¬S_1_handball  ∨ ¬S_1_tennis)   ∧
     (¬S_1_swimming  ∨ ¬S_1_tennis)   ∧

     (¬S_2_bowling   ∨ ¬S_2_handball) ∧
     (¬S_2_bowling   ∨ ¬S_2_swimming) ∧
     (¬S_2_bowling   ∨ ¬S_2_tennis)   ∧
     (¬S_2_handball  ∨ ¬S_2_swimming) ∧
     (¬S_2_handball  ∨ ¬S_2_tennis)   ∧
     (¬S_2_swimming  ∨ ¬S_2_tennis)   ∧

     (¬S_3_bowling   ∨ ¬S_3_handball) ∧
     (¬S_3_bowling   ∨ ¬S_3_swimming) ∧
     (¬S_3_bowling   ∨ ¬S_3_tennis)   ∧
     (¬S_3_handball  ∨ ¬S_3_swimming) ∧
     (¬S_3_handball  ∨ ¬S_3_tennis)   ∧
     (¬S_3_swimming  ∨ ¬S_3_tennis)   ∧

     (¬S_4_bowling   ∨ ¬S_4_handball) ∧
     (¬S_4_bowling   ∨ ¬S_4_swimming) ∧
     (¬S_4_bowling   ∨ ¬S_4_tennis)   ∧
     (¬S_4_handball  ∨ ¬S_4_swimming) ∧
     (¬S_4_handball  ∨ ¬S_4_tennis)   ∧
     (¬S_4_swimming  ∨ ¬S_4_tennis) 
     ``` 
2. Each property value is used **exactly once** among all houses:
   ```
      (¬C_1_black ∨ ¬C_2_black)      ∧
      (¬C_1_black ∨ ¬C_3_black)      ∧
      (¬C_1_black ∨ ¬C_4_black)      ∧
      (¬C_2_black ∨ ¬C_3_black)      ∧
      (¬C_2_black ∨ ¬C_4_black)      ∧
      (¬C_3_black ∨ ¬C_4_black)      ∧

      (¬C_1_blue  ∨ ¬C_2_blue)       ∧
      (¬C_1_blue  ∨ ¬C_3_blue)       ∧
      (¬C_1_blue  ∨ ¬C_4_blue)       ∧
      (¬C_2_blue  ∨ ¬C_3_blue)       ∧
      (¬C_2_blue  ∨ ¬C_4_blue)       ∧
      (¬C_3_blue  ∨ ¬C_4_blue)       ∧

      (¬C_1_red   ∨ ¬C_2_red)        ∧
      (¬C_1_red   ∨ ¬C_3_red)        ∧
      (¬C_1_red   ∨ ¬C_4_red)        ∧
      (¬C_2_red   ∨ ¬C_3_red)        ∧
      (¬C_2_red   ∨ ¬C_4_red)        ∧
      (¬C_3_red   ∨ ¬C_4_red)        ∧

      (¬C_1_white ∨ ¬C_2_white)      ∧
      (¬C_1_white ∨ ¬C_3_white)      ∧
      (¬C_1_white ∨ ¬C_4_white)      ∧
      (¬C_2_white ∨ ¬C_3_white)      ∧
      (¬C_2_white ∨ ¬C_4_white)      ∧
      (¬C_3_white ∨ ¬C_4_white)      ∧

      (¬N_1_American ∨ ¬N_2_American) ∧
      (¬N_1_American ∨ ¬N_3_American) ∧
      (¬N_1_American ∨ ¬N_4_American) ∧
      (¬N_2_American ∨ ¬N_3_American) ∧
      (¬N_2_American ∨ ¬N_4_American) ∧
      (¬N_3_American ∨ ¬N_4_American) ∧

      (¬N_1_British ∨ ¬N_2_British)   ∧
      (¬N_1_British ∨ ¬N_3_British)   ∧
      (¬N_1_British ∨ ¬N_4_British)   ∧
      (¬N_2_British ∨ ¬N_3_British)   ∧
      (¬N_2_British ∨ ¬N_4_British)   ∧
      (¬N_3_British ∨ ¬N_4_British)   ∧

      (¬N_1_Canadian ∨ ¬N_2_Canadian) ∧
      (¬N_1_Canadian ∨ ¬N_3_Canadian) ∧
      (¬N_1_Canadian ∨ ¬N_4_Canadian) ∧
      (¬N_2_Canadian ∨ ¬N_3_Canadian) ∧
      (¬N_2_Canadian ∨ ¬N_4_Canadian) ∧
      (¬N_3_Canadian ∨ ¬N_4_Canadian) ∧

      (¬N_1_Irish ∨ ¬N_2_Irish)       ∧
      (¬N_1_Irish ∨ ¬N_3_Irish)       ∧
      (¬N_1_Irish ∨ ¬N_4_Irish)       ∧
      (¬N_2_Irish ∨ ¬N_3_Irish)       ∧
      (¬N_2_Irish ∨ ¬N_4_Irish)       ∧
      (¬N_3_Irish ∨ ¬N_4_Irish)       ∧

      (¬A_1_butterflies ∨ ¬A_2_butterflies) ∧
      (¬A_1_butterflies ∨ ¬A_3_butterflies) ∧
      (¬A_1_butterflies ∨ ¬A_4_butterflies) ∧
      (¬A_2_butterflies ∨ ¬A_3_butterflies) ∧
      (¬A_2_butterflies ∨ ¬A_4_butterflies) ∧
      (¬A_3_butterflies ∨ ¬A_4_butterflies) ∧

      (¬A_1_dolphins ∨ ¬A_2_dolphins) ∧
      (¬A_1_dolphins ∨ ¬A_3_dolphins) ∧
      (¬A_1_dolphins ∨ ¬A_4_dolphins) ∧
      (¬A_2_dolphins ∨ ¬A_3_dolphins) ∧
      (¬A_2_dolphins ∨ ¬A_4_dolphins) ∧
      (¬A_3_dolphins ∨ ¬A_4_dolphins) ∧

      (¬A_1_horses ∨ ¬A_2_horses)     ∧
      (¬A_1_horses ∨ ¬A_3_horses)     ∧
      (¬A_1_horses ∨ ¬A_4_horses)     ∧
      (¬A_2_horses ∨ ¬A_3_horses)     ∧
      (¬A_2_horses ∨ ¬A_4_horses)     ∧
      (¬A_3_horses ∨ ¬A_4_horses)     ∧

      (¬A_1_turtles ∨ ¬A_2_turtles)   ∧
      (¬A_1_turtles ∨ ¬A_3_turtles)   ∧
      (¬A_1_turtles ∨ ¬A_4_turtles)   ∧
      (¬A_2_turtles ∨ ¬A_3_turtles)   ∧
      (¬A_2_turtles ∨ ¬A_4_turtles)   ∧
      (¬A_3_turtles ∨ ¬A_4_turtles)   ∧

      (¬S_1_bowling ∨ ¬S_2_bowling)   ∧
      (¬S_1_bowling ∨ ¬S_3_bowling)   ∧
      (¬S_1_bowling ∨ ¬S_4_bowling)   ∧
      (¬S_2_bowling ∨ ¬S_3_bowling)   ∧
      (¬S_2_bowling ∨ ¬S_4_bowling)   ∧
      (¬S_3_bowling ∨ ¬S_4_bowling)   ∧

      (¬S_1_handball ∨ ¬S_2_handball) ∧
      (¬S_1_handball ∨ ¬S_3_handball) ∧
      (¬S_1_handball ∨ ¬S_4_handball) ∧
      (¬S_2_handball ∨ ¬S_3_handball) ∧
      (¬S_2_handball ∨ ¬S_4_handball) ∧
      (¬S_3_handball ∨ ¬S_4_handball) ∧

      (¬S_1_swimming ∨ ¬S_2_swimming) ∧
      (¬S_1_swimming ∨ ¬S_3_swimming) ∧
      (¬S_1_swimming ∨ ¬S_4_swimming) ∧
      (¬S_2_swimming ∨ ¬S_3_swimming) ∧
      (¬S_2_swimming ∨ ¬S_4_swimming) ∧
      (¬S_3_swimming ∨ ¬S_4_swimming) ∧

      (¬S_1_tennis ∨ ¬S_2_tennis)     ∧
      (¬S_1_tennis ∨ ¬S_3_tennis)     ∧
      (¬S_1_tennis ∨ ¬S_4_tennis)     ∧
      (¬S_2_tennis ∨ ¬S_3_tennis)     ∧
      (¬S_2_tennis ∨ ¬S_4_tennis)     ∧
      (¬S_3_tennis ∨ ¬S_4_tennis)
   ```
3. There are **two houses** between the person who likes **Bowling** and the person who likes **Swimming**:

   ```text
   (S_1_bowling ∧ S_4_swimming) ∨ (S_1_swimming ∧ S_4_bowling)
   ```

4. There is **one house** between the **Irish** person and the person who likes **Handball** on the left:

   ```text
   (S_1_handball ∧ N_3_Irish) ∨ (S_2_handball ∧ N_4_Irish)
   ```

5. The **second house** is **Black**:

   ```text
   C_2_black
   ```

6. There is **one house** between the person who likes **Horses** and the **Red** house on the right:

   ```text
   (A_1_horses ∧ C_3_red) ∨ (A_2_horses ∧ C_4_red)
   ```

7. The **American** lives **directly to the left** of the person who likes **Turtles**:

   ```text
   (N_1_American ∧ A_2_turtles) ∨ (N_2_American ∧ A_3_turtles) ∨ (N_3_American ∧ A_4_turtles)
   ```

8. There are **two houses** between the person who likes **Horses** and the person who likes **Butterflies** on the right:

   ```text
   (A_1_horses ∧ A_4_butterflies)
   ```

9. The person who likes **Bowling** lives somewhere **to the right** of the person who likes **Tennis**:

   ```text
   (S_1_tennis ∧ S_2_bowling) ∨ (S_1_tennis ∧ S_3_bowling) ∨ (S_1_tennis ∧ S_4_bowling) ∨ 
   (S_2_tennis ∧ S_3_bowling) ∨ (S_2_tennis ∧ S_4_bowling) ∨ (S_3_tennis ∧ S_4_bowling)
   ```

10. There is **one house** between the person who likes **Handball** and the **White** house on the right:

    ```text
    (S_1_handball ∧ C_3_white) ∨ (S_2_handball ∧ C_4_white)
    ```

11. The **British** lives in the **first house**:

    ```text
    N_1_British
    ```

### 2.3 Final CNF model

1. Each house has **exactly one value** for each property:<br>
   - At least one: 
      ```
      (C_1_black      ∨ C_1_blue      ∨ C_1_red      ∨ C_1_white)      ∧
      (C_2_black      ∨ C_2_blue      ∨ C_2_red      ∨ C_2_white)      ∧
      (C_3_black      ∨ C_3_blue      ∨ C_3_red      ∨ C_3_white)      ∧
      (C_4_black      ∨ C_4_blue      ∨ C_4_red      ∨ C_4_white)      ∧
      (N_1_American   ∨ N_1_British   ∨ N_1_Canadian ∨ N_1_Irish)      ∧
      (N_2_American   ∨ N_2_British   ∨ N_2_Canadian ∨ N_2_Irish)      ∧
      (N_3_American   ∨ N_3_British   ∨ N_3_Canadian ∨ N_3_Irish)      ∧
      (N_4_American   ∨ N_4_British   ∨ N_4_Canadian ∨ N_4_Irish)      ∧
      (A_1_butterflies ∨ A_1_dolphins ∨ A_1_horses   ∨ A_1_turtles)    ∧
      (A_2_butterflies ∨ A_2_dolphins ∨ A_2_horses   ∨ A_2_turtles)    ∧
      (A_3_butterflies ∨ A_3_dolphins ∨ A_3_horses   ∨ A_3_turtles)    ∧
      (A_4_butterflies ∨ A_4_dolphins ∨ A_4_horses   ∨ A_4_turtles)    ∧
      (S_1_bowling     ∨ S_1_handball ∨ S_1_swimming ∨ S_1_tennis)     ∧
      (S_2_bowling     ∨ S_2_handball ∨ S_2_swimming ∨ S_2_tennis)     ∧
      (S_3_bowling     ∨ S_3_handball ∨ S_3_swimming ∨ S_3_tennis)     ∧
      (S_4_bowling     ∨ S_4_handball ∨ S_4_swimming ∨ S_4_tennis) 
      ``` 
   - At most one: 
     ```
     (¬C_1_black ∨ ¬C_1_blue)      ∧
     (¬C_1_black ∨ ¬C_1_red)       ∧
     (¬C_1_black ∨ ¬C_1_white)     ∧
     (¬C_1_blue  ∨ ¬C_1_red)       ∧
     (¬C_1_blue  ∨ ¬C_1_white)     ∧
     (¬C_1_red   ∨ ¬C_1_white)     ∧

     (¬C_2_black ∨ ¬C_2_blue)      ∧
     (¬C_2_black ∨ ¬C_2_red)       ∧
     (¬C_2_black ∨ ¬C_2_white)     ∧
     (¬C_2_blue  ∨ ¬C_2_red)       ∧
     (¬C_2_blue  ∨ ¬C_2_white)     ∧
     (¬C_2_red   ∨ ¬C_2_white)     ∧

     (¬C_3_black ∨ ¬C_3_blue)      ∧
     (¬C_3_black ∨ ¬C_3_red)       ∧ 
     (¬C_3_black ∨ ¬C_3_white)     ∧
     (¬C_3_blue  ∨ ¬C_3_red)       ∧
     (¬C_3_blue  ∨ ¬C_3_white)     ∧ 
     (¬C_3_red   ∨ ¬C_3_white)     ∧

     (¬C_4_black ∨ ¬C_4_blue)      ∧
     (¬C_4_black ∨ ¬C_4_red)       ∧
     (¬C_4_black ∨ ¬C_4_white)     ∧
     (¬C_4_blue  ∨ ¬C_4_red)       ∧
     (¬C_4_blue  ∨ ¬C_4_white)     ∧
     (¬C_4_red   ∨ ¬C_4_white)     ∧

     (¬N_1_American ∨ ¬N_1_British)   ∧
     (¬N_1_American ∨ ¬N_1_Canadian)  ∧
     (¬N_1_American ∨ ¬N_1_Irish)     ∧
     (¬N_1_British  ∨ ¬N_1_Canadian)  ∧
     (¬N_1_British  ∨ ¬N_1_Irish)     ∧
     (¬N_1_Canadian ∨ ¬N_1_Irish)     ∧

     (¬N_2_American ∨ ¬N_2_British)   ∧
     (¬N_2_American ∨ ¬N_2_Canadian)  ∧
     (¬N_2_American ∨ ¬N_2_Irish)     ∧
     (¬N_2_British  ∨ ¬N_2_Canadian)  ∧
     (¬N_2_British  ∨ ¬N_2_Irish)     ∧
     (¬N_2_Canadian ∨ ¬N_2_Irish)     ∧

     (¬N_3_American ∨ ¬N_3_British)   ∧
     (¬N_3_American ∨ ¬N_3_Canadian)  ∧
     (¬N_3_American ∨ ¬N_3_Irish)     ∧
     (¬N_3_British  ∨ ¬N_3_Canadian)  ∧
     (¬N_3_British  ∨ ¬N_3_Irish)     ∧
     (¬N_3_Canadian ∨ ¬N_3_Irish)     ∧

     (¬N_4_American ∨ ¬N_4_British)   ∧
     (¬N_4_American ∨ ¬N_4_Canadian)  ∧
     (¬N_4_American ∨ ¬N_4_Irish)     ∧
     (¬N_4_British  ∨ ¬N_4_Canadian)  ∧
     (¬N_4_British  ∨ ¬N_4_Irish)     ∧
     (¬N_4_Canadian ∨ ¬N_4_Irish)     ∧

     (¬A_1_butterflies ∨ ¬A_1_dolphins) ∧
     (¬A_1_butterflies ∨ ¬A_1_horses)   ∧
     (¬A_1_butterflies ∨ ¬A_1_turtles)  ∧
     (¬A_1_dolphins    ∨ ¬A_1_horses)   ∧ 
     (¬A_1_dolphins    ∨ ¬A_1_turtles)  ∧
     (¬A_1_horses      ∨ ¬A_1_turtles)  ∧

     (¬A_2_butterflies ∨ ¬A_2_dolphins) ∧
     (¬A_2_butterflies ∨ ¬A_2_horses)   ∧
     (¬A_2_butterflies ∨ ¬A_2_turtles)  ∧
     (¬A_2_dolphins    ∨ ¬A_2_horses)   ∧
     (¬A_2_dolphins    ∨ ¬A_2_turtles)  ∧
     (¬A_2_horses      ∨ ¬A_2_turtles)  ∧

     (¬A_3_butterflies ∨ ¬A_3_dolphins) ∧
     (¬A_3_butterflies ∨ ¬A_3_horses)   ∧
     (¬A_3_butterflies ∨ ¬A_3_turtles)  ∧
     (¬A_3_dolphins    ∨ ¬A_3_horses)   ∧
     (¬A_3_dolphins    ∨ ¬A_3_turtles)  ∧
     (¬A_3_horses      ∨ ¬A_3_turtles)  ∧

     (¬A_4_butterflies ∨ ¬A_4_dolphins) ∧
     (¬A_4_butterflies ∨ ¬A_4_horses)   ∧
     (¬A_4_butterflies ∨ ¬A_4_turtles)  ∧
     (¬A_4_dolphins    ∨ ¬A_4_horses)   ∧
     (¬A_4_dolphins    ∨ ¬A_4_turtles)  ∧
     (¬A_4_horses      ∨ ¬A_4_turtles)  ∧

     (¬S_1_bowling   ∨ ¬S_1_handball) ∧
     (¬S_1_bowling   ∨ ¬S_1_swimming) ∧
     (¬S_1_bowling   ∨ ¬S_1_tennis)   ∧
     (¬S_1_handball  ∨ ¬S_1_swimming) ∧
     (¬S_1_handball  ∨ ¬S_1_tennis)   ∧
     (¬S_1_swimming  ∨ ¬S_1_tennis)   ∧

     (¬S_2_bowling   ∨ ¬S_2_handball) ∧
     (¬S_2_bowling   ∨ ¬S_2_swimming) ∧
     (¬S_2_bowling   ∨ ¬S_2_tennis)   ∧
     (¬S_2_handball  ∨ ¬S_2_swimming) ∧
     (¬S_2_handball  ∨ ¬S_2_tennis)   ∧
     (¬S_2_swimming  ∨ ¬S_2_tennis)   ∧

     (¬S_3_bowling   ∨ ¬S_3_handball) ∧
     (¬S_3_bowling   ∨ ¬S_3_swimming) ∧
     (¬S_3_bowling   ∨ ¬S_3_tennis)   ∧
     (¬S_3_handball  ∨ ¬S_3_swimming) ∧
     (¬S_3_handball  ∨ ¬S_3_tennis)   ∧
     (¬S_3_swimming  ∨ ¬S_3_tennis)   ∧

     (¬S_4_bowling   ∨ ¬S_4_handball) ∧
     (¬S_4_bowling   ∨ ¬S_4_swimming) ∧
     (¬S_4_bowling   ∨ ¬S_4_tennis)   ∧
     (¬S_4_handball  ∨ ¬S_4_swimming) ∧
     (¬S_4_handball  ∨ ¬S_4_tennis)   ∧
     (¬S_4_swimming  ∨ ¬S_4_tennis) 
     ``` 
2. Each property value is used **exactly once** among all houses:
   ```
   (¬C_1_black ∨ ¬C_2_black)      ∧
   (¬C_1_black ∨ ¬C_3_black)      ∧
   (¬C_1_black ∨ ¬C_4_black)      ∧
   (¬C_2_black ∨ ¬C_3_black)      ∧
   (¬C_2_black ∨ ¬C_4_black)      ∧
   (¬C_3_black ∨ ¬C_4_black)      ∧

   (¬C_1_blue  ∨ ¬C_2_blue)       ∧
   (¬C_1_blue  ∨ ¬C_3_blue)       ∧
   (¬C_1_blue  ∨ ¬C_4_blue)       ∧
   (¬C_2_blue  ∨ ¬C_3_blue)       ∧
   (¬C_2_blue  ∨ ¬C_4_blue)       ∧
   (¬C_3_blue  ∨ ¬C_4_blue)       ∧

   (¬C_1_red   ∨ ¬C_2_red)        ∧
   (¬C_1_red   ∨ ¬C_3_red)        ∧
   (¬C_1_red   ∨ ¬C_4_red)        ∧
   (¬C_2_red   ∨ ¬C_3_red)        ∧
   (¬C_2_red   ∨ ¬C_4_red)        ∧
   (¬C_3_red   ∨ ¬C_4_red)        ∧

   (¬C_1_white ∨ ¬C_2_white)      ∧
   (¬C_1_white ∨ ¬C_3_white)      ∧
   (¬C_1_white ∨ ¬C_4_white)      ∧
   (¬C_2_white ∨ ¬C_3_white)      ∧
   (¬C_2_white ∨ ¬C_4_white)      ∧
   (¬C_3_white ∨ ¬C_4_white)      ∧

   (¬N_1_American ∨ ¬N_2_American) ∧
   (¬N_1_American ∨ ¬N_3_American) ∧
   (¬N_1_American ∨ ¬N_4_American) ∧
   (¬N_2_American ∨ ¬N_3_American) ∧
   (¬N_2_American ∨ ¬N_4_American) ∧
   (¬N_3_American ∨ ¬N_4_American) ∧

   (¬N_1_British ∨ ¬N_2_British)   ∧
   (¬N_1_British ∨ ¬N_3_British)   ∧
   (¬N_1_British ∨ ¬N_4_British)   ∧
   (¬N_2_British ∨ ¬N_3_British)   ∧
   (¬N_2_British ∨ ¬N_4_British)   ∧
   (¬N_3_British ∨ ¬N_4_British)   ∧

   (¬N_1_Canadian ∨ ¬N_2_Canadian) ∧
   (¬N_1_Canadian ∨ ¬N_3_Canadian) ∧
   (¬N_1_Canadian ∨ ¬N_4_Canadian) ∧
   (¬N_2_Canadian ∨ ¬N_3_Canadian) ∧
   (¬N_2_Canadian ∨ ¬N_4_Canadian) ∧
   (¬N_3_Canadian ∨ ¬N_4_Canadian) ∧

   (¬N_1_Irish ∨ ¬N_2_Irish)       ∧
   (¬N_1_Irish ∨ ¬N_3_Irish)       ∧
   (¬N_1_Irish ∨ ¬N_4_Irish)       ∧
   (¬N_2_Irish ∨ ¬N_3_Irish)       ∧
   (¬N_2_Irish ∨ ¬N_4_Irish)       ∧
   (¬N_3_Irish ∨ ¬N_4_Irish)       ∧

   (¬A_1_butterflies ∨ ¬A_2_butterflies) ∧
   (¬A_1_butterflies ∨ ¬A_3_butterflies) ∧
   (¬A_1_butterflies ∨ ¬A_4_butterflies) ∧
   (¬A_2_butterflies ∨ ¬A_3_butterflies) ∧
   (¬A_2_butterflies ∨ ¬A_4_butterflies) ∧
   (¬A_3_butterflies ∨ ¬A_4_butterflies) ∧

   (¬A_1_dolphins ∨ ¬A_2_dolphins) ∧
   (¬A_1_dolphins ∨ ¬A_3_dolphins) ∧
   (¬A_1_dolphins ∨ ¬A_4_dolphins) ∧
   (¬A_2_dolphins ∨ ¬A_3_dolphins) ∧
   (¬A_2_dolphins ∨ ¬A_4_dolphins) ∧
   (¬A_3_dolphins ∨ ¬A_4_dolphins) ∧

   (¬A_1_horses ∨ ¬A_2_horses)     ∧
   (¬A_1_horses ∨ ¬A_3_horses)     ∧
   (¬A_1_horses ∨ ¬A_4_horses)     ∧
   (¬A_2_horses ∨ ¬A_3_horses)     ∧
   (¬A_2_horses ∨ ¬A_4_horses)     ∧
   (¬A_3_horses ∨ ¬A_4_horses)     ∧

   (¬A_1_turtles ∨ ¬A_2_turtles)   ∧
   (¬A_1_turtles ∨ ¬A_3_turtles)   ∧
   (¬A_1_turtles ∨ ¬A_4_turtles)   ∧
   (¬A_2_turtles ∨ ¬A_3_turtles)   ∧
   (¬A_2_turtles ∨ ¬A_4_turtles)   ∧
   (¬A_3_turtles ∨ ¬A_4_turtles)   ∧

   (¬S_1_bowling ∨ ¬S_2_bowling)   ∧
   (¬S_1_bowling ∨ ¬S_3_bowling)   ∧
   (¬S_1_bowling ∨ ¬S_4_bowling)   ∧
   (¬S_2_bowling ∨ ¬S_3_bowling)   ∧
   (¬S_2_bowling ∨ ¬S_4_bowling)   ∧
   (¬S_3_bowling ∨ ¬S_4_bowling)   ∧

   (¬S_1_handball ∨ ¬S_2_handball) ∧
   (¬S_1_handball ∨ ¬S_3_handball) ∧
   (¬S_1_handball ∨ ¬S_4_handball) ∧
   (¬S_2_handball ∨ ¬S_3_handball) ∧
   (¬S_2_handball ∨ ¬S_4_handball) ∧
   (¬S_3_handball ∨ ¬S_4_handball) ∧

   (¬S_1_swimming ∨ ¬S_2_swimming) ∧
   (¬S_1_swimming ∨ ¬S_3_swimming) ∧
   (¬S_1_swimming ∨ ¬S_4_swimming) ∧
   (¬S_2_swimming ∨ ¬S_3_swimming) ∧
   (¬S_2_swimming ∨ ¬S_4_swimming) ∧
   (¬S_3_swimming ∨ ¬S_4_swimming) ∧

   (¬S_1_tennis ∨ ¬S_2_tennis)     ∧
   (¬S_1_tennis ∨ ¬S_3_tennis)     ∧
   (¬S_1_tennis ∨ ¬S_4_tennis)     ∧
   (¬S_2_tennis ∨ ¬S_3_tennis)     ∧
   (¬S_2_tennis ∨ ¬S_4_tennis)     ∧
   (¬S_3_tennis ∨ ¬S_4_tennis)
   ```
3. There are **two houses** between the person who likes **Bowling** and the person who likes **Swimming**:
   ```
   (S_1_bowling ∨ S_1_swimming) ∧ (S_1_bowling ∨ S_4_bowling) ∧ 
   (S_4_swimming ∨ S_1_swimming) ∧ (S_4_swimming ∨ S_4_bowling)
   ```
4. There is **one house** between the **Irish** person and the person who likes **Handball** on the left:
   ```
   (S_1_handball ∨ S_2_handball) ∧ 
   (S_1_handball ∨ N_4_Irish)    ∧
   (N_3_Irish    ∨ S_2_handball) ∧ 
   (N_3_Irish    ∨ N_4_Irish)
   ```
5. The **second house** is **Black**:
   ```
   C_2_black
   ```
6. There is **one house** between the person who likes **Horses** and the **Red** house on the right:
   ```
   (A_1_horses ∨ A_2_horses) ∧ 
   (A_1_horses ∨ C_4_red)    ∧ 
   (C_3_red    ∨ A_2_horses) ∧ 
   (C_3_red    ∨ C_4_red)
   ```
7. The **American** lives **directly to the left** of the person who likes **Turtles**:
   ```
   (N_1_American ∨ N_2_American ∨ N_3_American) ∧
   (N_1_American ∨ N_2_American ∨ A_4_turtles)  ∧
   (N_1_American ∨ A_3_turtles  ∨ N_3_American) ∧
   (N_1_American ∨ A_3_turtles  ∨ A_4_turtles)  ∧
   (A_2_turtles  ∨ N_2_American ∨ N_3_American) ∧
   (A_2_turtles  ∨ N_2_American ∨ A_4_turtles)  ∧
   (A_2_turtles  ∨ A_3_turtles  ∨ N_3_American) ∧
   (A_2_turtles  ∨ A_3_turtles  ∨ A_4_turtles)
   ```
8. There are **two houses** between the person who likes **Horses** and the person who likes **Butterflies** on the right:
   ```
   (A_1_horses ∧ A_4_butterflies)
   ```
9. The person who likes **Bowling** lives somewhere **to the right** of the person who likes **Tennis**:
    ```
    (S_1_tennis ∨ S_2_tennis ∨ S_3_tennis ∨ S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ S_3_tennis ∨ S_2_bowling ∨ S_3_bowling ∨ ¬S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ S_3_tennis ∨ S_2_bowling ∨ ¬S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ S_3_tennis ∨ S_2_bowling ∨ ¬S_3_bowling ∨ ¬S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ S_3_tennis ∨ ¬S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ S_3_tennis ∨ ¬S_2_bowling ∨ S_3_bowling ∨ ¬S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ S_3_tennis ∨ ¬S_2_bowling ∨ ¬S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ S_3_tennis ∨ ¬S_2_bowling ∨ ¬S_3_bowling ∨ ¬S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ ¬S_3_tennis ∨ S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ ¬S_3_tennis ∨ S_2_bowling ∨ ¬S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ ¬S_3_tennis ∨ ¬S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ S_2_tennis ∨ ¬S_3_tennis ∨ ¬S_2_bowling ∨ ¬S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ ¬S_2_tennis ∨ S_3_tennis ∨ S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ ¬S_2_tennis ∨ S_3_tennis ∨ ¬S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ ¬S_2_tennis ∨ ¬S_3_tennis ∨ S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (S_1_tennis ∨ ¬S_2_tennis ∨ ¬S_3_tennis ∨ ¬S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (¬S_1_tennis ∨ S_2_tennis ∨ S_3_tennis ∨ S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (¬S_1_tennis ∨ S_2_tennis ∨ ¬S_3_tennis ∨ S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (¬S_1_tennis ∨ ¬S_2_tennis ∨ S_3_tennis ∨ S_2_bowling ∨ S_3_bowling ∨ S_4_bowling) ∧
   (¬S_1_tennis ∨ ¬S_2_tennis ∨ ¬S_3_tennis ∨ S_2_bowling ∨ S_3_bowling ∨ S_4_bowling)
    ```
10. There is **one house** between the person who likes **Handball** and the **White** house on the right:
    ```
    (S_1_handball ∨ S_2_handball) ∧
    (S_1_handball ∨ C_4_white)    ∧
    (C_3_white    ∨ S_2_handball) ∧
    (C_3_white    ∨ C_4_white)
    ```
11. The **British** lives in the **first house**:
    ```
    N_1_British
    ```

### 2.4 CNF clause count estimation

| №  | Constraint | CNF clauses |
|----|------------|-------------|
| 1 | At least one | 16 |
| 2 | At most one  | 96 |
| 3  | Uniqueness constraints | 96 |
| 4  | Two houses between Bowling and Swimming | 4 |
| 5  | Handball is left of Irish with one house between | 4 |
| 6  | Second house is Black | 1 |
| 7  | One house between Horses and Red (Red on the right) | 4 |
| 7  | American is directly left of Turtles | 8 |
| 9  | Two houses between Horses and Butterflies (Butterflies on right) | 2 |
| 10  | Bowling is to the right of Tennis | 20 |
| 11 | One house between Handball and White (White on the right) | 4 |
| 12 | British lives in the first house | 1 |



## 3. Transformation of the model into the DIMACS format

After obtaining all clauses in CNF, the model must be converted into the DIMACS format in order to check its satisfiability using a SAT solver and, if a solution exists, retrieve the concrete assignment of variables.

### 3.1 Logical variable indexing

For this purpose, each logical variable is assigned a unique numerical identifier according to its position in the model. SAT solvers operate exclusively on such numerical representations. The correspondence table is provided below:

| №  | Variable    | №  |   Variable     |
| -- | ----------- | -- | -------------- |
| 1  | C₁_black    | 33 | A₁_butterflies |
| 2  | C₁_blue     | 34 | A₁_dolphins    |
| 3  | C₁_red      | 35 | A₁_horses      |
| 4  | C₁_white    | 36 | A₁_turtles     |
| 5  | C₂_black    | 37 | A₂_butterflies |
| 6  | C₂_blue     | 38 | A₂_dolphins    |
| 7  | C₂_red      | 39 | A₂_horses      |
| 8  | C₂_white    | 40 | A₂_turtles     |
| 9  | C₃_black    | 41 | A₃_butterflies |
| 10 | C₃_blue     | 42 | A₃_dolphins    |
| 11 | C₃_red      | 43 | A₃_horses      |
| 12 | C₃_white    | 44 | A₃_turtles     |
| 13 | C₄_black    | 45 | A₄_butterflies |
| 14 | C₄_blue     | 46 | A₄_dolphins    |
| 15 | C₄_red      | 47 | A₄_horses      |
| 16 | C₄_white    | 48 | A₄_turtles     |
| 17 | N₁_American | 49 | S₁_bowling     |
| 18 | N₁_British  | 50 | S₁_handball    |
| 19 | N₁_Canadian | 51 | S₁_swimming    |
| 20 | N₁_Irish    | 52 | S₁_tennis      |
| 21 | N₂_American | 53 | S₂_bowling     |
| 22 | N₂_British  | 54 | S₂_handball    |
| 23 | N₂_Canadian | 55 | S₂_swimming    |
| 24 | N₂_Irish    | 56 | S₂_tennis      |
| 25 | N₃_American | 57 | S₃_bowling     |
| 26 | N₃_British  | 58 | S₃_handball    |
| 27 | N₃_Canadian | 59 | S₃_swimming    |
| 28 | N₃_Irish    | 60 | S₃_tennis      |
| 29 | N₄_American | 61 | S₄_bowling     |
| 30 | N₄_British  | 62 | S₄_handball    |
| 31 | N₄_Canadian | 63 | S₄_swimming    |
| 32 | N₄_Irish    | 64 | S₄_tennis      |

### 3.2 DIMACS format requirements

The DIMACS structure imposes the following transformation rules:

* The file must begin with the line
  **`p cnf <number_of_variables> <number_of_clauses>`**.
* Logical negation `¬` is replaced with the `-` sign placed before the variable number.
* Disjunction `∨` is represented by spaces between variable numbers.
* Conjunction `∧` is not written explicitly — **each line in a DIMACS file corresponds to a single clause**.
* Every clause must **end with the number `0`**, which marks its termination.

> Thus, a CNF formula is a conjunction (logical “and”) of multiple disjunctions (logical “or”), each consisting of literals — variables or their negations. Each line in a DIMACS file lists the literals of a single clause, followed by `0`.

### 3.3 Final DIMACS file

```dimacs
p cnf 64 256
1 2 3 4 0
-1 -2 0
-1 -3 0
-1 -4 0
-2 -3 0
-2 -4 0
-3 -4 0
5 6 7 8 0
-5 -6 0
-5 -7 0
-5 -8 0
-6 -7 0
-6 -8 0
-7 -8 0
9 10 11 12 0
-9 -10 0
-9 -11 0
-9 -12 0
-10 -11 0
-10 -12 0
-11 -12 0
13 14 15 16 0
-13 -14 0
-13 -15 0
-13 -16 0
-14 -15 0
-14 -16 0
-15 -16 0
-1 -5 0
-1 -9 0
-1 -13 0
-5 -9 0
-5 -13 0
-9 -13 0
-2 -6 0
-2 -10 0
-2 -14 0
-6 -10 0
-6 -14 0
-10 -14 0
-3 -7 0
-3 -11 0
-3 -15 0
-7 -11 0
-7 -15 0
-11 -15 0
-4 -8 0
-4 -12 0
-4 -16 0
-8 -12 0
-8 -16 0
-12 -16 0
17 18 19 20 0
-17 -18 0
-17 -19 0
-17 -20 0
-18 -19 0
-18 -20 0
-19 -20 0
21 22 23 24 0
-21 -22 0
-21 -23 0
-21 -24 0
-22 -23 0
-22 -24 0
-23 -24 0
25 26 27 28 0
-25 -26 0
-25 -27 0
-25 -28 0
-26 -27 0
-26 -28 0
-27 -28 0
29 30 31 32 0
-29 -30 0
-29 -31 0
-29 -32 0
-30 -31 0
-30 -32 0
-31 -32 0
-17 -21 0
-17 -25 0
-17 -29 0
-21 -25 0
-21 -29 0
-25 -29 0
-18 -22 0
-18 -26 0
-18 -30 0
-22 -26 0
-22 -30 0
-26 -30 0
-19 -23 0
-19 -27 0
-19 -31 0
-23 -27 0
-23 -31 0
-27 -31 0
-20 -24 0
-20 -28 0
-20 -32 0
-24 -28 0
-24 -32 0
-28 -32 0
33 34 35 36 0
-33 -34 0
-33 -35 0
-33 -36 0
-34 -35 0
-34 -36 0
-35 -36 0
37 38 39 40 0
-37 -38 0
-37 -39 0
-37 -40 0
-38 -39 0
-38 -40 0
-39 -40 0
41 42 43 44 0
-41 -42 0
-41 -43 0
-41 -44 0
-42 -43 0
-42 -44 0
-43 -44 0
45 46 47 48 0
-45 -46 0
-45 -47 0
-45 -48 0
-46 -47 0
-46 -48 0
-47 -48 0
-33 -37 0
-33 -41 0
-33 -45 0
-37 -41 0
-37 -45 0
-41 -45 0
-34 -38 0
-34 -42 0
-34 -46 0
-38 -42 0
-38 -46 0
-42 -46 0
-35 -39 0
-35 -43 0
-35 -47 0
-39 -43 0
-39 -47 0
-43 -47 0
-36 -40 0
-36 -44 0
-36 -48 0
-40 -44 0
-40 -48 0
-44 -48 0
49 50 51 52 0
-49 -50 0
-49 -51 0
-49 -52 0
-50 -51 0
-50 -52 0
-51 -52 0
53 54 55 56 0
-53 -54 0
-53 -55 0
-53 -56 0
-54 -55 0
-54 -56 0
-55 -56 0
57 58 59 60 0
-57 -58 0
-57 -59 0
-57 -60 0
-58 -59 0
-58 -60 0
-59 -60 0
61 62 63 64 0
-61 -62 0
-61 -63 0
-61 -64 0
-62 -63 0
-62 -64 0
-63 -64 0
-49 -53 0
-49 -57 0
-49 -61 0
-53 -57 0
-53 -61 0
-57 -61 0
-50 -54 0
-50 -58 0
-50 -62 0
-54 -58 0
-54 -62 0
-58 -62 0
-51 -55 0
-51 -59 0
-51 -63 0
-55 -59 0
-55 -63 0
-59 -63 0
-52 -56 0
-52 -60 0
-52 -64 0
-56 -60 0
-56 -64 0
-60 -64 0
49 51 0
49 61 0
63 51 0
63 61 0
50 54 0
50 32 0
28 54 0
28 32 0
5 0
35 39 0
35 15 0
11 39 0
11 15 0
17 21 25 0
17 21 48 0
17 44 25 0
17 44 48 0
40 21 25 0
40 21 48 0
40 44 25 0
40 44 48 0
35 0
45 0
52 56 60 53 57 61 0
52 56 60 53 57 -61 0
52 56 60 53 -57 61 0
52 56 60 53 -57 -61 0
52 56 60 -53 57 61 0
52 56 60 -53 57 -61 0
52 56 60 -53 -57 61 0
52 56 60 -53 -57 -61 0
52 56 -60 53 57 61 0
52 56 -60 53 -57 61 0
52 56 -60 -53 57 61 0
52 56 -60 -53 -57 61 0
52 -56 60 53 57 61 0
52 -56 60 -53 57 61 0
52 -56 -60 53 57 61 0
52 -56 -60 -53 57 61 0
-52 56 60 53 57 61 0
-52 56 -60 53 57 61 0
-52 -56 60 53 57 61 0
-52 -56 -60 53 57 61 0
50 54 0
50 16 0
12 54 0
12 16 0
18 0
```

## 4. Use of a SAT solver

To check the satisfiability of the model (satisfiable/unsatisfiable), the SAT solver [**CryptoMiniSat5**](https://www.msoos.org/cryptominisat/) was used.

### 4.1 About CryptoMiniSat5

**CryptoMiniSat5** is a modern SAT solver optimized for handling large and complex Boolean formulas in CNF. It features efficient search heuristics, support for XOR constraints, and allows fast solution finding for problems presented in the DIMACS format.

### 4.2 SAT solver output  
Running our DIMACS file through CryptoMiniSat5 produces the following output:

```
s SATISFIABLE
v -1 2 -3 -4 5 -6 -7 -8 -9 -10 11 -12 -13 -14 -15 16 -17 18 -19 -20 21 -22 -23 
v -24 -25 -26 27 -28 -29 -30 -31 32 -33 -34 35 -36 -37 38 -39 -40 -41 -42 -43 
v 44 45 -46 -47 -48 -49 -50 51 -52 -53 54 -55 -56 -57 -58 -59 60 61 -62 -63 -64 0
```

### 4.3 Final assignment of properties to houses

| Property     | House #1 | House #2 | House #3 | House #4 |
|--------------|----------|----------|----------|----------|
| **Color**        |    blue      |  black         |      red    |  white        | 
| **Nationality**  |  British        |    American      |   Canadian       |   Irish       | 
| **Animal**       |   horses       |   dolphins       |     turtles     |   butterflies       | 
| **Sport**        |   swimming       |   handball       |   tennis       |  bowling        |
