<img src="images/tulane_long.png" width="128px">
<img src="images/icon_long.png" width="128px"> 

# EasyAPI
`UPDATED: 2024/10/12, JIARUI LI`

## Introduction
This project aims to transform a wide range of algorithms—currently implemented as functions, modules, or command-line tools—into accessible services by deploying them through a universal RESTful API server. By adhering to RESTful API standards, the project facilitates easy integration of these algorithms, enabling users to interact with them in a standardized and efficient manner.
The core objective is to develop a flexible API server framework that allows any algorithm to be seamlessly wrapped as a RESTful service. Additionally, we will define a series of data types under a unified protocol to ensure consistency and interoperability across different algorithms and services.
Moreover, the project will introduce an innovative communication protocol that combines elements of existing standards with novel features. This hybrid protocol will allow for delayed response handling, enabling requests to the API to be processed asynchronously and delivering results once they are available.
This approach provides a scalable and user-friendly platform for algorithm deployment and access, streamlining computational tasks across diverse environments.

If there is any issue, please put up with an issue or contact Jiarui Li (jli78@tulane.edu)

## TO-DO
- [x] Basic Framework
  - [x] Authentication Module
  - [x] I/O Control Module
  - [x] Algorithm Unit
  - [x] Auto Algorithm Inference
  - [x] Batch Load
  - [x] Memoization Cache
- [x] Data Type Standard
  - [x] Data Type Check
  - [x] Data Type Define
  - [x] Parameter Support
- [ ] Advanced Schedule Queue
  - [x] Allow Cancel
  - [x] Multipe Resource-dependent Queue
  - [ ] Dynamic Queue Layout
- [ ] Advanced Authority
  - [ ] Remote API Key
  - [ ] Resourse Control
- [ ] Documentation
  - [ ] RESTful Documentation
  - [x] Basic Documentation
- [x] Example Service
  - [x] SASA
  - [x] COREX
  - [x] BFactor
  - [x] Chain List & Selection
  - [x] PDB Fetch
  - [x] Sequence Entropy
  - [x] APL
  - [x] MHC-II
- [x] Communication Protocol
  - [x] WebSocket

## Start Server
```python
fastapi run easyapi
```