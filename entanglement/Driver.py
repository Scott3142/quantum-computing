import qsharp

from Quantum.Entanglement import Entanglement

ones = 0
equal = 0
for x in range(0, 1000):
    result = Entanglement.simulate()
    if result[0] == qsharp.Result.Zero:
        ones += 1
    if result[0] == result[1]:
        equal += 1

print('Entanglement Results:')
print(f'\t   One: {ones}')
print(f'\t  Zero: {1000-ones}')
print(f'\t Equal: {(equal/1000)*100}%')