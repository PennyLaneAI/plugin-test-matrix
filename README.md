# Plugin Test Matrix

This repository contains scheduled continuous integration for the official PennyLane plugins.

Continuous integration is performed by GitHub actions. Tests are executed on every push to `master`,
and are also run on a schedule of once per day.

Finally, tests can be triggered manually via the 'Actions' tab.

## Testing matrix

All entries in the matrix are tested against PennyLane latest (GitHub master).

|           | PyPI version                                                                                   | Stable plugin/stable PennyLane                                                                                                                                                                                                                          | Stable plugin/latest PennyLane                                                                                                                                                                                                                          | Latest plugin/ stable PennyLane                                                                                                                                                                                                                          | Latest plugin/latest PennyLane                                                                                                                                                                                                                          |
|:----------|:-----------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Qiskit](https://github.com/PennyLaneAI/pennylane-qiskit)    | ![](https://img.shields.io/pypi/v/pennylane-qiskit?color=green&label=%20&style=flat-square)    | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-stable-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-stable-latest)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-latest-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-latest-latest)       |
| [Cirq](https://github.com/PennyLaneAI/pennylane-cirq)      | ![](https://img.shields.io/pypi/v/pennylane-cirq?color=green&label=%20&style=flat-square)      | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-stable-stable)           | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-stable-latest)           | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-latest-stable)           | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-latest-latest)           |
| [SF](https://github.com/PennyLaneAI/pennylane-sf)        | ![](https://img.shields.io/pypi/v/pennylane-sf?color=green&label=%20&style=flat-square)        | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/sf-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Asf-stable-stable)               | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/sf-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Asf-stable-latest)               | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/sf-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Asf-latest-stable)               | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/sf-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Asf-latest-latest)               |
| [Qulacs](https://github.com/PennyLaneAI/pennylane-qulacs)    | ![](https://img.shields.io/pypi/v/pennylane-qulacs?color=green&label=%20&style=flat-square)    | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-stable-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-stable-latest)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-latest-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-latest-latest)       |
| [AQT](https://github.com/PennyLaneAI/pennylane-aqt)       | ![](https://img.shields.io/pypi/v/pennylane-aqt?color=green&label=%20&style=flat-square)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-stable-stable)             | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-stable-latest)             | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-latest-stable)             | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-latest-latest)             |
| [Honeywell](https://github.com/PennyLaneAI/pennylane-honeywell) | ![](https://img.shields.io/pypi/v/pennylane-honeywell?color=green&label=%20&style=flat-square) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-stable-stable) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-stable-latest) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-latest-stable) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-latest-latest) |
| [IonQ](https://github.com/PennyLaneAI/pennylane-ionq) | ![](https://img.shields.io/pypi/v/pennylane-ionq?color=green&label=%20&style=flat-square) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-stable-stable) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-stable-latest) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-latest-stable) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-latest-latest) |
| [Forest](https://github.com/rigetti/pennylane-forest)    | ![](https://img.shields.io/pypi/v/pennylane-forest?color=green&label=%20&style=flat-square)    | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/forest-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aforest-stable-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/forest-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aforest-stable-latest)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/forest-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aforest-latest-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/forest-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aforest-latest-latest)       |
| [ProjectQ](https://github.com/PennyLaneAI/pennylane-pq)  | ![](https://img.shields.io/pypi/v/pennylane-pq?color=green&label=%20&style=flat-square)        | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/pq-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-stable-stable)               | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/pq-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-stable-latest)               | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/pq-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-latest-stable)               | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/pq-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-latest-latest)               |
| [Lightning](https://github.com/PennyLaneAI/pennylane-lightning) | ![](https://img.shields.io/pypi/v/pennylane-lightning?color=green&label=%20&style=flat-square)    | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-stable-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-stable-latest)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-latest-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-latest-latest)       |
| [Orquestra](https://github.com/PennyLaneAI/pennylane-orquestra) | ![](https://img.shields.io/pypi/v/pennylane-orquestra?color=green&label=%20&style=flat-square)    | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-stable-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-stable-latest)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-latest-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-latest-latest)       |
| [Braket](https://github.com/aws/amazon-braket-pennylane-plugin-python) | ![](https://img.shields.io/pypi/v/amazon-braket-pennylane-plugin?color=green&label=%20&style=flat-square)    | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/braket-stable-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-stable-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/braket-stable-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-stable-latest)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/braket-latest-stable?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-latest-stable)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/braket-latest-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-latest-latest)       |

*Notes:*

* The device integration tests currently do not support devices with a fixed
  number of wires; as a result, `forest.qvm` is not tested.
  
* The Braket plugin device integration tests are run with `-k “not Sample and not no_0_shots”`,
  see #6

## QML repo

|           |   Status  |
|:----------|:----------|
| [`build-dev`](https://github.com/PennyLaneAI/qml/actions/workflows/build-dev.yml) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/qml/build-dev?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/qml/actions?query=workflow%3Abuild-dev) |
| [`build-master`](https://github.com/PennyLaneAI/qml/actions/workflows/build-master.yml) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/qml/build-master?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/qml/actions?query=workflow%3Abuild-master) |

## Interpreting the test matrix

* **Stable/stable**: This reflects a scenario where PennyLane and the plugin are both installed
  from PyPI. This column should **always** pass. If this test fails, it indicates that either (a) a
  bug exists, or (b) an upstream dependency (such as Qiskit or Qulacs)
  were released with breaking changes. In both cases, a bugfix release of the plugin should be made.

* **Stable/latest passing**: A new plugin release is not essential; the current
  PyPI release will continue to work once the new PennyLane version is released.

  - **Latest/latest passing**: Nothing to be done! However, it is still worth checking the
    plugin repository to see if new unreleased changes have been added that would
    be worth releasing.

  - **Latest/latest failing**: Indicates that recent changes have been made to the plugin repository
    post-release; further updates must be made to the plugin to ensure GitHub master passes.

* **Stable/latest failing**: A new plugin release is required for compatibility
  with the upcoming PennyLane release.

  - **Latest/latest failing**: Updates must be made to the plugin to ensure GitHub
    master passes.

  - **Latest/stable failing**: The requirement of PennyLane in the plugin will
    have to be increased.

  - **Latest/latest passing**: Nothing to be done! The plugin is ready to be released
    with the upcoming PennyLane release.

## Feature freeze testing matrix

All entries in the matrix are tested against the PennyLane release candidate branch (GitHub `v0.21.0-rc0` branch).

|           | Latest plugin/ release candidate PennyLane                                                                                                                                                                                                                          |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Qiskit](https://github.com/PennyLaneAI/pennylane-qiskit)    | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-rc-latest)       |
| [Cirq](https://github.com/PennyLaneAI/pennylane-cirq)      | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-rc-latest)           |
| [SF](https://github.com/PennyLaneAI/pennylane-sf)        | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/sf-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Asf-rc-latest)               |
| [Qulacs](https://github.com/PennyLaneAI/pennylane-qulacs)    | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-rc-latest)       |
| [AQT](https://github.com/PennyLaneAI/pennylane-aqt)       | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-rc-latest)             |
| [Honeywell](https://github.com/PennyLaneAI/pennylane-honeywell) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-rc-latest) |
| [IonQ](https://github.com/PennyLaneAI/pennylane-ionq) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-rc-latest) |
| [Forest](https://github.com/rigetti/pennylane-forest)    | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/forest-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aforest-rc-latest)       |
| [ProjectQ](https://github.com/PennyLaneAI/pennylane-pq)  | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/pq-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-rc-latest)               |
| [Lightning](https://github.com/PennyLaneAI/pennylane-lightning) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-rc-latest)       |
| [Orquestra](https://github.com/PennyLaneAI/pennylane-orquestra) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-rc-latest)       |
| [Braket](https://github.com/aws/amazon-braket-pennylane-plugin-python) | [![](https://img.shields.io/github/workflow/status/PennyLaneAI/plugin-test-matrix/braket-rc-latest?label=%20&logo=github&style=flat-square)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-rc-latest)       |


## Adding a plugin

Two Jinja2 workflow templates are provided, that makes it easier to add a new plugin to the test matrix:

* [`workflow-template-latest.yml`](workflow-template-latest.yml): for testing plugins against PennyLane latest
* [`workflow-template-stable.yml`](workflow-template-stable.yml): for testing plugins against PennyLane stable

Simply add a new plugin to the `workflows` list in [`compile.py`](compile.py), with the following dictionary keys:

* `plugin` (required): the name of the plugin **not including the PennyLane prefix**. The plugin
  repository and PyPI project are inferred from the plugin name. E.g., `'plugin': 'qiskit'` will
  correspond to the GitHub repo PennyLaneAI/pennylane-qiskit and the PyPI project
  `pennylane-qiskit`.

* `gh_user` (required): the GitHub user or organization which hosts the plugin repository.

* `which` (required): a set specifying whether to generate a workflow to test the `{"latest"}`
  (GitHub master) version of the plugin, `{"stable"}` (PyPI) version of the plugin, or both `{"latest", "stable"}`.

* `requirements` (optional): a list of Python packages that should be installed prior to plugin
  installation. You may use `pip` syntax, e.g., `pyscf==1.7.2`.

* `requirements_latest` (optional): *additional* list of Python packages that should be installed prior to
  latest/GitHub master plugin installation. For example, if the latest version of the plugin depends on a
  development version of a particular framework.

* `device_tests` (optional): a list of command line arguments to pass to the PennyLane device
  integration tests. Each list element corresponds to a single test run, e.g.,

  ```python
  "device_tests":
      [
          "--device=cirq.simulator --tb=short --skip-ops --analytic=True",
          "--device=cirq.simulator --tb=short --skip-ops --analytic=False --shots=8000"
      ]
  ```

* `additional_setup` (optional): multiline string containing additional GitHub actions for execution
  before the installment of plugins.

Once you have added your plugin, run

```console
$ python compile.py
```

This will autogenerate up to five workflow files, depending on the variable `which`:

* `.github/workflows/plugin-stable-stable.yml`
* `.github/workflows/plugin-stable-latest.yml`
* `.github/workflows/plugin-latest-stable.yml`
* `.github/workflows/plugin-latest-latest.yml`
* `.github/workflows/plugin-rc-latest.yml`

Finally, make sure to add a row to the testing matrix above!
