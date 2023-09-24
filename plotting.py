import matplotlib.pyplot as plt
import files


def save(file, format=None):
    files.prep_path(file)
    plt.savefig(file, format=format, bbox_inches='tight')
    plt.close()
