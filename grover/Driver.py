import qsharp
from GroversAlgorithm import SearchForMarkedInput

n_qubits = 5
result = SearchForMarkedInput.simulate(nQubits=n_qubits)
print(result)