# Cookie Puzzle

![Cookie Puzzle Photo](C:\Users\admin\Downloads\cookie_puzzle.jpg)

Aunt Geralda knows that one of Ana, Bruno, Cecilia, Daniela or Eduardo ate all
the cookies. She also knows that the guilty always lie and the innocent always
tell the truth.

- Bruno says, "The culprit is either Eduardo or Daniela".
- Eduardo says: "The guilty person is a girl."
- Finally, Daniela says, "if Bruno is guilty, then Cecilia is innocent."

Who ate the cookies? Who is innocent?

---

# Predicate Logic Solution

To determine who ate the cookie, we solve the problem using **predicate logic**. The solution follows all necessary steps, starting from defining the objects and formalizing the statements in logical form, and continuing with the transformation of the knowledge base and the application of the **resolution method** to derive the final conclusion.

## Contents
1. **Vocabulary**
   - Constants
   - Domains
   - Variables
   - Predicates
2. **Knowledge Base Formalization**
3. **CNF Transformation**
4. **Knowledge Base Clauses**
5. **First-Order Resolution with Set-of-Support Strategy**
   - 5.1 Daniela
   - 5.2 Bruno
   - 5.3 Eduardo
   - 5.4 Cecilia
   - 5.5 Ana
6. **Automated Solver Verification**
   - 6.1 DPLL SAT Solver
   - 6.2 Z3 Playground
7. **Conclusion**

## 1. Vocabulary
Based on the problem statement, the main elements of the formal language can be identified: *constants*, *variables*, and *predicates*.

### Constants

Constants represent the specific individuals mentioned in the problem.

| Object   | Constant | Information |
|----------|----------|-------------|
| Ana      | a        | female      |
| Bruno    | b        | male        |
| Cecilia  | c        | female      |
| Daniela  | d        | female      |
| Eduardo  | e        | male        |

### Domains 

To ensure the rules address only the relevant individuals, we define the set of all suspects:

$$
S = \{a, b, c, d, e\}
$$

### Variables

- `X` —  first-order variables ranging over the domain of suspects $S$.

### Predicates

- `guilty(X)` — a predicate that is true if and only if the individual `X` is guilty.
- `girl(X)` — true if individual `X` is female.

## 2. Knowledge Base Formalization

1. **At least one of Ana, Bruno, Cecilia, Daniela, or Eduardo is guilty:**

$$
guilty(a) \lor guilty(b) \lor guilty(c) \lor guilty(d) \lor guilty(e)
$$

2. **Ana is a female:**

$$
girl(a)
$$

3. **Bruno is a male:**

$$
\lnot girl(b)
$$

4. **Cecilia is a female:**

$$
girl(c)
$$

5. **Daniela is a female:**

$$
girl(d)
$$

6. **Eduardo is a male:**

$$
\lnot girl(e)
$$

7. **Bruno says: “The culprit is either Eduardo or Daniela”:**

$$
\lnot guilty(b) \leftrightarrow \big( guilty(e) \lor guilty(d) \big)
$$


8. **Eduardo says: “The guilty person is a girl”:**

$$
\lnot guilty(e) \leftrightarrow \exists X  \big( guilty(X) \land girl(X) \big)
$$


9. **Daniela says: “If Bruno is guilty, then Cecilia is innocent”:**

$$
\lnot guilty(d) \leftrightarrow \big( guilty(b) \rightarrow \lnot guilty(c) \big)
$$

## 3. CNF Transformation

1. **At least one of Ana, Bruno, Cecilia, Daniela, or Eduardo is guilty:**

   **Formula:** 

   $$
   guilty(a) \lor guilty(b) \lor guilty(c) \lor guilty(d) \lor guilty(e)
   $$

   **Resulting clauses:** 

   ```
   guilty(a) v guilty(b) v guilty(c) v guilty(d) v guilty(e)
   ```
2. **Ana is a female:**

   **Formula:** 

   $$
   girl(a)
   $$

   **Resulting clauses:** 
   ```
   girl(a)
   ```

3. **Bruno is a male:**
   
   **Formula:** 

   $$
   \lnot girl(b)
   $$

   **Resulting clauses:** 
   ```
   ¬girl(b)
   ```

