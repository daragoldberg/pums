import math

def get_se(per_wt,rep_weights):
    for i in rep_weights:
        result += (i - per_wt)**2
    return math.sqrt((4/80)*result)

def get_moe(m):
    result = math.sqrt(sum(map(lambda x: x**2, m)))
    return result

def get_se_2(per_wt,rep_weights):
    result = math.sqrt((sum(map(lambda x: (x-per_wt)**2,rep_weights))/20)
    return result