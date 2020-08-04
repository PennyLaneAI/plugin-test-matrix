# Plugin Test Matrix

This repository contains scheduled continuous integration for the official PennyLane plugins.

Continuous-integration is performed by GitHub actions. Tests are executed on every push to `master`,
and are also run on a schedule once a day.

Finally, tests can be triggered manually via the 'Actions' tab.

## Testing matrix

All entries in the matrix are tested against PennyLane latest (GitHub master).

|           | PyPI version                                                                                   | Tests (Stable)                                                                                                                                                                 | Tests (Latest)                                                                                                                                                                 |
|:----------|:-----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Qiskit    | ![](https://img.shields.io/pypi/v/pennylane-qiskit?color=green&label=%20&style=flat-square)    | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/qiskit-stable/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Aqiskit-stable)       | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/qiskit-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Aqiskit-latest)       |
| Cirq      | ![](https://img.shields.io/pypi/v/pennylane-cirq?color=green&label=%20&style=flat-square)      | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/cirq-stable/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Acirq-stable)           | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/cirq-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Acirq-latest)           |
| SF        | ![](https://img.shields.io/pypi/v/pennylane-sf?color=green&label=%20&style=flat-square)        | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/sf-stable/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Asf-stable)               | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/sf-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Asf-latest)               |
| Qulacs    | n/a                                                                                            | n/a                                                                                                                                                                            | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/qulacs-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Aqulacs-latest)       |
| AQT       | ![](https://img.shields.io/pypi/v/pennylane-aqt?color=green&label=%20&style=flat-square)       | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/aqt-stable/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Aaqt-stable)             | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/aqt-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Aaqt-latest)             |
| Honeywell | ![](https://img.shields.io/pypi/v/pennylane-honeywell?color=green&label=%20&style=flat-square) | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/honeywell-stable/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Ahoneywell-stable) | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/honeywell-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Ahoneywell-latest) |

*Notes:*

* PennyLane-SF currently depends against Strawberry Fields master, not stable

## Adding a plugin

The file [`workflow-template.yml`](workflow-template.yml) is a Jinja2 template that makes it easy to
add a new plugin to the testing matrix. Simply add a new plugin to the `workflows` list in
[`compile.py`](compile.py), with the following dictionary keys:

* `plugin` (required): the name of the plugin **not including the PennyLane prefix**. The plugin
  repository and PyPI project are inferred from the plugin name. E.g., `'plugin': 'qiskit'` will
  correspond to the GitHub repo PennyLaneAI/pennylane-qiskit and the PyPI project
  `pennylane-qiskit`.

* `which` (required): a set specifying whether to generate a workflow to test the `{"latest"}`
  (GitHub master) version of the plugin, `{"stable"}` (PyPI) version of the plugin, or both `{"latest", "stable"}`.

* `requirements` (optional): a list of Python packages that should be installed prior to plugin
  installation. You may use `pip` syntax, e.g., `pyscf==1.7.2`.

* `device_tests` (optional): a list of command line arguments to pass to the PennyLane device
  integration tests. Each list element corresponds to a single test run, e.g.,

  ```python
  "device_tests":
      [
          "--device=cirq.simulator --tb=short --skip-ops --analytic=True",
          "--device=cirq.simulator --tb=short --skip-ops --analytic=False --shots=8000"
      ]
  ```

Once you have added your plugin, run

```console
$ python compile.py
```

This will autogenerate two workflow files, `.github/workflows/plugin-stable.yml` and
`.github/workflows/plugin-latest.yml`. Finally, make sure to add a row to the testing matrix above!
