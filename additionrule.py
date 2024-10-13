even = {2,4,6}
greater_than_2 = {3,4,5,6}
allpossible={1,2,3,4,5,6}

def probablity_a_b(a,b,s):
    prob_a = len(a)/len(s)
    prob_b = len(b)/len(s)
    inter = a.intersection(b)
    probinter = len(inter)/len(s)
    return(prob_a + prob_b - probinter)

print("probablity of getting an even number or getting a number which is greater than two after rolling a dice is   ", probablity_a_b(even,greater_than_2,allpossible))