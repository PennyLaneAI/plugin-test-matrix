# Plugin Test Matrix

This repository contains regularly scheduled continuous-integration for the official PennyLane plugins.

The continuous integration is performed by GitHub actions. Tests are executed on every push to `master`,
and are also run on a schedule of once per day.

Finally, tests can be triggered manually via the 'Actions' tab.

## Testing matrix

All entries in the matrix are tested against PennyLane latest (GitHub master).

|                                                                        | PyPI version                                                                                              | Stable plugin/stable PennyLane                                                                                                                                                                                                                                  | Stable plugin/latest PennyLane                                                                                                                                                                                                                                  | Latest plugin/ stable PennyLane                                                                                                                                                                                                                                 | Latest plugin/latest PennyLane                                                                                                                                                                                                                                  |
|:-----------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Qiskit](https://github.com/PennyLaneAI/pennylane-qiskit)              | ![](https://img.shields.io/pypi/v/pennylane-qiskit?color=green&label=%20&style=flat-square)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-stable-stable)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-stable-latest)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-latest-stable)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-latest-latest)       |
| [Cirq](https://github.com/PennyLaneAI/pennylane-cirq)                  | ![](https://img.shields.io/pypi/v/pennylane-cirq?color=green&label=%20&style=flat-square)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-stable-stable)           | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-stable-latest)           | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-latest-stable)           | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-latest-latest)           |
| [Qulacs](https://github.com/PennyLaneAI/pennylane-qulacs)              | ![](https://img.shields.io/pypi/v/pennylane-qulacs?color=green&label=%20&style=flat-square)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-stable-stable)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-stable-latest)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-latest-stable)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-latest-latest)       |
| [AQT](https://github.com/PennyLaneAI/pennylane-aqt)                    | ![](https://img.shields.io/pypi/v/pennylane-aqt?color=green&label=%20&style=flat-square)                  | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-stable-stable)             | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-stable-latest)             | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-latest-stable)             | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-latest-latest)             |
| [Honeywell](https://github.com/PennyLaneAI/pennylane-honeywell)        | ![](https://img.shields.io/pypi/v/pennylane-honeywell?color=green&label=%20&style=flat-square)            | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-stable-stable) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-stable-latest) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-latest-stable) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-latest-latest) |
| [IonQ](https://github.com/PennyLaneAI/pennylane-ionq)                  | ![](https://img.shields.io/pypi/v/pennylane-ionq?color=green&label=%20&style=flat-square)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-stable-stable)           | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-stable-latest)           | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-latest-stable)           | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-latest-latest)           |
| [Rigetti](https://github.com/PennyLaneAI/pennylane-rigetti)            | ![](https://img.shields.io/pypi/v/pennylane-rigetti?color=green&label=%20&style=flat-square)              | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Arigetti-stable-stable)     | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Arigetti-stable-latest)     | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Arigetti-latest-stable)     | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Arigetti-latest-latest)     |
| [ProjectQ](https://github.com/PennyLaneAI/pennylane-pq)                | ![](https://img.shields.io/pypi/v/pennylane-pq?color=green&label=%20&style=flat-square)                   | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/pq-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-stable-stable)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/pq-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-stable-latest)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/pq-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-latest-stable)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/pq-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-latest-latest)               |
| [Lightning](https://github.com/PennyLaneAI/pennylane-lightning)        | ![](https://img.shields.io/pypi/v/pennylane-lightning?color=green&label=%20&style=flat-square)            | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-stable-stable) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-stable-latest) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-latest-stable) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-latest-latest) |
| [Orquestra](https://github.com/PennyLaneAI/pennylane-orquestra)        | ![](https://img.shields.io/pypi/v/pennylane-orquestra?color=green&label=%20&style=flat-square)            | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-stable-stable) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-stable-latest) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-latest-stable) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-latest-latest) |
| [Braket](https://github.com/aws/amazon-braket-pennylane-plugin-python) | ![](https://img.shields.io/pypi/v/amazon-braket-pennylane-plugin?color=green&label=%20&style=flat-square) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-stable-stable)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-stable-latest)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-latest-stable)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-latest-latest)       |

*Notes:*

* The device integration tests currently do not support devices with a fixed
  number of wires; as a result, `rigetti.qvm` is not tested.

* The Braket plugin device integration tests are run with `-k “not Sample and not no_0_shots”`,
  see #6

## QML repo

|                                                                                                                   | Status                                                                                                                                                                                                   |
|:------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`build-branch-dev`](https://github.com/PennyLaneAI/qml/blob/master/.github/workflows/build-branch-dev.yml)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/qml/build-branch-dev.yml)](https://github.com/PennyLaneAI/qml/actions/workflows/build-branch-dev.yml)       |
| [`build-branch-master`](https://github.com/PennyLaneAI/qml/blob/master/.github/workflows/build-branch-master.yml) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/qml/build-branch-master.yml)](https://github.com/PennyLaneAI/qml/actions/workflows/build-branch-master.yml) |

## Catalyst compiler

The following table shows the current Catalyst compatibility with the Lightning and PennyLane packages, where each of the 3 packages is tested as "latest" and "stable". Latest versions are built directly from the repository's main or master branch, while stable is built from the repository at the most recent release tag. The reason this is needed rather than installing PyPI packages is that the Lightning dependency in Catalyst needs to be built from source and cannot be obtained from the PyPI package. PennyLane stable is installed from PyPI.

<table>
  <tr>
    <td></td>
    <td colspan="2">PennyLane <b>stable</b></td>
    <td colspan="2">PennyLane <b>latest</b></td>
  </tr>
  <tr>
    <td></td>
    <td>Lightning <b>stable</b></td>
    <td>Lightning <b>latest</b></td>
    <td>Lightning <b>stable</b></td>
    <td>Lightning <b>latest</b></td>
  </tr>
  <tr>
    <td>Catalyst <b>stable</b></td>
    <td><a href=https://github.com/PennyLaneAI/catalyst/actions/workflows/CPL_stable-stable-stable.yaml><img src=https://img.shields.io/github/actions/workflow/status/PennyLaneAI/catalyst/CPL_stable-stable-stable.yaml alt="Check CPL stable/stable/stable"></a></td>
    <td><a href=https://github.com/PennyLaneAI/catalyst/actions/workflows/CPL_stable-stable-latest.yaml><img src=https://img.shields.io/github/actions/workflow/status/PennyLaneAI/catalyst/CPL_stable-stable-latest.yaml alt="Check CPL stable/stable/latest"></a></td>
    <td><a href=https://github.com/PennyLaneAI/catalyst/actions/workflows/CPL_stable-latest-stable.yaml><img src=https://img.shields.io/github/actions/workflow/status/PennyLaneAI/catalyst/CPL_stable-latest-stable.yaml alt="Check CPL stable/latest/stable"></a></td>
    <td><a href=https://github.com/PennyLaneAI/catalyst/actions/workflows/CPL_stable-latest-latest.yaml><img src=https://img.shields.io/github/actions/workflow/status/PennyLaneAI/catalyst/CPL_stable-latest-latest.yaml alt="Check CPL stable/latest/latest"></a></td>
  </tr>
  <tr>
    <td>Catalyst <b>latest</b></td>
    <td><a href=https://github.com/PennyLaneAI/catalyst/actions/workflows/CPL_latest-stable-stable.yaml><img src=https://img.shields.io/github/actions/workflow/status/PennyLaneAI/catalyst/CPL_latest-stable-stable.yaml alt="Check CPL latest/stable/stable"></a></td>
    <td><a href=https://github.com/PennyLaneAI/catalyst/actions/workflows/CPL_latest-stable-latest.yaml><img src=https://img.shields.io/github/actions/workflow/status/PennyLaneAI/catalyst/CPL_latest-stable-latest.yaml alt="Check CPL latest/stable/latest"></a></td>
    <td><a href=https://github.com/PennyLaneAI/catalyst/actions/workflows/CPL_latest-latest-stable.yaml><img src=https://img.shields.io/github/actions/workflow/status/PennyLaneAI/catalyst/CPL_latest-latest-stable.yaml alt="Check CPL latest/latest/stable"></a></td>
    <td><a href=https://github.com/PennyLaneAI/catalyst/actions/workflows/CPL_latest-latest-latest.yaml><img src=https://img.shields.io/github/actions/workflow/status/PennyLaneAI/catalyst/CPL_latest-latest-latest.yaml alt="Check CPL latest/latest/latest"></a></td>
  </tr>
</table>

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

All entries in the matrix are tested against the PennyLane release candidate branch (GitHub `v0.29.0-rc0` branch).

|                                                                        | Latest plugin/ release candidate PennyLane                                                                                                                                                                                                              |
|:-----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Qiskit](https://github.com/PennyLaneAI/pennylane-qiskit)              | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqiskit-latest-rc)       |
| [Cirq](https://github.com/PennyLaneAI/pennylane-cirq)                  | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Acirq-latest-rc)           |
| [Qulacs](https://github.com/PennyLaneAI/pennylane-qulacs)              | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aqulacs-latest-rc)       |
| [AQT](https://github.com/PennyLaneAI/pennylane-aqt)                    | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aaqt-latest-rc)             |
| [Honeywell](https://github.com/PennyLaneAI/pennylane-honeywell)        | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Ahoneywell-latest-rc) |
| [IonQ](https://github.com/PennyLaneAI/pennylane-ionq)                  | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aionq-latest-rc)           |
| [Rigetti](https://github.com/PennyLaneAI/pennylane-rigetti)            | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Arigetti-latest-rc)     |
| [ProjectQ](https://github.com/PennyLaneAI/pennylane-pq)                | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/pq-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Apq-latest-rc)               |
| [Lightning](https://github.com/PennyLaneAI/pennylane-lightning)        | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Alightning-latest-rc) |
| [Orquestra](https://github.com/PennyLaneAI/pennylane-orquestra)        | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/orquestra-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Aorquestra-latest-rc) |
| [Braket](https://github.com/aws/amazon-braket-pennylane-plugin-python) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions?query=workflow%3Abraket-latest-rc)       |


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
* `.github/workflows/plugin-latest-rc.yml`

Finally, make sure to add a row to the testing matrix above!
