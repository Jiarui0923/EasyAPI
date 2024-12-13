<img src="/images/tulane_long.png" width="128px">
<img src="/images/icon_long.png" width="128px"> 

# EasyAPI Configuration Guideline
`Update: 2024-12-13`

The EasyAPI configuration is a json files including 6 sections including server_name, task_queue, authenticator, iolib, cache, and modules.

The server will use `config.json` under the same path where the server is launched. If `config.json` does not exist, it will use internal configurations.

To change the configuration file path, please set environment variable `easyapi_config` to the `config.json` absolute path.

## Example Configuration
This is an example configuration. Build two task queues with 1 CPU. Use a JSON file as authenticator. The cache backend is MongoDB. Only one module (`add_number`) loaded.
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

### Server Name
- Key: `"server_name"`
- Default: `"local"`

Set the server name. This will affected later server index. Please name it follow Python variable name standard.

### Task Queue
- Key: `"task_queue"`

Configure the task queues affiliated with computational resources.
- Queue Layouts
  - Key: `"layouts"`
  This is a list of dictionaries. Each dictionary defined a queue and its resources. The dictionary should follow format `{"cpu":cpu_number, "cuda":cuda_number}` to defined number of CPU and CUDA assigned to this queue.

### Authenticator
- Key: `"authenticator"`

Configure the authenticator for the API.
There are two types of Authenticator provided:
1. memory: directly load credentials to memory.
   - `"type"` = `"memory"`
   - `"credentials"` = `{}` The credentials should be loaded to memory.
2. json: dynamically load credentials from a given json file.
   - `"type"` = `"json"`
   - `"file"` = `"credentials.json"` to the JSON file storing credentials

**Credential file/dictionary format:**  
It should be a dictionary. For each key-value pair, key is the API ID and value consists of `"key"` anf `"access"`. `"key"` is the API key and `"access"` is access field that should be a list. If the first item is `"*"`, this credential can access all algorithms. If it is a list of algorithm ids, this credential can only access these algorithms.

Example:
```json
{
    "fuv249---": {
        "key": "adhjd--------",
        "access": ["*"]
    }
}
```

### IO-Lib Cache
- Key: `"iolib"`

Where the I/O types should be cached together.

1. File Cache
   - `"file"` = `"iolib.json"` Which file used to cache.

### Algorithm Result Cache
- Key: `"cache"`

To accelerate algorithm and avoid duplicated computation, EasyAPI will create signature for the given parameter and store it with the result. For the next query, it will directly fetch the result.

There are two cache backend provided `mongodb` and `memory`
1. memory: Everything will be cached in memory, and will ne cleaned after server shutdown.
   - `"type"` = `"memory"`
   - `"hash"` = `"MD5"` The method used to create parameter signature. Could be `MD5`, `SHA1`, `SHA256`, and `SHA512`.
2. mongodb: Cache will be maintained by mongodb, which could be loaded back after restart.
   - `"type"` = `"mongodb"`
   - `"host"` = `"mongodb://localhost"` The mongodb host
   - `"database"` = `"easyapi_cache"` Databased used for cache.
   - `"hash"` = `"MD5"` The method used to create parameter signature. Could be `MD5`, `SHA1`, `SHA256`, and `SHA512`.
  
### Algorithm Modules
- Key: `"modules"`

The algorithm modules need to be loaded. It should be a list of importable string. It could be an installed module or a indexable module under current path.

Example:
```json
"modules": [
    "algorithms.add_number"
]
```