4. **Cecilia is a female:**

   **Formula:** 

   $$
   girl(c)
   $$

   **Resulting clauses:** 
   ```
   girl(c)
   ```

5. **Daniela is a female:**

   **Formula:** 

   $$
   girl(d)
   $$

   **Resulting clauses:** 
   ```
   girl(d)
   ```

6. **Eduardo is a male:**
   
   **Formula:** 

   $$
   \lnot girl(e)
   $$

   **Resulting clauses:** 
   ```
   ¬girl(e)
   ```

7. **Bruno says: “The culprit is either Eduardo or Daniela”:**

      **Formula:**  

      $$
      \lnot guilty(b) \leftrightarrow \big( guilty(e) \lor guilty(d) \big)
      $$

      **Conversion to CNF:**  
      $$
      \begin{aligned}
      \lnot guilty(b) \leftrightarrow (guilty(e) \lor guilty(d))
      &\equiv (\lnot guilty(b) \rightarrow (guilty(e) \lor guilty(d))) \\
      &\quad \land ((guilty(e) \lor guilty(d)) \rightarrow \lnot guilty(b)) \\
      &\equiv (\lnot(\lnot guilty(b)) \lor (guilty(e) \lor guilty(d))) \\
      &\quad \land (\lnot (guilty(e) \lor guilty(d)) \lor guilty(b)) \\
      &\equiv (guilty(b) \lor guilty(e) \lor guilty(d)) \\ 
      &\quad \land ((\lnot guilty(e) \land \lnot guilty(d)) \lor \lnot guilty(b)) \\
      &\equiv (guilty(b) \lor guilty(e) \lor guilty(d)) \\
      &\quad \land (\lnot guilty(e) \lor \lnot guilty(b)) \\
      &\quad \land (\lnot guilty(d) \lor \lnot guilty(b))
      \end{aligned}
      $$

   **Resulting clauses:** 
   ```
   guilty(b) v guilty(e) v guilty(d)
   ¬guilty(e) v ¬guilty(b)
   ¬guilty(d) v ¬guilty(b)
   ```

8. **Eduardo says: “The guilty person is a girl”:**

   **Formula:** 

   $$
   \lnot guilty(e) \leftrightarrow \exists X \big( guilty(X) \land girl(X) \big)
   $$

   **Conversion to CNF:** 

   $$
   \begin{aligned}
   \lnot guilty(e) \leftrightarrow \exists X \big( guilty(X) \land girl(X) \big)
   &\equiv (\lnot guilty(e) \rightarrow \exists X (guilty(X) \land girl(X))) \\
   &\quad \land (\exists X  (guilty(X) \land girl(X)) \rightarrow \lnot guilty(e)) \\
   &\equiv (\lnot (\lnot guilty(e)) \lor \exists X (guilty(X) \land girl(X))) \\
   &\quad \land (\lnot \exists X (guilty(X) \land girl(X)) \lor \lnot guilty(e)) \\
   &\equiv (guilty(e) \lor \exists X (guilty(X) \land girl(X))) \\
   &\quad \land (\forall X \lnot (guilty(X) \land girl(X)) \lor \lnot guilty(e)) \\
   &\equiv \exists X  ((guilty(e) \lor  guilty(X)) \\
   &\quad \land (guilty(e) \lor girl(X))) \\
   &\quad \land \forall X (\lnot guilty(X) \lor \lnot girl(X) \lor \lnot guilty(e)) \\
   &\equiv ((guilty(e) \lor  guilty(SK_1)) \\
   &\quad \land (guilty(e) \lor girl(SK_1))) \\
   &\quad \land (\lnot guilty(X) \lor \lnot girl(X) \lor \lnot guilty(e)) 
   \end{aligned}
   $$

   **Resulting clauses:** 

   ```
   guilty(e) v guilty(SK₁)
   guilty(e) v girl(SK₁)
   ¬guilty(e) v ¬guilty(X) v ¬girl(X)
   ```

