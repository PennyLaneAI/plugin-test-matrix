from textwrap import dedent

from jinja2 import FileSystemLoader, Environment


workflows = [
    {
        "plugin": "qiskit",
        "gh_user": "PennyLaneAI",
        "which": ["latest", "stable"],
        "requirements": ["qiskit", "pyscf==1.7.2"],
        "device_tests": [
            "--device=qiskit.basicaer --tb=short --skip-ops --shots=20000 --device-kwargs backend=qasm_simulator",
            "--device=qiskit.aer --tb=short --skip-ops --shots=20000",
            "--device=qiskit.basicaer --tb=short --skip-ops --shots=None --device-kwargs backend=statevector_simulator",
            "--device=qiskit.aer --tb=short --skip-ops --shots=None --device-kwargs backend=aer_simulator_unitary",
        ],
        "test_kwargs": ["-k 'not test_ibmq.py and not test_runtime.py'"],
        "token": "IBMQX_TOKEN",
    },
    {
        "plugin": "cirq",
        "gh_user": "PennyLaneAI",
        "which": ["latest", "stable"],
        "requirements": ["cirq", "qsimcirq"],
        "device_tests": [
            "--device=cirq.simulator --tb=short --skip-ops --shots=None",
            "--device=cirq.simulator --tb=short --skip-ops --shots=20000",
            "--device=cirq.mixedsimulator --tb=short --skip-ops --shots=None",
            "--device=cirq.mixedsimulator --tb=short --skip-ops --shots=20000",
            # Pasqal doesn't work, says
            #      qubits = [pasqal.ThreeDQubit(wire * control_radius / 2, 0, 0) for wire in range(wires)]
            #      E   TypeError: unsupported operand type(s) for /: 'str' and 'int'
            # "--device=cirq.pasqal --tb=short --skip-ops --analytic=False --shots=20000 --device-kwargs control_radius=2.",
            "--device=cirq.qsim --tb=short --skip-ops --analytic=False --shots=20000",
        ],
    },
    {
        "plugin": "qulacs",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": ["qulacs"],
        "device_tests": [
            "--device=qulacs.simulator --tb=short --skip-ops --shots=None",
            "--device=qulacs.simulator --tb=short --skip-ops --shots=20000",
        ],
    },
    {
        "plugin": "rigetti",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": ["pyquil==2.28.2"],
        "device_tests": [
            "--device=rigetti.numpy_wavefunction --tb=short --skip-ops --shots=None",
            "--device=rigetti.wavefunction --tb=short --skip-ops --shots=20000",
            # "--device=rigetti.qvm --tb=short --skip-ops --shots=20000 --device-kwargs device=4q-qvm",
        ],
        "additional_setup": dedent("""
            - name: Run Rigetti Quilc
              run: docker run --rm -d -p 5555:5555 rigetti/quilc:1.23.0 -R

            - name: Run Rigetti QVM
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
        "plugin": "ionq",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": [],
        "device_tests": ["--device=ionq.simulator --tb=short --skip-ops --shots=10000"],
        "token": "IONQ_API_KEY",
    },
    {
        "plugin": "pq",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": ["projectq"],
        "device_tests": [],
        "token": "IBMQX_TOKEN",
    },
    {
        "plugin": "lightning",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": ["pybind11"],
        "device_tests": [
            "--device lightning.qubit --shots=None --skip-ops",
            "--device lightning.qubit --skip-ops --shots=20000",
            ],
        "additional_setup": dedent("""
            - name: Install buildtools & compilers
              run: |
                sudo apt-get update && sudo apt-get -y -q install cmake gcc-${{ env.GCC_VERSION }} g++-${{ env.GCC_VERSION }} ninja-build"""
        ),
        "additional_env_vars": "GCC_VERSION: 11",
        "runs_on": "ubuntu-22.04",
    },
    {
        "plugin": "orquestra",
        "gh_user": "PennyLaneAI",
        "which": ["stable", "latest"],
        "requirements": [],
        "device_tests": [],
        "test_kwargs": ["-k 'not e2e'"],
        "branch": "main",
    },
    {
        "plugin": "braket",
        "plugin_repo": "amazon-braket-pennylane-plugin-python",
        "plugin_package": "amazon-braket-pennylane-plugin",
        "gh_user": "aws",
        "which": ["stable", "latest"],
        "requirements": [],
        "device_tests": [],
        "branch": "main",
        "device_tests": [
            "--device=braket.local.qubit --tb=short --skip-ops --shots=20000 -k 'not no_0_shots'",
            "--device=braket.local.qubit --tb=short --skip-ops -k 'not Sample and not no_0_shots'",
        ],
        "tests_loc": "test/unit_tests",
        "additional_setup": dedent("""
            - name: Install TF
              run: |
                pip install tensorflow~=$TF_VERSION keras~=$TF_VERSION"""
        ),
        "additional_env_vars": "TF_VERSION: 2.12.0\n  TORCH_VERSION: 2.0.0+cpu",
    },
    {
        "plugin": "quantuminspire",
        "gh_user": "QuTech-Delft",
        "which": ["stable", "latest"],
        "requirements": ["pennylane-qiskit", "quantuminspire", "qiskit"],
        "branch": "master",
        "device_tests": [
            "--device=quantuminspire.qi --tb=short --skip-ops --shots=4096 --device-kwargs backend='QX single-node simulator'",
        ],
        "tests_loc": "tests/unit_test",
        "token": "QI_TOKEN",
    },
]


def render_from_template(template, **kwargs):
    loader = FileSystemLoader(".")
    env = Environment(loader=loader)
    template = env.get_template(template)
    return template.render(**kwargs)


def render_templates():

    for wf in workflows:

        if "plugin_package" not in wf:
            plugin_name = wf["plugin"]
            wf["plugin_package"] = "pennylane_" + plugin_name

        if "plugin_repo" not in wf:
            plugin_name = wf["plugin"]
            wf["plugin_repo"] = "pennylane-" + plugin_name

        if "tests_loc" not in wf:
            wf["tests_loc"] = "tests"

        # PennyLane stable tests
        for i in wf["which"]:
            with open(f".github/workflows/{wf['plugin']}-{i}-stable.yml", "w") as f:
                f.write(render_from_template("workflow-template-stable.yml", latest=i ==  "latest", **wf))

        # PennyLane latest tests
        for i in wf["which"]:
            with open(f".github/workflows/{wf['plugin']}-{i}-latest.yml", "w") as f:
                f.write(
                    render_from_template("workflow-template-latest.yml", latest=i == "latest", **wf)
                )

        # PennyLane release candidate tests
        for i in wf["which"]:
            with open(f".github/workflows/{wf['plugin']}-latest-rc.yml", "w") as f:
                f.write(
                    render_from_template("workflow-template-release-candidate.yml", latest=True, **wf)
                )


if __name__ == "__main__":
    render_templates()
