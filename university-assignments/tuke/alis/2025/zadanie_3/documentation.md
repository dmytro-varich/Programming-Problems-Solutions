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
   - Variables
   - Predicates
2. **Knowledge Base Formalization**
3. **CNF Transformation**
4. **Knowledge Base Clauses**
5. **Resolution with Set-of-Support Strategy**
  - 5.1 Daniela
  - 5.2 Cecilia
  - 5.3 Bruno
  - 5.4 Eduardo
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

### Variables

- `X` — a variable representing an arbitrary individual in the problem domain.
- `Y` — another variable representing an arbitrary individual in the problem domain.

### Predicates

- `guilty(X)` — a predicate that is true if and only if the individual `X` is guilty.

## 2. Knowledge Base Formalization

1. **At least one person is guilty:**

$$
\exists X; guilty(X)
$$

2. **Exactly one person is guilty:**

$$
\exists X \Big( guilty(X) \land \forall Y ((Y \neq X) \rightarrow \lnot guilty(Y)) \Big)
$$

3. **Bruno says: “The culprit is either Eduardo or Daniela”:**

$$
\lnot guilty(b) \leftrightarrow \big( guilty(e) \lor guilty(d) \big)
$$


4. **Eduardo says: “The guilty person is a girl”:**

$$
\lnot guilty(e) \leftrightarrow \big( guilty(a) \lor guilty(c) \lor guilty(d) \big)
$$


5. **Daniela says: “If Bruno is guilty, then Cecilia is innocent”:**

$$
\lnot guilty(d) \leftrightarrow \big( guilty(b) \rightarrow \lnot guilty(c) \big)
$$

## 3. CNF Transformation

1. **At least one person is guilty:**

   **Formula:** 

   $$
   \exists X; guilty(X)
   $$

   **Conversion to CNF:** 

   $$
   \begin{aligned}
   \exists X\; guilty(X)
   &\equiv guilty(a) \lor guilty(b) \lor guilty(c) \lor guilty(d) \lor guilty(e)
   \end{aligned}
   $$

   **Resulting clauses:** 
   ```
   guilty(a) v guilty(b) v guilty(c) v guilty(d) v guilty(e)
   ```

2. **Exactly one person is guilty:**

   **Formula:** 

   $$
   \exists X \Big( guilty(X) \land \forall Y ((Y \neq X) \rightarrow \lnot guilty(Y)) \Big)
   $$

   **Conversion to CNF:** 

   - Eliminate the quantifiers: 
     - $X, Y \in \{a, b, c, d, e\}$
     - $\exists X; guilty(X) ;\rightarrow; guilty(a) \lor guilty(b) \lor guilty(c) \lor guilty(d) \lor guilty(e) \quad \text{(at least one guilty)}$
     - $\forall Y ; ((Y \neq X) \rightarrow \lnot guilty(Y)) ;\rightarrow; \text{all pairs } (X \neq Y) \text{ give } \lnot guilty(X) \lor \lnot guilty(Y) \quad \text{(at most one guilty)}$

   - Combine them:
     $$
     \begin{aligned}
     & (guilty(a) \lor guilty(b) \lor guilty(c) \lor guilty(d) \lor guilty(e)) \\
     & \land (\lnot guilty(a) \lor \lnot guilty(b)) \\
     & \land (\lnot guilty(a) \lor \lnot guilty(c)) \\
     & \land (\lnot guilty(a) \lor \lnot guilty(d)) \\
     & \land (\lnot guilty(a) \lor \lnot guilty(e)) \\
     & \land (\lnot guilty(b) \lor \lnot guilty(c)) \\
     & \land (\lnot guilty(b) \lor \lnot guilty(d)) \\
     &\land (\lnot guilty(b) \lor \lnot guilty(e)) \\
     & \land (\lnot guilty(c) \lor \lnot guilty(d)) \\
     & \land (\lnot guilty(c) \lor \lnot guilty(e)) \\
     & \land (\lnot guilty(d) \lor \lnot guilty(e))
     \end{aligned}
     $$

   **Resulting clauses:** 
   
   ```
   guilty(a) v guilty(b) v guilty(c) v guilty(d) v guilty(e)
   ¬guilty(a) v ¬guilty(b)
   ¬guilty(a) v ¬guilty(c)
   ¬guilty(a) v ¬guilty(d)
   ¬guilty(a) v ¬guilty(e)
   ¬guilty(b) v ¬guilty(c)
   ¬guilty(b) v ¬guilty(d)
   ¬guilty(b) v ¬guilty(d)
   ¬guilty(b) v ¬guilty(e)
   ¬guilty(c) v ¬guilty(d)
   ¬guilty(c) v ¬guilty(e)
   ¬guilty(d) v ¬guilty(e)
   ```
   
3. **Bruno says: “The culprit is either Eduardo or Daniela”:**

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

