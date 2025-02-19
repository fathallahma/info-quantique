import os
from dotenv import load_dotenv
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService

load_dotenv()
api_token = os.getenv("IBMQ_API_TOKEN")

quantum_service = QiskitRuntimeService(channel="ibm_quantum", token=api_token)

backends = quantum_service.backends()
print("Voici les backends disponibles : ", backends)

selected_backend = backends[0].name
print(f"Backend sélectionné : {selected_backend}")

circuit = QuantumCircuit(1, 1)
circuit.h(0)
circuit.measure(0, 0)

execution_job = quantum_service._run(
    program_id="sampler",
    options={"backend": selected_backend},
    inputs={"circuits": [circuit], "shots": 1}
)

print("ID du job exécuté : ", execution_job.job_id())
