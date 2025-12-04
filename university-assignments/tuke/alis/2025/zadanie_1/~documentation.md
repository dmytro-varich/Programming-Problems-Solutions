# Репрезентация переменных и их доменов

Всего **16 переменных**, которые пресдставляют собою одно значение и репрезентовано как (Объект, Свойство).

Например:
- дом №1 и его цвет → переменная Color₁
- дом №3 и его национальность → Nationality₃

## Определение переменных

```css
Color₁, Color₂, Color₃, Color₄
Nationality₁, Nationality₂, Nationality₃, Nationality₄
Animal₁, Animal₂, Animal₃, Animal₄
Sport₁,  Sport₂,  Sport₃,  Sport₄
```


```matematica   
C₁, C₂, C₃, C₄       (colors)
N₁, N₂, N₃, N₄       (nationalities)
A₁, A₂, A₃, A₄       (animals)
S₁, S₂, S₃, S₄       (sports)
```

## Переменные и их домены

Colorᵢ, для i ∈ {1,2,3,4}
Domain(Colorᵢ) = {black, blue, red, white}

Nationalityᵢ, для i ∈ {1,2,3,4}
Domain(Nationalityᵢ) = {American, British, Canadian, Irish}

Animalᵢ, для i ∈ {1,2,3,4}
Domain(Animalᵢ) = {butterflies, dolphins, horses, turtles}

Sportᵢ, для i ∈ {1,2,3,4}
Domain(Sportᵢ) = {bowling, handball, swimming, tennis}

```
C_i ∈ {black, blue, red, white}
N_i ∈ {American, British, Canadian, Irish}
A_i ∈ {butterflies, dolphins, horses, turtles}
S_i ∈ {bowling, handball, swimming, tennis}
```

Где i = 1,2,3,4 — номер дома.

https://chatgpt.com/share/691dbc2d-ba24-800a-a3ac-0f35d24dc141

(S_1_bowling ∧ S_4_swimming)
∨
(S_1_swimming ∧ S_4_bowling)

(S_1_handball ∧ N_3_Irish)
∨
(S_2_handball ∧ N_4_Irish)


C_2_black


(A_1_horses ∧ C_3_red)
∨
(A_2_horses ∧ C_4_red)

(N_1_American ∧ A_2_turtles)
∨
(N_2_American ∧ A_3_turtles)
∨
(N_3_American ∧ A_4_turtles)

A_1_horses ∧ A_4_butterflies

(S_1_tennis ∧ S_2_bowling)
∨
(S_1_tennis ∧ S_3_bowling)
∨
(S_1_tennis ∧ S_4_bowling)
∨
(S_2_tennis ∧ S_3_bowling)
∨
(S_2_tennis ∧ S_4_bowling)
∨
(S_3_tennis ∧ S_4_bowling)


(S_1_handball ∧ C_3_white)
∨
(S_2_handball ∧ C_4_white)

N_1_British


У нас 4 свойства: Color, Nationality, Animal, Sport.
У каждого свойства:

4 дома

4 возможных значения

Обычно делаем так (минимальный, не избыточный вариант):

Для каждого свойства:

Для каждого дома — “ровно одно значение свойства”

4 дома ⇒ 4 ограничении вида:
ровно одно из {X_i1, X_i2, X_i3, X_i4}

Для каждого значения — “значение не может быть у двух домов сразу” (at most one)

4 значения ⇒ 4 ограничения вида:
не более одного из {X_1j, X_2j, X_3j, X_4j}

Итого на одно свойство:
4 (per house) + 4 (per value) = 8 ограничений
Итого на одно свойство:
4 (per house) + 4 (per value) = 8 ограничений

На все 4 свойства:
4 × 8 = 32 доменных ограничения на уровне логики

Это то, что ты можешь писать в документации как:

“Для каждого дома: ровно один цвет / спорт / животное / национальность.”

“Каждый цвет / спорт / животное / национальность используется не более одного раза.”


(S_1_bowling ∨ S_1_swimming)
∧ (S_1_bowling ∨ S_4_bowling)
∧ (S_4_swimming ∨ S_1_swimming)
∧ (S_4_swimming ∨ S_4_bowling)


