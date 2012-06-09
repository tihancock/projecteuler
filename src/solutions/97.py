"""
Calculate the last 10 digits of the prime 28433*2^7830457+1. This calculation
makes use of the fact that the last n digits of 2^x repeat every 4*5^n-1
iterations.
"""

print str(28433*2**(7830457%(4*5**9))+1)[-10::]
