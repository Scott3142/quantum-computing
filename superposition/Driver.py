import qsharp

from Quantum.Superposition import Superposition

ones = 0
for x in range(0, 1000):
    result = Superposition.simulate()
    if result == qsharp.Result.One:
        ones += 1
    
print('Collapsed States: ')
print(f'\t  One: {ones}')
print(f'\t Zero: {1000-ones}')