(S_1_handball ∨ S_2_handball)
∧ (S_1_handball ∨ N_4_Irish)
∧ (N_3_Irish ∨ S_2_handball)
∧ (N_3_Irish ∨ N_4_Irish)


(A_1_horses ∨ A_2_horses)
∧ (A_1_horses ∨ C_4_red)
∧ (C_3_red ∨ A_2_horses)
∧ (C_3_red ∨ C_4_red)


(N_1_American ∨ N_2_American ∨ N_3_American)
∧ (N_1_American ∨ N_2_American ∨ A_4_turtles)
∧ (N_1_American ∨ A_3_turtles ∨ N_3_American)
∧ (N_1_American ∨ A_3_turtles ∨ A_4_turtles)
∧ (A_2_turtles ∨ N_2_American ∨ N_3_American)
∧ (A_2_turtles ∨ N_2_American ∨ A_4_turtles)
∧ (A_2_turtles ∨ A_3_turtles ∨ N_3_American)
∧ (A_2_turtles ∨ A_3_turtles ∨ A_4_turtles)

A_1_horses ∧ A_4_butterflies

C_2_black

N_1_British

(S_1_handball ∨ S_2_handball) ∧
(S_1_handball ∨ C_4_white) ∧
(C_3_white ∨ S_2_handball) ∧
(C_3_white ∨ C_4_white)

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




