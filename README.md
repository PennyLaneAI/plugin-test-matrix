# Plugin Test Matrix

This repository contains regularly scheduled continuous-integration for the official PennyLane plugins.

The continuous integration is performed by GitHub actions. Tests are executed on every push to `master`,
and are also run on a schedule of once per day.

Finally, tests can be triggered manually via the 'Actions' tab.

## Testing matrix

All entries in the matrix are tested against PennyLane latest (GitHub master).


|                                                                             | PyPI version                                                                                              | Stable plugin/stable PennyLane                                                                                                                                                                                                                                            | Stable plugin/latest PennyLane                                                                                                                                                                                                                                            | Latest plugin/ stable PennyLane                                                                                                                                                                                                                                           | Latest plugin/latest PennyLane                                                                                                                                                                                                                                            |
| :-------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Qiskit](https://github.com/PennyLaneAI/pennylane-qiskit)                   | ![](https://img.shields.io/pypi/v/pennylane-qiskit?color=green&label=%20&style=flat-square)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qiskit-stable-stable.yml)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qiskit-stable-latest.yml)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qiskit-latest-stable.yml)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qiskit-latest-latest.yml)                 |
| [Cirq](https://github.com/PennyLaneAI/pennylane-cirq)                       | ![](https://img.shields.io/pypi/v/pennylane-cirq?color=green&label=%20&style=flat-square)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/cirq-stable-stable.yml)                     | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/cirq-stable-latest.yml)                     | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/cirq-latest-stable.yml)                     | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/cirq-latest-latest.yml)                     |
| [Qulacs](https://github.com/PennyLaneAI/pennylane-qulacs)                   | ![](https://img.shields.io/pypi/v/pennylane-qulacs?color=green&label=%20&style=flat-square)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qulacs-stable-stable.yml)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qulacs-stable-latest.yml)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qulacs-latest-stable.yml)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qulacs-latest-latest.yml)                 |
| [AQT](https://github.com/PennyLaneAI/pennylane-aqt)                         | ![](https://img.shields.io/pypi/v/pennylane-aqt?color=green&label=%20&style=flat-square)                  | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/aqt-stable-stable.yml)                       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/aqt-stable-latest.yml)                       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/aqt-latest-stable.yml)                       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/aqt-latest-latest.yml)                       |
| [Honeywell](https://github.com/PennyLaneAI/pennylane-honeywell)             | ![](https://img.shields.io/pypi/v/pennylane-honeywell?color=green&label=%20&style=flat-square)            | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/honeywell-stable-stable.yml)           | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/honeywell-stable-latest.yml)           | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/honeywell-latest-stable.yml)           | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/honeywell-latest-latest.yml)           |
| [IonQ](https://github.com/PennyLaneAI/pennylane-ionq)                       | ![](https://img.shields.io/pypi/v/pennylane-ionq?color=green&label=%20&style=flat-square)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/ionq-stable-stable.yml)                     | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/ionq-stable-latest.yml)                     | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/ionq-latest-stable.yml)                     | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/ionq-latest-latest.yml)                     |
| [Rigetti](https://github.com/PennyLaneAI/pennylane-rigetti)                 | ![](https://img.shields.io/pypi/v/pennylane-rigetti?color=green&label=%20&style=flat-square)              | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/rigetti-stable-stable.yml)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/rigetti-stable-latest.yml)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/rigetti-latest-stable.yml)               | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/rigetti-latest-latest.yml)               |
| [Lightning](https://github.com/PennyLaneAI/pennylane-lightning)             | ![](https://img.shields.io/pypi/v/pennylane-lightning?color=green&label=%20&style=flat-square)            | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/pennylane-lightning/compat-check-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/pennylane-lightning/actions/workflows/compat-check-stable-stable.yml)      | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/pennylane-lightning/compat-check-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/pennylane-lightning/actions/workflows/compat-check-stable-latest.yml)      | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/pennylane-lightning/compat-check-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/pennylane-lightning/actions/workflows/compat-check-latest-stable.yml)      | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/pennylane-lightning/compat-check-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/pennylane-lightning/actions/workflows/compat-check-latest-latest.yml)      |
| [Braket](https://github.com/aws/amazon-braket-pennylane-plugin-python)      | ![](https://img.shields.io/pypi/v/amazon-braket-pennylane-plugin?color=green&label=%20&style=flat-square) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/braket-stable-stable.yml)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/braket-stable-latest.yml)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/braket-latest-stable.yml)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/braket-latest-latest.yml)                 |
| [Quantum Inspire](https://github.com/QuTech-Delft/pennylane-quantuminspire) | ![](https://img.shields.io/pypi/v/pennylane-quantuminspire?color=green&label=%20&style=flat-square)       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/quantuminspire-stable-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/quantuminspire-stable-stable.yml) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/quantuminspire-stable-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/quantuminspire-stable-latest.yml) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/quantuminspire-latest-stable.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/quantuminspire-latest-stable.yml) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/quantuminspire-latest-latest.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/quantuminspire-latest-latest.yml) |


*Notes:*

* The device integration tests currently do not support devices with a fixed
  number of wires; as a result, `rigetti.qvm` is not tested.

* The Braket plugin device integration tests are run with `-k “not Sample and not no_0_shots”`,
  see #6
  
* The Qiskit tests above are run with `-k 'not test_ibmq.py and not test_runtime.py'`, that is, 
  without using devices that access the IBMQ backend. The IBMQ backend is tested via `test_ibmp.qpy` 
  and `test_runtime.py` tests on the latest version of Pennylane and the plugin twice a week. 
  Their status is shown below:

|                                                                | Status                                                                                                                                                                                                                         |
|:---------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Qiskit-IBMQ](https://github.com/PennyLaneAI/pennylane-qiskit) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/pennylane-qiskit/ibmq_tests.yml?branch=master)](https://github.com/PennyLaneAI/pennylane-qiskit/actions/workflows/ibmq_tests.yml) |



## QML repo

|                                                                                                                   | Status                                                                                                                                                                                                   |
| :---------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
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

All entries in the matrix are tested against the PennyLane release candidate branch (GitHub `vX.XX.X-rc0` branch).

|                                                                             | Latest plugin/ release candidate PennyLane                                                                                                                                                                                                                     |
|:----------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Qiskit](https://github.com/PennyLaneAI/pennylane-qiskit)                   | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qiskit-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qiskit-latest-rc.yml)                 |
| [Cirq](https://github.com/PennyLaneAI/pennylane-cirq)                       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/cirq-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/cirq-latest-rc.yml)                     |
| [Qulacs](https://github.com/PennyLaneAI/pennylane-qulacs)                   | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/qulacs-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/qulacs-latest-rc.yml)                 |
| [AQT](https://github.com/PennyLaneAI/pennylane-aqt)                         | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/aqt-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/aqt-latest-rc.yml)                       |
| [Honeywell](https://github.com/PennyLaneAI/pennylane-honeywell)             | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/honeywell-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/honeywell-latest-rc.yml)           |
| [IonQ](https://github.com/PennyLaneAI/pennylane-ionq)                       | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/ionq-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/ionq-latest-rc.yml)                     |
| [Rigetti](https://github.com/PennyLaneAI/pennylane-rigetti)                 | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/rigetti-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/rigetti-latest-rc.yml)               |
| [Lightning](https://github.com/PennyLaneAI/pennylane-lightning)             | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/lightning-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/lightning-latest-rc.yml)           |
| [Catalyst](https://github.com/PennyLaneAI/catalyst)                         | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/catalyst/CPL_latest-rc-latest.yaml)](https://github.com/PennyLaneAI/catalyst/actions/workflows/CPL_latest-rc-latest.yaml)                                         |
| [Braket](https://github.com/aws/amazon-braket-pennylane-plugin-python)      | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/braket-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/braket-latest-rc.yml)                 |
| [Quantum Inspire](https://github.com/QuTech-Delft/pennylane-quantuminspire) | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/PennyLaneAI/plugin-test-matrix/quantuminspire-latest-rc.yml?branch=master)](https://github.com/PennyLaneAI/plugin-test-matrix/actions/workflows/quantuminspire-latest-rc.yml) |


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

* `token` (optional): sets an environment variable with the same name as the token. The value is loaded from the
  repository secrets. The token is required by some plugins for backend authentication.

* `additional_env_vars` (optional): string containing additional environment variables you'd like to be set for
  the CI action. Double-check the whitespace when using this - variables should be separated with "\n  "

* `runs_on` (optional): string to override the workflow's default `runs-on` attribute of `ubuntu-latest`.

* `test_kwargs` (optional): additional arguments to pass to pytest for the given plugin.

* `no_deprecation_error` (optional): set to True to not raise PL deprecation warnings as errors when testing
  the latest version of the plugin. By default, PL deprecation warnings are raised as errors.

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
