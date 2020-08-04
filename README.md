# Plugin CI

This repository contains continuous integration for the official PennyLane plugins.

Continuous-integration is performmed by GitHub actions; all plugin CI workflows are
available in the folder [`.github/workflows`](.github/workflows).

## Testing matrix

|                   | PennyLane v0.9                                                                        | PennyLane master                                                                                                         |
|---------------    |-------------------------------------------------------------------------------------- |----------------------------------------------------------------------------          |
| Qiskit v0.9       | ![Qiskit](https://github.com/PennyLaneAI/plugin-tests/workflows/Qiskit/badge.svg)     | ![Qiskit](https://github.com/PennyLaneAI/plugin-tests/workflows/Qiskit/badge.svg)    |
| Qiskit master     | -                                                                                     | ![Qiskit](https://github.com/PennyLaneAI/plugin-tests/workflows/Qiskit/badge.svg)    |
|                   |                                                                                       |                                                                                      |