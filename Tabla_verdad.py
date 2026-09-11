import itertools


print(" P | Q | ~P | P ^ Q | P v Q | P -> Q | P <-> Q")
print("-" * 47)

for P, Q in itertools.product([True, False], repeat=2):
    
    not_p = not P
    and_pq = P and Q
    or_pq = P or Q
    implies_pq = not P or Q       
    equiv_pq = P == Q              

    
    to_vf = lambda val: "V" if val else "F"

    print(
        f" {to_vf(P)} | {to_vf(Q)} |  {to_vf(not_p)} |   {to_vf(and_pq)}   |   {to_vf(or_pq)}   |   {to_vf(implies_pq)}    |    {to_vf(equiv_pq)}"
    )