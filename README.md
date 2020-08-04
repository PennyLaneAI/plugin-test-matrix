# Plugin Scheduled CI

This repository contains continuous integration for the official PennyLane plugins.

Continuous-integration is performed by GitHub actions. Tests are executed on every push to `master`,
and are also run on a schedule once a day.

Finally, tests can be triggered manually via the 'Actions' tab.

## Testing matrix

All entries in the matrix are tested against PennyLane latest (GitHub master).

|        | PyPI version                                                                                | Tests (Stable)                                                                                                                                                           | Tests (Latest)                                                                                                                                                           |
|:-------|:--------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Qiskit | ![](https://img.shields.io/pypi/v/pennylane-qiskit?color=green&label=%20&style=flat-square) | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/qiskit-stable/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Aqiskit-stable) | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/qiskit-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Aqiskit-latest) |
| Cirq   | ![](https://img.shields.io/pypi/v/pennylane-cirq?color=green&label=%20&style=flat-square)   | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/cirq-stable/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Acirq-stable)     | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/cirq-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Acirq-latest)     |
|        |                                                                                             |                                                                                                                                                                          |                                                                                                                                                                          |

## Adding a plugin

The file [`workflow-template.yml`](workflow-template.yml) is a Jinja2 template that makes it easy to
add a new plugin to the testing matrix. Simply add a new plugin to the `workflows` list in
[`compile.py`](compile.py), with the following dictionary keys:

* `plugin` (required): the name of the plugin **not including the PennyLane prefix**. The plugin
  repository and PyPI project are inferred from the plugin name. E.g., `'plugin': 'qiskit'` will
  correspond to the GitHub repo PennyLaneAI/pennylane-qiskit and the PyPI project
  `pennylane-qiskit`.

* `requirements` (optional): a list of Python packages that should be installed prior to plugin
  installation. You may use `pip` syntax, e.g., `pyscf==1.7.2`.

* `device_tests` (optional): a list of command line arguments to pass to the PennyLane device
  integration tests. Each list element corresponds to a single test run, e.g.,

  ```python "device_tests": [ "--device=cirq.simulator --tb=short --skip-ops --analytic=True",
  "--device=cirq.simulator --tb=short --skip-ops --analytic=False --shots=8000", ]
  ```

Once you have added your plugin, run

```console $ python compile.py
```

This will autogenerate two workflow files, `.github/workflows/plugin-stable.yml` and
`.github/workflows/plugin-latest.yml`. Finally, make sure to add a row to the testing matrix above!
