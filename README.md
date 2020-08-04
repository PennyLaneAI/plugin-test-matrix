# Plugin CI

This repository contains continuous integration for the official PennyLane plugins.

Continuous-integration is performmed by GitHub actions; all plugin CI workflows are
available in the folder [`.github/workflows`](.github/workflows).

## Testing matrix

All entries in the matrix are tested against PennyLane latest (GitHub master).

|                                                                                                    | Stable                                                                                                                                                                   | Latest                                                                                                                                                                   |
|:---------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Qiskit ![](https://img.shields.io/pypi/v/pennylane-qiskit?color=green&label=%20&style=flat-square) | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/qiskit-stable/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Aqiskit-stable) | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/qiskit-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Aqiskit-latest) |
| Cirq   ![](https://img.shields.io/pypi/v/pennylane-cirq?color=green&label=%20&style=flat-square)   | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/cirq-stable/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Acirq-stable)     | [![](https://github.com/PennyLaneAI/plugin-tests/workflows/cirq-latest/badge.svg)](https://github.com/PennyLaneAI/plugin-tests/actions?query=workflow%3Acirq-latest)     |
|                                                                                                    |                                                                                                                                                                          |                                                                                                                                                                          |