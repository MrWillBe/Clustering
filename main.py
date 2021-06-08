import numpy as np

from barycenter_list import Barycenter_List
from Operator import Operator

# barycenter_list = barycenter.random_barycenter(3)
# print(barycenter_list)

# p_barycenter_number == 2 is used to generate two barycenter (x, y)
# p_line == 2 is used to generate 2 times (twice) "x" for 2 barycenter
# barycenter_abs = barycenter.get_abs_barycenter_list(2, 2)
# print(barycenter_abs)

# p_barycenter_number == 2 is used to generate two barycenter (x, y)
# p_line == 2 is used to generate 2 times (twice) "x" for 2 barycenter
# barycenter_ord = barycenter.get_ord_barycenter(2, 2)
# print(barycenter_ord)

barycenter_group = Barycenter_List(2)
#print(barycenter_group.barycenter_list[1].abs)
#data = np.array(barycenter_group.abs_list, barycenter_group.ord_list)
#print(data)
normes = Operator.norme(barycenter_group)
print(normes)
Operator.sortNorms(normes)
print(normes)