print [((m*m-n*n)*(2*m*n)*(m*m+n*n)) for m in range (1000) for n in range(1000) if m>n and m*(m+n)==500]