9.  **Daniela says: “If Bruno is guilty, then Cecilia is innocent”:**

   **Formula:** 
   $$
   \lnot guilty(d) \leftrightarrow \big( guilty(b) \rightarrow \lnot guilty(c) \big)
   $$

   **Conversion to CNF:** 

   - Eliminate implications:
     
     $$
     guilty(b) \rightarrow \lnot guilty(c)
     \equiv \lnot guilty(b) \lor \lnot guilty(c)
     $$

   - Expand equivalences: 

     $$
     \begin{aligned}
     \lnot guilty(d) \leftrightarrow (\lnot guilty(b) \lor \lnot guilty(c))
     &\equiv (\lnot guilty(d) \rightarrow (\lnot guilty(b) \lor \lnot guilty(c))) \\
     &\quad \land ((\lnot guilty(b) \lor \lnot guilty(c)) \rightarrow \lnot guilty(d)) \\
     &\equiv (\lnot (\lnot guilty(d)) \lor (\lnot guilty(b) \lor \lnot guilty(c))) \\
     &\quad \land (\lnot (\lnot guilty(b) \lor \lnot guilty(c)) \lor \lnot guilty(d)) \\
     &\equiv (guilty(d) \lor (\lnot guilty(b) \lor \lnot guilty(c))) \\
     &\quad \land ((guilty(b) \land guilty(c)) \lor \lnot guilty(d)) \\
     &\equiv (guilty(d) \lor \lnot guilty(b) \lor \lnot guilty(c)) \\
     &\quad \land (guilty(b) \lor \lnot guilty(d)) \\
     &\quad \land (guilty(c) \lor \lnot guilty(d))
     \end{aligned}
     $$

   **Resulting clauses:** 

   ```
   guilty(d) v ¬guilty(b) v ¬guilty(c)
   guilty(b) v ¬guilty(d)
   guilty(c) v ¬guilty(d)
   ```

## 4. Knowledge Base Clauses

After converting the formal representation of the knowledge base into CNF, we removed all duplicates and obtained the final numbered list of clauses:

|  № | Knowledge Base Clause                                       |
| -: | ----------------------------------------------------------- |
| 1 | `guilty(a) v guilty(b) v guilty(c) v guilty(d) v guilty(e)`|
| 2    | `girl(a)`                         |
| 3    | `¬girl(b)`                         |
| 4    | `girl(c)`                         |
| 5    | `girl(d)`                         |
| 6    | `¬girl(e)`                         |
| 7 | `guilty(b) v guilty(e) v guilty(d)`                         |
| 8 | `¬guilty(e) v ¬guilty(b)`                                    |
| 9 | `¬guilty(d) v ¬guilty(b)`                                    |
| 10 | `guilty(e) v guilty(SK₁)`                                    |
| 11 | `guilty(e) v girl(SK₁)`                                    |
| 12 | `¬guilty(e) v ¬guilty(X) v ¬girl(X)`             |
| 13 | `guilty(d) v ¬guilty(b) v ¬guilty(c)`                       |
| 14 | `guilty(b) v ¬guilty(d)`                                    |
| 15 | `guilty(c) v ¬guilty(d)`                                    |


## 5. First-Order Resolution with Set-of-Support Strategy

The **first-order resolution method** is a sound and complete inference technique for **first-order logic**, which allows reasoning with predicates, constants, and quantified variables. In this approach, logical conclusions are derived by applying the **resolution rule** together with **unification** to eliminate variables and match complementary literals.

The **set-of-support resolution method** is a refinement of this approach, where resolution is applied only to clauses that involve a specially selected set of support, typically related to the goal being proved. This approach restricts the search space, makes the reasoning process more goal-directed, and helps reach a contradiction or the desired conclusion more efficiently.

**Core idea:**

* All clauses are divided into two sets:

  * **Knowledge Base (KB)** — trusted facts and rules
  * **Set of Support (SOS)** — clauses related to the negation of the goal

**Resolution rule:**

* Resolution is applied **only if at least one parent clause belongs to the SOS**
* **Unification** is used to match variables across clauses in first-order logic

**Why it works:**

* Reduces the search space
* Prevents unnecessary resolutions
* Guides reasoning toward a contradiction or proof

**Goal:**

* Derive the **empty clause (□)**, which confirms the conclusion

**Result:**

* Enables structured and efficient reasoning in **first-order logic**

### 5.1 Daniela

First, we test the hypothesis that **Daniela is innocent**: `¬guilty(d)`. To do this, we apply the resolution method in order to confirm or refute this assumption:

