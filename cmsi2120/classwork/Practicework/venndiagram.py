import matplotlib.pyplot as plt
from matplotlib_venn import venn2

venn2(
  subsets = (8,10,5),
  set_labels = ('Are Healthy', 'Do Exrecise')
)

plt.show()