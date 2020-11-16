#!/usr/bin/python3
# coding: utf-8


def suite(n):
  if (n == 0):
    return 8
  return 6 * suite(n-1) + 2 # Calcul de U0 jusqu’à Un.


n = int(input(“Calcul de Un avec Un+1 = 6*Un + 2 et U0 = 8 avec n = ”))
print (“U”+str(n)+” = “+str(suite(n)))


------------------------------------------------------------------------ Résultat -----------------------------------------------------------------------------