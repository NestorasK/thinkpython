import math
def estimate_pi():
    k = 0
    est_pi = 0
    sum_part = 0
    while True:
        changing_term_a = (math.factorial(4*k) * (1103 + 26390 * k))
        changing_term_b = ((math.factorial(k)**4) * 396**(4*k))
        term_i = changing_term_a / changing_term_b
        sum_part = sum_part + term_i
        if term_i < 1e-15:
            break
        k = k + 1
    stable_part = (2 * math.sqrt(2)) / 9801
    pi_est = 1 / (stable_part * sum_part)
    return pi_est


print('\npi:', math.pi, '\npi estimate:', estimate_pi(), '\n')





