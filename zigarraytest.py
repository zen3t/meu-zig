from array import array
import ctypes

a = array("i",range(100))
i = 5
print(a)

def sep_arr_py(l,no):
    is_le = []
    is_gt = []
    for i in l:
        if i <= no:
            is_le.append(i)
        else:
            is_gt.append(i)
    return is_le,is_gt
is_lepy,is_gtpy = sep_arr_py(a,i)
print(is_lepy,is_gtpy)
l,l_len = a.buffer_info()
n_array = array('i', [i])
n,_ = n_array.buffer_info()
is_le_array = array("i",[0] * l_len)
is_le_array = array("i",[0] * l_len)
resultcounter_is_le_array = array("Q",[0])
resultcounter_is_gt_array = array("Q",[0])

