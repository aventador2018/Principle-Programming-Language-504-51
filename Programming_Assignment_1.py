# Let G be the grammar with vocabulary V = {S, A, a, b}, set of terminals T = {a, b}, starting symbol S, and
# productions P = {S -> aA, S -> b, A -> aa}. What is L(G), the language of this grammar?

S = ['aA', 'b']
A = ['aa']

result_set = []
result = ''
for i in range(0, len(S)):
    result = S[i]
    for j in range (0, 20):
        result = result.replace('S', S[0])
        result = result.replace('A', A[0])
        if result.find('S') == -1 and result.find('A') == -1:
            result_set.append(result)
            break
print(result_set)