4. **Eduardo says: “The guilty person is a girl”:**

   **Formula:** 

   $$
   \lnot guilty(e) \leftrightarrow \big( guilty(a) \lor guilty(c) \lor guilty(d) \big)
   $$

   **Conversion to CNF:** 

   $$
   \begin{aligned}
   \lnot guilty(e) \leftrightarrow (guilty(a) \lor guilty(c) \lor guilty(d))
   &\equiv (\lnot guilty(e) \rightarrow (guilty(a) \lor guilty(c) \lor guilty(d))) \\
   &\quad \land ((guilty(a) \lor guilty(c) \lor guilty(d)) \rightarrow \lnot guilty(e)) \\
   &\equiv (\lnot (\lnot guilty(e)) \lor (guilty(a) \lor guilty(c) \lor guilty(d))) \\
   &\quad \land (\lnot (guilty(a) \lor guilty(c) \lor guilty(d)) \lor \lnot guilty(e)) \\
   &\equiv (guilty(e) \lor (guilty(a) \lor guilty(c) \lor guilty(d))) \\
   &\quad \land ((\lnot guilty(a) \land \lnot guilty(c) \land \lnot guilty(d)) \lor \lnot guilty(e)) \\
   &\equiv (guilty(e) \lor guilty(a) \lor guilty(c) \lor guilty(d)) \\
   &\quad \land (\lnot guilty(a) \lor \lnot guilty(e)) \\
   &\quad \land (\lnot guilty(c) \lor \lnot guilty(e)) \\
   &\quad \land (\lnot guilty(d) \lor \lnot guilty(e))
   \end{aligned}
   $$

   **Resulting clauses:** 

   ```
   guilty(e) v guilty(a) v guilty(c) v guilty(d)
   ¬guilty(a) v ¬guilty(e)
   ¬guilty(c) v ¬guilty(e)
   ¬guilty(d) v ¬guilty(e)
   ```

5. **Daniela says: “If Bruno is guilty, then Cecilia is innocent”:**

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
|  1 | `guilty(a) v guilty(b) v guilty(c) v guilty(d) v guilty(e)` |
|  2 | `¬guilty(a) v ¬guilty(b)`                                   |
|  3 | `¬guilty(a) v ¬guilty(c)`                                   |
|  4 | `¬guilty(a) v ¬guilty(d)`                                   |
|  5 | `¬guilty(a) v ¬guilty(e)`                                   |
|  6 | `¬guilty(b) v ¬guilty(c)`                                   |
|  7 | `¬guilty(b) v ¬guilty(d)`                                   |
|  8 | `¬guilty(b) v ¬guilty(e)`                                   |
|  9 | `¬guilty(c) v ¬guilty(d)`                                   |
| 10 | `¬guilty(c) v ¬guilty(e)`                                   |
| 11 | `¬guilty(d) v ¬guilty(e)`                                   |
| 12 | `guilty(b) v guilty(e) v guilty(d)`                         |
| 13 | `guilty(e) v guilty(a) v guilty(c) v guilty(d)`             |
| 14 | `guilty(d) v ¬guilty(b) v ¬guilty(c)`                       |
| 15 | `guilty(b) v ¬guilty(d)`                                    |
| 16 | `guilty(c) v ¬guilty(d)`                                    |

## 5. Resolution with Set-of-Support Strategy 

The **set-of-support resolution method** is a logical inference strategy in which resolution is applied only to clauses that involve a specially selected set of support, typically related to the goal being proved. This approach restricts the search space, makes the reasoning process more goal-directed, and helps reach a contradiction or the desired conclusion more efficiently.

**Core idea:**
- All clauses are divided into two sets:
  - **Knowledge Base (KB)** — trusted facts and rules
  - **Set of Support (SOS)** — clauses related to the negation of the goal

**Resolution rule:**
- Resolution is applied **only if at least one parent clause belongs to the SOS**

**Why it works:**
- Reduces the search space  
- Prevents unnecessary resolutions  
- Guides reasoning toward a contradiction or proof

**Goal:**
- Derive the **empty clause (□)**, which confirms the conclusion

**Result:**

- More efficient and structured logical inference

### 5.1 Daniela

First, we test the hypothesis that **Daniela is innocent**: `¬guilty(d)`. To do this, we apply the resolution method in order to confirm or refute this assumption:

|    № | Derived Clause | Resolution Step / Description           |
| ---: | :------------: | --------------------------------------- |
|   17 |  `guilty(d)`   | Negated conclusion                      |
|   18 |  `guilty(b)`   | Resolution of clauses **15** and **17** |
|   19 |  `guilty(c)`   | Resolution of clauses **16** and **17** |
|   20 |  `¬guilty(c)`  | Resolution of clauses **6** and **18**  |
|   21 |      `□`       | Resolution of clauses **19** and **20** |

As a result of the resolution process, an **empty clause** is derived, which indicates a logical contradiction when the negation of the hypothesis is assumed. Therefore, the statement `¬guilty(d)` is true, and we can add it to the knowledge base as **Fact 17**.

### 5.2 Cecilia

