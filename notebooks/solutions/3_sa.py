def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

max_e = 1000
n_runs = 5

# Random Search
fs = np.zeros((n_runs, max_e))
for j in range(n_runs):
    min_f = np.inf
    for i in range(max_e):
        x = np.random.rand()*4-2
        y = np.random.rand()*4-2
        f = himmelblau(x, y)
        if f < min_f:
            min_f = f
        fs[j, i] = min_f
fs_mean = np.mean(fs, 0)
fs_std = np.std(fs, 0)

# Simulated Annealing
sa_fs = np.zeros((n_runs, max_e))
for j in range(n_runs):
    x = np.random.randn(2)
    fx = himmelblau(x[0], x[1])
    fbest = fx
    xbest = np.copy(x)
    for i in range(max_e):
      xp = x + np.random.randn(2)
      T = (max_e - i) / max_e
      fxp = himmelblau(xp[0], xp[1])
      if (fxp < fx) or (np.exp(-(fxp-fx)/T) > np.random.rand()):
        x = np.copy(xp)
        if fxp < fbest:
          fbest = fxp
          xbest = np.copy(xp)
      sa_fs[j, i] = fbest
sa_fs_mean = np.mean(sa_fs, 0)
sa_fs_std = np.std(sa_fs, 0)

# Plotting
ax_x = range(max_e)
fig = plt.figure(figsize=(8, 6))
plt.fill_between(ax_x, fs_mean+0.5*fs_std, fs_mean-0.5*fs_std, alpha=0.5);
plt.plot(ax_x, fs_mean, label='PRS')
plt.fill_between(ax_x, sa_fs_mean+0.5*sa_fs_std, sa_fs_mean-0.5*sa_fs_std, alpha=0.5, color='r');
plt.plot(ax_x, sa_fs_mean, color='r', label='SA')
plt.yscale('log')
plt.legend()
plt.show();

