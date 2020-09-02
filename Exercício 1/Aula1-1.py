import statistics
x = [1,5,6,6,7,8,8,8]
print(statistics.mean(x))
print(statistics.variance(x))
print(statistics.stdev(x))
Med=1.143
Des_pad= 0.063
CV = (Des_pad/Med)*100
print(CV)
print(statistics.mode(x))