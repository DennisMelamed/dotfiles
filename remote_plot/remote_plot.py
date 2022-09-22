import matplotlib.pyplot as plt
import mpld3


def show(remote=False):
    if remote:
        mpld3.show()
    else:
        plt.show()
