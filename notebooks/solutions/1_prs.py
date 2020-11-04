es = []
fs = []
min_f = np.Inf
for i in range(1000):
    x = np.random.rand()*4-2
    y = np.random.rand()*4-2
    f = rosenbrock(x, y)
    if f < min_f:
        min_f = f
        es += [i]
        fs += [f]
fig = plt.figure(figsize=(8, 6))
plt.yscale('log')
plt.plot(es, fs);
