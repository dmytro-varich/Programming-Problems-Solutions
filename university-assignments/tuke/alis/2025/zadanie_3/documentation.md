# Cookie Puzzle

![Cookie Puzzle Photo](university-assignments/tuke/alis/2025/zadanie_3/media/cookie_puzzle_photo.jpg)

Aunt Geralda knows that one of Ana, Bruno, Cecilia, Daniela or Eduardo ate all
the cookies. She also knows that the guilty always lie and the innocent always
tell the truth.


- Bruno says, "The culprit is either Eduardo or Daniela".
- Eduardo says: "The guilty person is a girl."
- Finally, Daniela says, "if Bruno is guilty, then Cecilia is innocent."

Who ate the cookies? Who is innocent?

---

# Predicate Logic Solution

## Contents

1. **Vocabulary**
2. **Knowledge Base Formalization**
3. **CNF Transformation**
4. **Knowledge Base Clauses**
5. **Resolution with Set-of-Support Strategy**
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
     & \land (\lnot guilty(a) \lor \lnot guilty(b))
     \land (\lnot guilty(a) \lor \lnot guilty(c))
     \land (\lnot guilty(a) \lor \lnot guilty(d))
     \land (\lnot guilty(a) \lor \lnot guilty(e)) \\
     & \land (\lnot guilty(b) \lor \lnot guilty(c))
     \land (\lnot guilty(b) \lor \lnot guilty(d))
     \land (\lnot guilty(b) \lor \lnot guilty(e)) \\
     & \land (\lnot guilty(c) \lor \lnot guilty(d))
     \land (\lnot guilty(c) \lor \lnot guilty(e)) \\
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
...

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

![Result Cookie Puzzle Photo](dmytro-varich/Programming-Problems-Solutions/university-assignments/tuke/alis/2025/zadanie_3/media/result_cookie_puzzle.png)