def mu_lambda(evals=10000, lam=10, alpha=0.1):
    x = np.random.rand(2)*10-5
    x_best = x
    f_best = himmelblau(x[0], x[1])
    fits = np.zeros(evals)
    e = 0
    gens = int(np.floor(evals/lam))
    for g in range(gens):
        N = np.random.normal(size=(lam, 2))
        F = np.zeros(lam)
        for i in range(lam):
            ind = x + N[i, :]
            F[i] = himmelblau(ind[0], ind[1])
            if F[i] < f_best:
                f_best = F[i]
                x_best = ind
            fits[e] = f_best
            e += 1
        mu_f = np.mean(F)
        std_f = np.std(F)
        A = F
        if std_f > 0:
            A = (F - mu_f) / std_f
        x = x - alpha * np.dot(A, N) / lam
    return fits

max_e = 1000
n_runs = 5

ax_x = range(max_e)
fig = plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b', 'k']
alphas = [1.0, 0.5, 0.1, 0.01]
for ai in range(len(alphas)):
    alpha = alphas[ai]
    runs = []
    for i in range(n_runs):
        runs += [mu_lambda(evals=max_e, alpha=alpha)]
    runs = np.array(runs)
    runs_mean = np.mean(runs, 0)
    runs_std = np.std(runs, 0)
    plt.fill_between(ax_x, runs_mean+0.5*runs_std, runs_mean-0.5*runs_std, alpha=0.5, color=colors[ai])
    plt.plot(ax_x, runs_mean, label=str(alpha), c=colors[ai])

plt.yscale('log')
plt.legend()
plt.show();
