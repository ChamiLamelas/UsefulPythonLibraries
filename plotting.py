import matplotlib.pyplot as plt
import files


def save(file, format=None):
    files.prep_path(file)
    plt.savefig(file, format=format, bbox_inches='tight')
    plt.close()


def make_plot_nice(ax, xlabel, ylabel, ymin, ymax, fontsize=16, legendcol=1):
    if legendcol is not None:
        ax.legend(fontsize=fontsize, ncol=legendcol, frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params('y', labelsize=fontsize)
    ax.tick_params('x', labelsize=fontsize)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_ylim([ymin, ymax])
    ax.grid()
