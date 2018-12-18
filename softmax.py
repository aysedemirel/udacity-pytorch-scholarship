import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    exp_l = np.exp(L)
    sum_exp = sum(exp_l)
    result = []
    for i in exp_l:
        result.append(i*1.0/sum_exp) # e1/(e1+....+en)
    return result
