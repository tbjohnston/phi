# Estimation of Phi 6 Jan 2013
from numpy import all

phi = 0.5 * (1. + 5.**.5)
print "Phi is approximately %s" % phi

# initialize variables
f0 = 1.
f1 = 1.
k = 0
limit = 24
esti= numpy.zeros(limit)
errorf = numpy.zeros(limit)
errorg = numpy.zeros(limit)


while k <= (limit-1):
    esti[k]= f1 / f0
    errorf[k] = abs(esti[k] - phi)
    errorg[k] = esti[k]-phi
    print "%i, %i, %i, %s, %s" % (k, f0, f1, esti[k], errorf[k])
    f2 = f0 + f1
    f0 = f1
    f1 = f2
    k += 1
    
plot(esti, 'bo', label = 'Estimate of Phi')
plot(esti, ':k')
ylim(.8, 2.1)
xlabel('Term in Fibonacci Sequence')
title('Estimate of Phi using Fibonnaci Sequence')
show()

