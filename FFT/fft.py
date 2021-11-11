import math

def a(n):
    m = math.log(n) / math.log(2)
    n2 = n

    # DOFOR k = 1, m
    k = 1
    while k <= m:
        n1 = n2
        n2 = n2/2
        angle = 0
        arg = (2 * math.pi) / n1

        # DOFOR j=0, N2 - 1
        j = 0
        while j < n2 - 1:
            c = math.cos(angle)
            s = -(math.sin(angle))

            # DOFOR i=j, N-1, N1
            i = j
            while i < n-1: 
                # TODO: implement the weird part with kk xt yt y(i) x(i) inside this loop
                i += n1
                angle = (j + 1) * arg
            j += 1

        k += 1

def b(n):
    j = 0

    # DOFOR i = 0, N - 2
    i = 0
    while i < n - 2:
        if i < j:
            xt = xj
            xj = xi
            xi = xt
            yt = yj
            yj = yi 
            yi = yt
        k = n/2
        while k < j+1:
            j = j - k
            k = k/2
        j = j + k
        i += 1
    
    # DOFOR i = 0, N - 1
    i = 0
    while i < n - 1:
        x(i) = x(i)/n 
        y(i) = y(i)/n
        
#define the lambda function for x() and y()
x = lambda n : n+n
y = lambda n : n+n