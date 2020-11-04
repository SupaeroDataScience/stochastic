max_e = 1000
n_runs = 5
fs = np.zeros((n_runs, max_e))
for j in range(n_runs):
    min_f = np.Inf
    for i in range(max_e):
        x = np.random.rand()*4-2
        y = np.random.rand()*4-2
        f = rosenbrock(x, y)
        if f < min_f:
            min_f = f
        fs[j, i] = min_f
fs_mean = np.mean(fs, 0)
fs_std = np.std(fs, 0)

ro_fs = np.zeros((n_runs, max_e))
for j in range(n_runs):
    min_f = np.Inf
    x = np.random.rand()*4-2
    y = np.random.rand()*4-2
    for i in range(max_e):
        temp_x = x + np.random.randn()
        temp_y = y + np.random.randn()
        f = rosenbrock(temp_x, temp_y)
        if f < min_f:
            min_f = f
            x = temp_x
            y = temp_y
        ro_fs[j, i] = min_f
ro_fs_mean = np.mean(ro_fs, 0)
ro_fs_std = np.std(ro_fs, 0)

ax_x = range(max_e)
fig = plt.figure(figsize=(8, 6))
plt.fill_between(ax_x, fs_mean+0.5*fs_std, fs_mean-0.5*fs_std, alpha=0.5);
plt.plot(ax_x, fs_mean, label='PRS')
plt.fill_between(ax_x, ro_fs_mean+0.5*ro_fs_std, ro_fs_mean-0.5*ro_fs_std, alpha=0.5, color='r');
plt.plot(ax_x, ro_fs_mean, color='r', label='RO')
plt.yscale('log')
plt.legend()
plt.show();
