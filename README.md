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
- [ ] Basic Framework
  - [ ] Authentication Module
  - [ ] I/O Control Module
  - [ ] Algorithm Unit
- [ ] Data Type Standard
  - [ ] Data Type Check
  - [ ] Data Type Define
- [ ] Example Service
  - [ ] SASA
  - [ ] COREX
  - [ ] Sequence Entropy
- [ ] New Communication Protocol
