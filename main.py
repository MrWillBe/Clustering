import barycenter

barycenter_list = barycenter.random_barycenter(3)
print(barycenter_list)

# p_barycenter_number == 2 is used to generate two barycenter (x, y)
# p_line == 2 is used to generate 2 times (twice) "x" for 2 barycenter
barycenter_abs = barycenter.get_abs_barycenter(2, 2)
print(barycenter_abs)

# p_barycenter_number == 2 is used to generate two barycenter (x, y)
# p_line == 2 is used to generate 2 times (twice) "x" for 2 barycenter
barycenter_ord = barycenter.get_ord_barycenter(2, 2)
print(barycenter_ord)