(C_1_1 ∨ C_1_2 ∨ C_1_3 ∨ C_1_4)
(¬C_1_1 ∨ ¬C_1_2)
(¬C_1_1 ∨ ¬C_1_3)
(¬C_1_1 ∨ ¬C_1_4)
(¬C_1_2 ∨ ¬C_1_3)
(¬C_1_2 ∨ ¬C_1_4)
(¬C_1_3 ∨ ¬C_1_4)
(C_2_1 ∨ C_2_2 ∨ C_2_3 ∨ C_2_4)
(¬C_2_1 ∨ ¬C_2_2)
(¬C_2_1 ∨ ¬C_2_3)
(¬C_2_1 ∨ ¬C_2_4)
(¬C_2_2 ∨ ¬C_2_3)
(¬C_2_2 ∨ ¬C_2_4)
(¬C_2_3 ∨ ¬C_2_4)
(C_3_1 ∨ C_3_2 ∨ C_3_3 ∨ C_3_4)
(¬C_3_1 ∨ ¬C_3_2)
(¬C_3_1 ∨ ¬C_3_3)
(¬C_3_1 ∨ ¬C_3_4)
(¬C_3_2 ∨ ¬C_3_3)
(¬C_3_2 ∨ ¬C_3_4)
(¬C_3_3 ∨ ¬C_3_4)
(C_4_1 ∨ C_4_2 ∨ C_4_3 ∨ C_4_4)
(¬C_4_1 ∨ ¬C_4_2)
(¬C_4_1 ∨ ¬C_4_3)
(¬C_4_1 ∨ ¬C_4_4)
(¬C_4_2 ∨ ¬C_4_3)
(¬C_4_2 ∨ ¬C_4_4)
(¬C_4_3 ∨ ¬C_4_4)
(¬C_1_1 ∨ ¬C_2_1)
(¬C_1_1 ∨ ¬C_3_1)
(¬C_1_1 ∨ ¬C_4_1)
(¬C_2_1 ∨ ¬C_3_1)
(¬C_2_1 ∨ ¬C_4_1)
(¬C_3_1 ∨ ¬C_4_1)
(¬C_1_2 ∨ ¬C_2_2)
(¬C_1_2 ∨ ¬C_3_2)
(¬C_1_2 ∨ ¬C_4_2)
(¬C_2_2 ∨ ¬C_3_2)
(¬C_2_2 ∨ ¬C_4_2)
(¬C_3_2 ∨ ¬C_4_2)
(¬C_1_3 ∨ ¬C_2_3)
(¬C_1_3 ∨ ¬C_3_3)
(¬C_1_3 ∨ ¬C_4_3)
(¬C_2_3 ∨ ¬C_3_3)
(¬C_2_3 ∨ ¬C_4_3)
(¬C_3_3 ∨ ¬C_4_3)
(¬C_1_4 ∨ ¬C_2_4)
(¬C_1_4 ∨ ¬C_3_4)
(¬C_1_4 ∨ ¬C_4_4)
(¬C_2_4 ∨ ¬C_3_4)
(¬C_2_4 ∨ ¬C_4_4)
(¬C_3_4 ∨ ¬C_4_4)
(N_1_1 ∨ N_1_2 ∨ N_1_3 ∨ N_1_4)
(¬N_1_1 ∨ ¬N_1_2)
(¬N_1_1 ∨ ¬N_1_3)
(¬N_1_1 ∨ ¬N_1_4)
(¬N_1_2 ∨ ¬N_1_3)
(¬N_1_2 ∨ ¬N_1_4)
(¬N_1_3 ∨ ¬N_1_4)
(N_2_1 ∨ N_2_2 ∨ N_2_3 ∨ N_2_4)
(¬N_2_1 ∨ ¬N_2_2)
(¬N_2_1 ∨ ¬N_2_3)
(¬N_2_1 ∨ ¬N_2_4)
(¬N_2_2 ∨ ¬N_2_3)
(¬N_2_2 ∨ ¬N_2_4)
(¬N_2_3 ∨ ¬N_2_4)
(N_3_1 ∨ N_3_2 ∨ N_3_3 ∨ N_3_4)
(¬N_3_1 ∨ ¬N_3_2)
(¬N_3_1 ∨ ¬N_3_3)
(¬N_3_1 ∨ ¬N_3_4)
(¬N_3_2 ∨ ¬N_3_3)
(¬N_3_2 ∨ ¬N_3_4)
(¬N_3_3 ∨ ¬N_3_4)
(N_4_1 ∨ N_4_2 ∨ N_4_3 ∨ N_4_4)
(¬N_4_1 ∨ ¬N_4_2)
(¬N_4_1 ∨ ¬N_4_3)
(¬N_4_1 ∨ ¬N_4_4)
(¬N_4_2 ∨ ¬N_4_3)
(¬N_4_2 ∨ ¬N_4_4)
(¬N_4_3 ∨ ¬N_4_4)
(¬N_1_1 ∨ ¬N_2_1)
(¬N_1_1 ∨ ¬N_3_1)
(¬N_1_1 ∨ ¬N_4_1)
(¬N_2_1 ∨ ¬N_3_1)
(¬N_2_1 ∨ ¬N_4_1)
(¬N_3_1 ∨ ¬N_4_1)
(¬N_1_2 ∨ ¬N_2_2)
(¬N_1_2 ∨ ¬N_3_2)
(¬N_1_2 ∨ ¬N_4_2)
(¬N_2_2 ∨ ¬N_3_2)
(¬N_2_2 ∨ ¬N_4_2)
(¬N_3_2 ∨ ¬N_4_2)
(¬N_1_3 ∨ ¬N_2_3)
(¬N_1_3 ∨ ¬N_3_3)
(¬N_1_3 ∨ ¬N_4_3)
(¬N_2_3 ∨ ¬N_3_3)
(¬N_2_3 ∨ ¬N_4_3)
(¬N_3_3 ∨ ¬N_4_3)
(¬N_1_4 ∨ ¬N_2_4)
(¬N_1_4 ∨ ¬N_3_4)
(¬N_1_4 ∨ ¬N_4_4)
(¬N_2_4 ∨ ¬N_3_4)
(¬N_2_4 ∨ ¬N_4_4)
(¬N_3_4 ∨ ¬N_4_4)
(A_1_1 ∨ A_1_2 ∨ A_1_3 ∨ A_1_4)
(¬A_1_1 ∨ ¬A_1_2)
(¬A_1_1 ∨ ¬A_1_3)
(¬A_1_1 ∨ ¬A_1_4)
(¬A_1_2 ∨ ¬A_1_3)
(¬A_1_2 ∨ ¬A_1_4)
(¬A_1_3 ∨ ¬A_1_4)
(A_2_1 ∨ A_2_2 ∨ A_2_3 ∨ A_2_4)
(¬A_2_1 ∨ ¬A_2_2)
(¬A_2_1 ∨ ¬A_2_3)
(¬A_2_1 ∨ ¬A_2_4)
(¬A_2_2 ∨ ¬A_2_3)
(¬A_2_2 ∨ ¬A_2_4)
(¬A_2_3 ∨ ¬A_2_4)
(A_3_1 ∨ A_3_2 ∨ A_3_3 ∨ A_3_4)
(¬A_3_1 ∨ ¬A_3_2)
(¬A_3_1 ∨ ¬A_3_3)
(¬A_3_1 ∨ ¬A_3_4)
(¬A_3_2 ∨ ¬A_3_3)
(¬A_3_2 ∨ ¬A_3_4)
(¬A_3_3 ∨ ¬A_3_4)
(A_4_1 ∨ A_4_2 ∨ A_4_3 ∨ A_4_4)
(¬A_4_1 ∨ ¬A_4_2)
(¬A_4_1 ∨ ¬A_4_3)
(¬A_4_1 ∨ ¬A_4_4)
(¬A_4_2 ∨ ¬A_4_3)
(¬A_4_2 ∨ ¬A_4_4)
(¬A_4_3 ∨ ¬A_4_4)
(¬A_1_1 ∨ ¬A_2_1)
(¬A_1_1 ∨ ¬A_3_1)
(¬A_1_1 ∨ ¬A_4_1)
(¬A_2_1 ∨ ¬A_3_1)
(¬A_2_1 ∨ ¬A_4_1)
(¬A_3_1 ∨ ¬A_4_1)
(¬A_1_2 ∨ ¬A_2_2)
(¬A_1_2 ∨ ¬A_3_2)
(¬A_1_2 ∨ ¬A_4_2)
(¬A_2_2 ∨ ¬A_3_2)
(¬A_2_2 ∨ ¬A_4_2)
(¬A_3_2 ∨ ¬A_4_2)
(¬A_1_3 ∨ ¬A_2_3)
(¬A_1_3 ∨ ¬A_3_3)
(¬A_1_3 ∨ ¬A_4_3)
(¬A_2_3 ∨ ¬A_3_3)
(¬A_2_3 ∨ ¬A_4_3)
(¬A_3_3 ∨ ¬A_4_3)
(¬A_1_4 ∨ ¬A_2_4)
(¬A_1_4 ∨ ¬A_3_4)
(¬A_1_4 ∨ ¬A_4_4)
(¬A_2_4 ∨ ¬A_3_4)
(¬A_2_4 ∨ ¬A_4_4)
(¬A_3_4 ∨ ¬A_4_4)
(S_1_1 ∨ S_1_2 ∨ S_1_3 ∨ S_1_4)
(¬S_1_1 ∨ ¬S_1_2)
(¬S_1_1 ∨ ¬S_1_3)
(¬S_1_1 ∨ ¬S_1_4)
(¬S_1_2 ∨ ¬S_1_3)
(¬S_1_2 ∨ ¬S_1_4)
(¬S_1_3 ∨ ¬S_1_4)
(S_2_1 ∨ S_2_2 ∨ S_2_3 ∨ S_2_4)
(¬S_2_1 ∨ ¬S_2_2)
(¬S_2_1 ∨ ¬S_2_3)
(¬S_2_1 ∨ ¬S_2_4)
(¬S_2_2 ∨ ¬S_2_3)
(¬S_2_2 ∨ ¬S_2_4)
(¬S_2_3 ∨ ¬S_2_4)
(S_3_1 ∨ S_3_2 ∨ S_3_3 ∨ S_3_4)
(¬S_3_1 ∨ ¬S_3_2)
(¬S_3_1 ∨ ¬S_3_3)
(¬S_3_1 ∨ ¬S_3_4)
(¬S_3_2 ∨ ¬S_3_3)
(¬S_3_2 ∨ ¬S_3_4)
(¬S_3_3 ∨ ¬S_3_4)
(S_4_1 ∨ S_4_2 ∨ S_4_3 ∨ S_4_4)
(¬S_4_1 ∨ ¬S_4_2)
(¬S_4_1 ∨ ¬S_4_3)
(¬S_4_1 ∨ ¬S_4_4)
(¬S_4_2 ∨ ¬S_4_3)
(¬S_4_2 ∨ ¬S_4_4)
(¬S_4_3 ∨ ¬S_4_4)
(¬S_1_1 ∨ ¬S_2_1)
(¬S_1_1 ∨ ¬S_3_1)
(¬S_1_1 ∨ ¬S_4_1)
(¬S_2_1 ∨ ¬S_3_1)
(¬S_2_1 ∨ ¬S_4_1)
(¬S_3_1 ∨ ¬S_4_1)
(¬S_1_2 ∨ ¬S_2_2)
(¬S_1_2 ∨ ¬S_3_2)
(¬S_1_2 ∨ ¬S_4_2)
(¬S_2_2 ∨ ¬S_3_2)
(¬S_2_2 ∨ ¬S_4_2)
(¬S_3_2 ∨ ¬S_4_2)
(¬S_1_3 ∨ ¬S_2_3)
(¬S_1_3 ∨ ¬S_3_3)
(¬S_1_3 ∨ ¬S_4_3)
(¬S_2_3 ∨ ¬S_3_3)
(¬S_2_3 ∨ ¬S_4_3)
(¬S_3_3 ∨ ¬S_4_3)
(¬S_1_4 ∨ ¬S_2_4)
(¬S_1_4 ∨ ¬S_3_4)
(¬S_1_4 ∨ ¬S_4_4)
(¬S_2_4 ∨ ¬S_3_4)
(¬S_2_4 ∨ ¬S_4_4)
(¬S_3_4 ∨ ¬S_4_4)


