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
  - [x] External Settings
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
  - [x] Entry Control
- [ ] Documentation
  - [ ] RESTful Documentation
  - [x] Basic Documentation
- [x] Communication Protocol
  - [x] WebSocket

## Requirements
All code was developed in Python 3.12.x.

|Package|Version|Usage|Website|Require|
|:------|:-----:|:----|:-----:|:-----:|
|fastapi <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="64pt">|`0.112.1`|Basic API Framework|[<img src="/images/icons/link.png" width="20pt">](https://fastapi.tiangolo.com/)|`REQUIRED`|
|pandas <img src="https://pandas.pydata.org/docs/_static/pandas.svg" width="52pt">|`2.2.2`|Data processing|[<img src="/images/icons/link.png" width="20pt">](https://pandas.pydata.org/)|`REQUIRED`|
|numpy <img src="https://numpy.org/images/logo.svg" width="16pt">|`1.26.4`|Mathmatical computation|[<img src="/images/icons/link.png" width="20pt">](https://numpy.org/)|`REQUIRED`|
|pymongo <img src="https://webimages.mongodb.com/_com_assets/cms/kuyjf3vea2hg34taa-horizontal_default_slate_blue.svg?auto=format%252Ccompress" width="64pt">|`4.10.1`|MongoDB Access|[<img src="/images/icons/link.png" width="20pt">](https://www.mongodb.com/zh-cn/docs/languages/python/pymongo-driver/current/)|`OPTIONAL`|

**NOTICE**: To install `fastapi`, please follow: `pip install "fastapi[standard]"`.

## Server Configuration
More settings and details could be found at [Server Configuration](/docs/config_guide.md).  
The EasyAPI configuration is a json files including 6 sections including server_name, task_queue, authenticator, iolib, cache, and modules.  
The server will use `config.json` under the same path where the server is launched. If `config.json` does not exist, it will use internal configurations.  
To change the configuration file path, please set environment variable `easyapi_config` to the `config.json` absolute path.

This is an example server configuration:
```json
{
    "server_name": "local_test",
    "task_queue": {
        "layouts": [
            {"cpu":1, "cuda":0},
            {"cpu":1, "cuda":0}
        ]
    },
    "authenticator": {
        "type": "json",
        "file": "credentials.json"
    },
    "iolib": {
        "file": "iolib.json"
    },
    "cache": {
        "type": "mongodb",
        "host": "mongodb://localhost",
        "database": "easyapi_cache",
        "hash": "MD5"
    },
    "modules": [
        "algorithms.add_number"
    ]
}
```


## Start Server
To run the server (on port 8000), please run:
```bash
fastapi run easyapi
```
To change the server port:
```bash
fastapi run easyapi --port 8001
```
To run under developement mode:
```bash
fastapi dev easyapi
```