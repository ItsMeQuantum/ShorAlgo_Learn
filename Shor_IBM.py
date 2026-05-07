from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np


def qft_dagger(n):
    """
    Inverse Quantum Fourier Transform
    """
    qc = QuantumCircuit(n)

    
    for qubit in range(n // 2):
        qc.swap(qubit, n - qubit - 1)

    
    for j in range(n):
        for m in range(j):
            qc.cp(-np.pi / float(2 ** (j - m)), m, j)

        qc.h(j)

    return qc