(S_1_1 ∨ S_1_3)
(S_1_1 ∨ S_4_1)
(S_4_3 ∨ S_1_3)
(S_4_3 ∨ S_4_1)

(S_1_2 ∨ S_2_2)
(S_1_2 ∨ N_4_4)
(N_3_4 ∨ S_2_2)
(N_3_4 ∨ N_4_4)

(A_1_3 ∨ A_2_3)
(A_1_3 ∨ C_4_3)
(C_3_3 ∨ A_2_3)
(C_3_3 ∨ C_4_3)

(N_1_1 ∨ N_2_1 ∨ N_3_1)
(N_1_1 ∨ N_2_1 ∨ A_4_4)
(N_1_1 ∨ A_3_4 ∨ N_3_1)
(N_1_1 ∨ A_3_4 ∨ A_4_4)
(A_2_4 ∨ N_2_1 ∨ N_3_1)
(A_2_4 ∨ N_2_1 ∨ A_4_4)
(A_2_4 ∨ A_3_4 ∨ N_3_1)
(A_2_4 ∨ A_3_4 ∨ A_4_4)

(A_1_3)
(A_4_1)

(C_2_1)

(N_1_2)

(S_1_2 ∨ S_2_2)
(S_1_2 ∨ C_4_4)
(C_3_4 ∨ S_2_2)
(C_3_4 ∨ C_4_4)

