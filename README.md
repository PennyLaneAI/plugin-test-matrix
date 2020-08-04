# Plugin CI

This repository contains continuous integration for the official PennyLane plugins.

Continuous-integration is performmed by GitHub actions; all plugin CI workflows are
available in the folder [`.github/workflows`](.github/workflows).

## Testing matrix

All entries in the matrix are tested against PennyLane latest (GitHub master).

|                   | Stable                                                                                          | Latest                                                                                   |
|---------------    |------------------------------------------------------------------------------------------------ |------------------------------------------------------------------------------------      |
| Qiskit            | ![Qiskit](https://github.com/PennyLaneAI/plugin-tests/workflows/qiskit-stable/badge.svg)        | ![Qiskit](https://github.com/PennyLaneAI/plugin-tests/workflows/qiskit-latest/badge.svg) |
|                   |                                                                                                 |                                                                                          |