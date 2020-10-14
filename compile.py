from textwrap import dedent

from jinja2 import FileSystemLoader, Environment


workflows = [
    {
        "plugin": "qiskit",
        "gh_user": "PennyLaneAI",
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
        "gh_user": "PennyLaneAI",
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
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": ["qulacs"],
        "device_tests": [
            "--device=qulacs.simulator --tb=short --skip-ops --analytic=True",
            "--device=qulacs.simulator --tb=short --skip-ops --analytic=False --shots=20000",
        ],
    },
    {
        "plugin": "sf",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": ["strawberryfields"],
        "device_tests": [],
    },
    {
        "plugin": "forest",
        "gh_user": "rigetti",
        "which": ["stable", "latest"],
        "requirements": ["pyquil"],
        "device_tests": [
            "--device=forest.numpy_wavefunction --tb=short --skip-ops --analytic=True",
            "--device=forest.wavefunction --tb=short --skip-ops --analytic=False --shots=20000",
            # "--device=forest.qvm --tb=short --skip-ops --shots=20000 --device-kwargs device=4q-qvm",
        ],
        "additional_setup": dedent("""
            - name: Run Forest Quilc
              run: docker run --rm -d -p 5555:5555 rigetti/quilc -R

            - name: Run Forest QVM
              run: docker run --rm -d -p 5000:5000 rigetti/qvm -S"""
        )
    },
    {
        "plugin": "aqt",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": [],
        "device_tests": [],
    },
    {
        "plugin": "honeywell",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": [],
        "device_tests": [],
    },
    {
        "plugin": "pq",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": ["projectq"],
        "device_tests": [],
    },
    {
        "plugin": "lightning",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": ["pybind11"],
        "device_tests": [
            "--device lightning.qubit --analytic True --skip-ops",
            "--device lightning.qubit --analytic False --skip-ops --shots=20000",
            ],
        "additional_setup": dedent("""
            - name: Install Eigen
              run: |
                sudo apt install libeigen3-dev"""
        )
    },
]


def render_from_template(template, **kwargs):
    loader = FileSystemLoader(".")
    env = Environment(loader=loader)
    template = env.get_template(template)
    return template.render(**kwargs)


def render_templates():

    for wf in workflows:
        # PennyLane stable tests
        # if "stable" in wf["which"]:
        for i in wf["which"]:
            with open(f".github/workflows/{wf['plugin']}-{i}-stable.yml", "w") as f:
                f.write(render_from_template("workflow-template-stable.yml", latest=i ==  "latest", **wf))

        # PennyLane latest tests
        for i in wf["which"]:
            with open(f".github/workflows/{wf['plugin']}-{i}-latest.yml", "w") as f:
                f.write(
                    render_from_template("workflow-template-latest.yml", latest=i == "latest", **wf)
                )


if __name__ == "__main__":
    render_templates()