(S_1_4 ∨ S_2_4 ∨ S_3_4 ∨ S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ S_3_4 ∨ S_2_1 ∨ S_3_1 ∨ ¬S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ S_3_4 ∨ S_2_1 ∨ ¬S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ S_3_4 ∨ S_2_1 ∨ ¬S_3_1 ∨ ¬S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ S_3_4 ∨ ¬S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ S_3_4 ∨ ¬S_2_1 ∨ S_3_1 ∨ ¬S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ S_3_4 ∨ ¬S_2_1 ∨ ¬S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ S_3_4 ∨ ¬S_2_1 ∨ ¬S_3_1 ∨ ¬S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ ¬S_3_4 ∨ S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ ¬S_3_4 ∨ S_2_1 ∨ ¬S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ ¬S_3_4 ∨ ¬S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ S_2_4 ∨ ¬S_3_4 ∨ ¬S_2_1 ∨ ¬S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ ¬S_2_4 ∨ S_3_4 ∨ S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ ¬S_2_4 ∨ S_3_4 ∨ ¬S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ ¬S_2_4 ∨ ¬S_3_4 ∨ S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(S_1_4 ∨ ¬S_2_4 ∨ ¬S_3_4 ∨ ¬S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(¬S_1_4 ∨ S_2_4 ∨ S_3_4 ∨ S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(¬S_1_4 ∨ S_2_4 ∨ ¬S_3_4 ∨ S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(¬S_1_4 ∨ ¬S_2_4 ∨ S_3_4 ∨ S_2_1 ∨ S_3_1 ∨ S_4_1) ∧
(¬S_1_4 ∨ ¬S_2_4 ∨ ¬S_3_4 ∨ S_2_1 ∨ S_3_1 ∨ S_4_1)