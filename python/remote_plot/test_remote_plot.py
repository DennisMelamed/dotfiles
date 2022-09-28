import remote_plot as rplt
import matplotlib.pyplot as plt

plt.plot([0, 1, 2])
rplt.show(remote=False)

plt.plot([0, 1, 2])
rplt.show(remote=True)
