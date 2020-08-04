from jinja2 import FileSystemLoader, Environment


workflows = [
    {
        "plugin": "qiskit",
        "requirements": ["qiskit", "pyscf==1.7.2"],
        "device_tests": [
            "--device=qiskit.basicaer --tb=short --skip-ops --shots=8000",
            "--device=qiskit.aer --tb=short --skip-ops --shots=8000",
        ]
    },
    {
        "plugin": "cirq",
        "requirements": ["cirq"],
        "device_tests": [
            "--device=cirq.simulator --tb=short --skip-ops --analytic=True",
            "--device=cirq.simulator --tb=short --skip-ops --analytic=False --shots=8000",
            "--device=cirq.mixedsimulator --tb=short --skip-ops --analytic=True",
            "--device=cirq.mixedsimulator --tb=short --skip-ops --analytic=False --shots=8000",
        ]
    },
]


def render_from_template(**kwargs):
    loader = FileSystemLoader(".")
    env = Environment(loader=loader)
    template = env.get_template("workflow-template.yml")
    return template.render(**kwargs)


def render_templates():

    for wf in workflows:
        for i in ["latest", "stable"]:
            with open(f".github/workflows/{wf['plugin']}-{i}.yml", "w") as f:
                f.write(render_from_template(latest=i == "latest", **wf))


if __name__ == "__main__":
    render_templates()