|    № | Derived Clause | Resolution Step / Description           |
| ---: | :------------: | --------------------------------------- |
|   16 |  `guilty(d)`   | Negated conclusion                      |
|   17 |  `¬guilty(b)`   | Resolution of clauses **9** and **16** |
|   18 |  `¬guilty(d)`  | Resolution of clauses **14** and **17**  |
|   19 |  `□`  | Resolution of clauses **16** and **18**  |

As a result of the resolution process, an **empty clause** is derived, which indicates a logical contradiction when the negation of the hypothesis is assumed. Therefore, the statement `¬guilty(d)` is true, and we can add it to the knowledge base as **Fact 16**.

### 5.2 Bruno

Knowing that **Daniela is innocent**, we can assume that her statement is true: if **Bruno is guilty**, then **Cecilia is innocent**. Based on this, we test the hypothesis that Bruno is innocent: `¬guilty(b)`.

| №    |           Derived Clause            | Resolution Step / Description           |
| :--- | :---------------------------------: | --------------------------------------- |
| 17   |             `guilty(b)`             | Negated conclusion                      |
| 18   |            `guilty(d) v ¬guilty(b) v ¬guilty(d)`             | Resolution of clauses **13** and **15**  |
| 19   |            `¬guilty(b)`             | Tautology elimination of clause **18** |
| 20   |            `□`             | Resolution of clauses **17** and **19**  |

As a result of the resolution with the negation of the hypothesis that **Bruno is innocent**, an **empty clause** was derived, which proves his innocence. Consequently, we add the fact `¬guilty(b)` to the knowledge base as **clause 17**.

### 5.3 Eduardo

We already have proofs that **Daniela** and **Bruno** are innocent. Bruno claims that the guilty person is either **Eduardo** or **Daniela**. However, since we already know that **Daniela is innocent**, we can test the hypothesis that **Eduardo is guilty**: `guilty(e)`.

| №    |     Derived Clause      | Resolution Step / Description           |
| ---- | :---------------------: | --------------------------------------- |
| 18   |      `¬guilty(e)`       | Negated conclusion                      |
| 19   | `guilty(b) v guilty(d)` | Resolution of clauses **7** and **18** |
| 20   |       `guilty(b)`       | Resolution of clauses **16** and **19** |
| 21   |           `□`           | Resolution of clauses **17** and **20** |

As a result of the resolution process, we obtained an **empty clause**, which means that the hypothesis of Eduardo’s guilt is true. Thus, we have identified the person who ate the cookie.

### 5.4 Cecilia

We know that **Eduard is guilty**, and we have recorded this hypothesis as axiom **number 18**. Now, in order to verify that **Cecilia is innocent**, we will test the hypothesis: `¬guilty(c)`.

| №    |     Derived Clause      | Resolution Step / Description           |
| ---- | :---------------------: | --------------------------------------- |
| 19   |       `guilty(c)`       | Negated conclusion                      |
| 20   |      `guilty(d) v ¬guilty(d) v ¬guilty(c)`       | Resolution of clauses **13** and **14**  |
| 21   |           `¬guilty(c)`           | Tautology elimination of clause **20** |
| 22   |           `□`           | Resolution of clauses **19** and **21** |

As a result of the resolution with the negation of the hypothesis that **Cecilia is innocent**, an **empty clause** was derived, which proves her innocence. Consequently, we add the fact `¬guilty(c)` to the knowledge base as **Clause 19**.

### 5.5 Ana

Since **Eduardo** has been identified **as** **guilty** and **Bruno**, **Cecilia**, and **Daniela** **as innocent**, we proceed to verify the remaining suspect by testing the hypothesis that **Ana is innocent**: `¬guilty(a)`.

| №    |     Derived Clause      | Resolution Step / Description           |
| ---- | :---------------------: | --------------------------------------- |
| 20   |       `guilty(a)`       | Negated conclusion                      |
| 21   |      `guilty(a) v guilty(c) v guilty(d) v guilty(e)`       | Resolution of clauses **1** and **17**  |
| 22   |      `guilty(a) v guilty(d) v guilty(e)`       | Resolution of clauses **19** and **21**  |
| 23   |      `guilty(a) v guilty(e)`       | Resolution of clauses **16** and **22**  |
| 24   |      `¬guilty(e) v ¬guilty(a) v ¬girl(a)`       | Unification: substitute **{X / a}** into **clause 12**  |
| 25   |      `¬guilty(a) v ¬girl(a)`       | Resolution of clauses **23** and **24**  |
| 26   |      `¬girl(a)`       | Resolution of clauses **20** and **25**  |
| 27   |      `□`       | Resolution of clauses **2** and **26**  |