Knowing that **Daniela is innocent**, we can assume that her statement is true: if **Bruno is guilty**, then **Cecilia is innocent**. Based on this, we test the hypothesis that Cecilia is innocent: `¬guilty(c)`.


| №    |     Derived Clause      | Resolution Step / Description           |
| ---- | :---------------------: | --------------------------------------- |
| 18   |       `guilty(c)`       | Negated conclusion                      |
| 19   |      `¬guilty(b)`       | Resolution of clauses **6** and **18**  |
| 20   |      `¬guilty(d)`       | Resolution of clauses **9** and **18**  |
| 21   |      `¬guilty(e)`       | Resolution of clauses **10** and **18** |
| 22   | `guilty(e) v guilty(d)` | Resolution of clauses **12** and **19** |
| 23   |       `guilty(e)`       | Resolution of clauses **20** and **22** |
| 24   |           `□`           | Resolution of clauses **21** and **23** |

As a result of the resolution process, an **empty clause** was derived, thereby proving that Cecilia is innocent. Therefore, we can add this fact to the knowledge base as **rule 18**.

### 5.3 Bruno

Now, in order to fully verify Daniela’s statement, we attempt to prove the hypothesis that **Bruno is guilty**: `guilty(b)`.

| №    |     Derived Clause      | Resolution Step / Description           |
| ---- | :---------------------: | --------------------------------------- |
| 19   |      `¬guilty(b)`       | Negated conclusion                      |
| 20   | `guilty(e) v guilty(d)` | Resolution of clauses **12** and **19** |
| 21   |       `guilty(e)`       | Resolution of clauses **17** and **20** |
| 22   |      `¬guilty(a)`       | Resolution of clauses **5** and **21**  |
| 23   |      `¬guilty(c)`       | Resolution of clauses **10** and **21** |
| 24   |      `¬guilty(d)`       | Resolution of clauses **11** and **21** |

During the resolution process, **no empty clause was derived**. Instead, the following literals were obtained in the course of resolution:`¬guilty(b)`, `guilty(e)`, `¬guilty(a)`, `¬guilty(c)`, `¬guilty(d)`.

This means that we **cannot prove** that Bruno is guilty. Therefore, we proceed to test the alternative hypothesis — that **Bruno is innocent**.

| №    |           Derived Clause            | Resolution Step / Description           |
| :--- | :---------------------------------: | --------------------------------------- |
| 19   |             `guilty(b)`             | Negated conclusion                      |
| 20   |            `¬guilty(e)`             | Resolution of clauses **8** and **19**  |
| 21   |            `¬guilty(a)`             | Resolution of clauses **2** and **19**  |
| 22   |            `¬guilty(c)`             | Resolution of clauses **6** and **19**  |
| 23   | `guilty(a) v guilty(c) v guilty(d)` | Resolution of clauses **13** and **20** |
| 24   |       `guilty(c) v guilty(d)`       | Resolution of clauses **21** and **23** |
| 25   |             `guilty(d)`             | Resolution of clauses **22** and **24** |
| 26   |                 `□`                 | Resolution of clauses **17** and **25** |


As a result of the resolution with the negation of the hypothesis that Bruno is guilty, an **empty clause** was obtained, which proves his innocence. Consequently, we add the fact `¬guilty(b)` to the knowledge base as the, **numbered 19**.

### 5.4 Eduardo

We already have proofs that **Daniela** and **Bruno** are innocent. Therefore, Daniela’s statement has been fully analyzed, and we can proceed to the next statement — **Bruno’s**.

Bruno claims that the guilty person is either **Eduardo** or **Daniela**. However, since we already know that **Daniela is innocent**, we can test the hypothesis that **Eduardo is guilty**: `guilty(e)`.

| №    |     Derived Clause      | Resolution Step / Description           |
| ---- | :---------------------: | --------------------------------------- |
| 20   |      `¬guilty(e)`       | Negated conclusion                      |
| 21   | `guilty(b) v guilty(d)` | Resolution of clauses **12** and **20** |
| 22   |       `guilty(d)`       | Resolution of clauses **19** and **21** |
| 23   |           `□`           | Resolution of clauses **17** and **22** |

As a result of the resolution process, we obtained an **empty clause**, which means that the hypothesis of Eduardo’s guilt is true. Thus, we have identified the person who ate the cookie.

### 5.5 Ana

Since the guilty person — **Eduardo** — has been identified, there is no need to continue checking further hypotheses, in particular whether **Ana** is guilty or not. The statement that one of the girls ate the cookie is false, therefore **Ana is automatically considered innocent**, without requiring an additional resolution proof.


## 6. Automated Solver Verification

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

Having completed the entire process of solving in predicate logic using the resolution method with the set-of-support strategy, and verifying the results with SAT/SMT solvers, we concluded that the constant **e (Eduardo)** is the person who *ate the cookies*. All others — **a (Ana), b (Bruno), c (Cecilia), d (Daniela)** — *are innocent*.

![Result Cookie Puzzle Photo](C:\Users\admin\Downloads\result_cookie_puzzle.png)