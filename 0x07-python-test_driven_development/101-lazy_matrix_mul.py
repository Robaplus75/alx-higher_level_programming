#!/usr/bin/python3
"""defines a fucntion for matrix multiplication"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrixes

    Args:
        m_a (list of lists of ints/floats): matrix one
        m_b (list of lists of ints/floats): matrix two
    """

    return (numpy.matmul(m_a, m_b))
