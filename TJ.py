#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:51:09 2023

@author: tj
"""

import numpy as np

# define the matrix A
A = np.array([[1, 2, 0], [1, 1, 2], [0, 1, 1]])

# find the determinant of A
det_A = np.linalg.det(A)

# find the matrix of cofactors of A
C = np.array([[1, 0, -1], [2, 1, 0], [0, -2, 1]])

# find the adjugate of A
adj_A = np.transpose(C)

# find the inverse of A
A_inv = (1/det_A) * adj_A

# print the inverse of A
print(A_inv)