#!/usr/env python3
################################################################################
# eulers_formula.py

# this module contains mathematics with complex numbers, for most cases
# just import math - but we need cmath here
import cmath

# the famous result of eulers formula with x = -1
# the formula uses a special type of number system called complex numbers,
# to use complex numbers we use functions from cmath
magic_number = cmath.exp(cmath.sqrt(-1) * cmath.pi)

# print out the result and notice how there are slight errors in the computation
print("A fancy maths equation euler discovered was e^i(pi) = "
      + str(magic_number))

# let's explain the little oddity in the results
print("Okay, this looks less fancy now, but the number is actually -1,"
      + "computers just don't have enough accuracy to deal with trancendental"
      + " numbers")
