from textwrap import dedent

from jinja2 import FileSystemLoader, Environment


workflows = [
    {
        "plugin": "qiskit",
        "gh_user": "PennyLaneAI",
        "which": ["latest", "stable"],
        "requirements": ["qiskit", "pyscf"],
        "device_tests": [
            "--device=qiskit.basicsim --tb=short --skip-ops --shots=20000 --device-kwargs backend=basic_simulator",
            "--device=qiskit.aer --tb=short --skip-ops --shots=20000",
            "--device=qiskit.aer --tb=short --skip-ops --shots=None --device-kwargs backend=statevector_simulator",
            "--device=qiskit.aer --tb=short --skip-ops --shots=None --device-kwargs backend=unitary_simulator",
        ],
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
            "--device=cirq.pasqal --tb=short --skip-ops --analytic=False --shots=20000 --device-kwargs control_radius=2.",
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
        "plugin": "aqt",
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
        "plugin": "braket",
        "plugin_repo": "amazon-braket-pennylane-plugin-python",
        "plugin_package": "amazon-braket-pennylane-plugin",
        "gh_user": "aws",
        "which": ["stable", "latest"],
        "requirements": ["pytest-xdist"],
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
        "no_deprecation_error": True,
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
        with open(f".github/workflows/{wf['plugin']}-latest-rc.yml", "w") as f:
            f.write(
                render_from_template("workflow-template-release-candidate.yml", latest=True, **wf)
            )


if __name__ == "__main__":
    render_templates()
