# ShorAlgo_Learn

Shor’s Algorithm is a quantum algorithm designed to factor large integers efficiently. Factoring is a hard problem for classical computers, especially as numbers grow large, and it forms the backbone of widely used cryptographic systems like RSA.

This project demonstrates the implementation and understanding of Shor’s Algorithm using modern quantum computing frameworks (such as Qiskit). It is intended for educational and experimental purposes, focusing on both the theoretical foundations and practical execution.

---

Classical factorization algorithms scale poorly with large inputs. In contrast, Shor’s Algorithm runs in polynomial time, making it exponentially faster for large integers.

If scalable quantum computers become practical, Shor’s Algorithm could break widely used encryption systems, fundamentally changing cybersecurity.

---


## Problem Statement

Given a composite number `N`, the goal is to find its non-trivial factors.

Example:

N = 15
Factors = 3 × 5

---

## Core Idea

Shor’s Algorithm reduces the problem of factoring into a problem of finding the **order** of a number.

For a randomly chosen integer `a` such that:

gcd(a, N) = 1

we define the order `r` as the smallest integer satisfying:

a^r ≡ 1 (mod N)

Finding this period `r` is the key step, and this is where quantum computation provides a speed advantage.

---

## Algorithm Steps

### 1. Choose a Random Integer

Pick a number `a` such that:

1 < a < N
gcd(a, N) = 1

If gcd(a, N) ≠ 1, a non-trivial factor is already found.

---

### 2. Reduce to Order Finding

We now aim to find the order `r` such that:

a^r mod N = 1

---

### 3. Quantum Phase Estimation (QPE)

This is the quantum core of the algorithm.

* A quantum circuit is constructed to estimate the phase of a unitary operator.
* The unitary operator encodes modular exponentiation.
* The output encodes the periodicity of the function.

---

### 4. Quantum Fourier Transform (QFT)

The QFT is applied to extract frequency (period) information from the quantum state.

It transforms the superposition into a form where measurement reveals the period `r`.

---

### 5. Measurement

The quantum state is measured, producing a value that approximates:

k / r

This value is processed using classical methods to estimate `r`.

---

### 6. Classical Post-Processing

Using continued fractions, we approximate the measured value to recover `r`.

Once `r` is found:

* If `r` is odd, retry
* If a^(r/2) ≡ -1 (mod N), retry

Otherwise, compute:

gcd(a^(r/2) - 1, N)
gcd(a^(r/2) + 1, N)

These yield non-trivial factors of `N`.

---

## Example (N = 15)

1. Choose a = 2
2. Compute order r:

2^4 ≡ 1 (mod 15) → r = 4

3. Compute:

gcd(2^2 - 1, 15) = gcd(3, 15) = 3
gcd(2^2 + 1, 15) = gcd(5, 15) = 5

Factors found: 3 and 5

---

## Quantum Circuit Components

A typical implementation includes:

* Input register (superposition of states)
* Work register (modular exponentiation)
* Controlled unitary operations
* Inverse Quantum Fourier Transform
* Measurement operations

---

## Implementation Notes

* Most practical implementations simulate the algorithm due to hardware limitations.
* Noise and decoherence significantly affect real quantum devices.
* The algorithm is typically demonstrated on small numbers like 15 or 21.

---


## Limitations

* Current quantum hardware is not capable of factoring large numbers used in real-world encryption.
* Requires a large number of qubits and error correction for scalability.
* Probabilistic output means multiple runs are often required.

---

## Applications

* Cryptanalysis (breaking RSA)
* Number theory research
* Benchmarking quantum computers

---

## Prerequisites

To understand this project, familiarity with the following is helpful:

* Basic number theory (modular arithmetic, gcd)
* Linear algebra (vectors, transformations)
* Quantum computing basics (qubits, gates, superposition)
* Python and Qiskit (for implementation)

---

## Conclusion

Shor’s Algorithm represents a major breakthrough in computational theory, showing that quantum systems can solve certain problems far more efficiently than classical computers.

While practical large-scale factorization is still out of reach, the algorithm remains one of the strongest motivations for building scalable quantum hardware.
