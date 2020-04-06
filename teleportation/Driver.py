import qsharp
import random

from Quantum.Teleportation import Teleportation

trues = 0
equal = 0
for x in range(0, 1000):
    sent_message = random.choice([True,False])
    received_message = Teleportation.simulate(sentMessage=sent_message)

    if received_message:
        trues += 1
    if sent_message == received_message:
        equal += 1

print('Teleportation Results:')
print(f'\t   True: {trues}')
print(f'\t  False: {1000-trues}')
print(f'\t Equal: {(equal/1000)*100}%')