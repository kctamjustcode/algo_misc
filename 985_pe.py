import math, copy

def triangle_ineq(X,Y,Z):
    return X+Y>Z and X+Z>Y and Y+Z>X

def rev_cosine_rule(A,B,C):
    return math.acos((B**2+C**2-A**2)/(2*B*C))#/math.pi*180

def corr_spnd_angles(X,Y,Z):
    return rev_cosine_rule(X,Y,Z), rev_cosine_rule(Y,Z,X), rev_cosine_rule(Z,X,Y)

A1, B1, C1 = rev_cosine_rule(8,9,10), rev_cosine_rule(9,10,8), rev_cosine_rule(10,8,9)
print(A1+B1+C1==math.pi)

def sol(A,B,C):
    assert round(A+B+C, 12) == round(math.pi, 12)
    return (A+B-C)/2, (A+C-B)/2, (B+C-A)/2

def sol_valid(a, b, c, A, B, C):
    return round(a+b+c,12) == round(math.pi/2,12) and round(a+b,12) == round(A,12) and round(a+c,12) == round(B,12) and round(b+c,12) == round(C,12)

print(sol(A1,B1,C1))
a1, b1, c1 = sol(A1,B1,C1)
print(round(a1+b1+c1,12) == round(math.pi/2, 12))
#print(a1+b1==A1)
#print(a1,b1,a1+b1,A1)
#print(sol_valid(a1,b1,c1,A1,B1,C1))

def valid_para(X,Y,Z):
    A_sol, B_sol, C_sol = rev_cosine_rule(X,Y,Z), rev_cosine_rule(Y,Z,X), rev_cosine_rule(Z,X,Y)
    a_sol, b_sol, c_sol = sol(A_sol, B_sol, C_sol)
    return sol_valid(a_sol,b_sol,c_sol,A_sol,B_sol,C_sol)

print(valid_para(8,9,10))
a2,b2,c2 = sol(2*a1,2*b1,2*c1)
print(sol_valid(a2,b2,c2,2*a1,2*b1,2*c1))
a3,b3,c3 = sol(2*a2,2*b2,2*c2)
print(sol_valid(a3,b3,c3,2*a2,2*b2,2*c3))

