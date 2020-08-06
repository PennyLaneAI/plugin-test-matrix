from jinja2 import FileSystemLoader, Environment


workflows = [
    {
        "plugin": "qiskit",
        "which": ["latest", "stable"],
        "requirements": ["qiskit", "pyscf==1.7.2"],
        "device_tests": [
            "--device=qiskit.basicaer --tb=short --skip-ops --analytic=False --shots=20000 --device-kwargs backend=qasm_simulator",
            "--device=qiskit.aer --tb=short --skip-ops --analytic=False --shots=20000 --device-kwargs backend=qasm_simulator",
            "--device=qiskit.basicaer --tb=short --skip-ops --analytic=True --device-kwargs backend=statevector_simulator",
            "--device=qiskit.aer --tb=short --skip-ops --analytic=True --device-kwargs backend=unitary_simulator",
        ],
    },
    {
        "plugin": "cirq",
        "which": ["latest", "stable"],
        "requirements": ["cirq"],
        "device_tests": [
            "--device=cirq.simulator --tb=short --skip-ops --analytic=True",
            "--device=cirq.simulator --tb=short --skip-ops --analytic=False --shots=20000",
            "--device=cirq.mixedsimulator --tb=short --skip-ops --analytic=True",
            "--device=cirq.mixedsimulator --tb=short --skip-ops --analytic=False --shots=20000",
        ],
    },
    {
        "plugin": "qulacs",
        "which": ["latest"],
        "requirements": ["qulacs"],
        "device_tests": [
            "--device=qulacs.simulator --tb=short --skip-ops --analytic=True",
            "--device=qulacs.simulator --tb=short --skip-ops --analytic=False --shots=20000",
        ],
    },
    {
        "plugin": "sf",
        "which": ["stable", "latest"],
        "requirements": ["git+https://github.com/XanaduAI/strawberryfields.git"],
        "device_tests": [],
    },
    {"plugin": "aqt", "which": ["stable", "latest"], "requirements": [], "device_tests": []},
    {"plugin": "honeywell", "which": ["stable", "latest"], "requirements": [], "device_tests": []},
]


def render_from_template(**kwargs):
    loader = FileSystemLoader(".")
    env = Environment(loader=loader)
    template = env.get_template("workflow-template.yml")
    return template.render(**kwargs)


def render_templates():

    for wf in workflows:
        for i in wf["which"]:
            with open(f".github/workflows/{wf['plugin']}-{i}.yml", "w") as f:
                f.write(render_from_template(latest=i == "latest", **wf))


if __name__ == "__main__":
    render_templates()