The resolution process starting from the negated hypothesis `guilty(a)` resulted in the derivation of an **empty clause**, which proves that **Ana is innocent**. Moreover, this result shows that the statement claiming that at least one of the girls is guilty is false.


## 6. **Automated Solver Verification**
   
To ensure the correctness of our solution, we will verify it using automated SAT/SMT solvers, namely **[DPLL SAT Solver](https://www.inf.ufpr.br/dpasqualin/d3-dpll/)** and **[Z3 Playground](https://microsoft.github.io/z3guide/playground/Freeform%20Editing/)**.

### 6.1 DPLL SAT Solver

**[DPLL SAT Solver](https://www.inf.ufpr.br/dpasqualin/d3-dpll/)** is an implementation of the **Davis-Putnam-Logemann-Loveland (DPLL)** algorithm for checking the satisfiability of Boolean formulas in Conjunctive Normal Form (CNF). This algorithm uses **unit clause propagation** and **non-chronological backtracking** for efficient solution search.

To run the SAT solver correctly, our knowledge base is transformed into the format it accepts:  
- The `guilty` predicate is removed, leaving only the literals represented as CNF clauses.  
- A minus `-` indicates the negation of a literal.  

**Example input:**

```
a b c d e
-a -b
-a -c
-a -d
-a -e
-b -c
-b -d
-b -e
-c -d
-c -e
-d -e
b e d
e a c d
d -b -c
b -d
c -d
```

**Solution:** 

```
SATISFIABLE e -a -b -d -c
```

### 6.2 Z3 Playground

**[Z3 Playground](https://microsoft.github.io/z3guide/playground/Freeform%20Editing/)** is a web interface for the **Z3 SMT solver**, which allows checking the satisfiability of logical formulas written in the SMT-LIB language. Z3 supports Boolean, integer, and other types of variables, enabling the formalization of more complex logical dependencies.

For Z3, our knowledge base is translated into the correct SMT-LIB format:

```smt
; ----- Variables -----
(declare-fun A () Bool) ; Ana
(declare-fun B () Bool) ; Bruno
(declare-fun C () Bool) ; Cecilia
(declare-fun D () Bool) ; Daniela
(declare-fun E () Bool) ; Eduardo

; ----- Exactly one guilty -----

; At least one
(assert (or A B C D E))

; At most one
(assert (or (not A) (not B)))
(assert (or (not A) (not C)))
(assert (or (not A) (not D)))
(assert (or (not A) (not E)))

(assert (or (not B) (not C)))
(assert (or (not B) (not D)))
(assert (or (not B) (not E)))

(assert (or (not C) (not D)))
(assert (or (not C) (not E)))

(assert (or (not D) (not E)))

; ----- Bruno -----
; Bruno says: "E or D"
; guilty -> lies, innocent -> tells truth
(assert (= (not B) (or E D)))

; ----- Eduardo -----
; Eduardo says: "guilty person is a girl" = A or C or D
(assert (= (not E) (or A C D)))

; ----- Daniela -----
; Daniela says: "if B then not C"
(assert (= (not D) (=> B (not C))))

; ----- Check -----
(check-sat)
(get-model)
```

**Output:**

```
sat
(
  (define-fun A () Bool
    false)
  (define-fun D () Bool
    false)
  (define-fun B () Bool
    false)
  (define-fun C () Bool
    false)
  (define-fun E () Bool
    true)
)
```

> Variables `true/false` represent “guilty/innocent”.

## 7. Conclusion

Having completed the entire process of solving in predicate logic using the resolution method with the set-of-support strategy, we concluded that the constant **e (Eduardo)** is the person who *ate the cookies*. All others — **a (Ana), b (Bruno), c (Cecilia), d (Daniela)** — *are innocent*.

![Result Cookie Puzzle Photo](C:\Users\admin\Downloads\result_cookie_puzzle.png)