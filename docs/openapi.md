---
title: EasyAPI v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="easyapi">EasyAPI v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

This project aims to transform a wide range of algorithms—currently implemented as functions, modules, or command-line tools—into accessible services by deploying them through a universal RESTful API server. By adhering to RESTful API standards, the project facilitates easy integration of these algorithms, enabling users to interact with them in a standardized and efficient manner.
The core objective is to develop a flexible API server framework that allows any algorithm to be seamlessly wrapped as a RESTful service. Additionally, we will define a series of data types under a unified protocol to ensure consistency and interoperability across different algorithms and services.
Moreover, the project will introduce an innovative communication protocol that combines elements of existing standards with novel features. This hybrid protocol will allow for delayed response handling, enabling requests to the API to be processed asynchronously and delivering results once they are available.
This approach provides a scalable and user-friendly platform for algorithm deployment and access, streamlining computational tasks across diverse environments.

<h1 id="easyapi-i-o-types">I/O Types</h1>

## get_type_list_io__get

<a id="opIdget_type_list_io__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /io/ \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /io/ HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/io/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/io/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/io/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/io/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/io/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/io/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /io/`

*Get Type List*

Retrieves a paginated list of I/O types, with optional full details.

Parameters:
----------
skip : int
    The number of entries to skip (for pagination).
limit : int
    The maximum number of entries to return (for pagination).
full : bool
    If true, return full details of the I/O types.
auth_id : str
    The ID of the user making the request, used for authorization.
    
Returns:
-------
dict
    A dictionary containing the total number of I/O types, skip, limit, and the records (list of I/O types).
    
Raises:
------
HTTPException
    If the skip value exceeds the total number of I/O types.

<h3 id="get_type_list_io__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|skip|query|integer|false|none|
|limit|query|integer|false|none|
|full|query|boolean|false|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_type_list_io__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_type_list_io__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_type_schema_io__io_id__get

<a id="opIdget_type_schema_io__io_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /io/{io_id} \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /io/{io_id} HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/io/{io_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/io/{io_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/io/{io_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/io/{io_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/io/{io_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/io/{io_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /io/{io_id}`

*Get Type Schema*

Retrieves the schema for a specific I/O type by its ID.

Parameters:
----------
io_id : str
    The ID of the I/O type to retrieve the schema for.
auth_id : str
    The ID of the user making the request, used for authorization.

Returns:
-------
dict
    The schema of the requested I/O type.

Raises:
------
HTTPException
    If the I/O type with the specified ID is not found.

<h3 id="get_type_schema_io__io_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|io_id|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_type_schema_io__io_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_type_schema_io__io_id__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="easyapi-algorithm-entries">Algorithm Entries</h1>

## get_entry_list_entries__get

<a id="opIdget_entry_list_entries__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /entries/ \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /entries/ HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/entries/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/entries/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/entries/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/entries/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/entries/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/entries/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /entries/`

*Get Entry List*

Retrieves a list of algorithm entries with optional pagination.

Parameters:
----------
skip : int
    The number of entries to skip (for pagination).
limit : int
    The maximum number of entries to return (for pagination).
name : bool
    If true, return only the name of each entry.
auth_id : str
    The ID of the user making the request, used for authorization.
    
Returns:
-------
dict
    A dictionary containing the total number of entries, skip, limit, and the records (list of entries).
    
Raises:
------
HTTPException
    If the skip value exceeds the total number of entries, or if other errors occur.

<h3 id="get_entry_list_entries__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|skip|query|integer|false|none|
|limit|query|integer|false|none|
|name|query|boolean|false|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_entry_list_entries__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_entry_list_entries__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## submit_task_entries__entry_name__post

<a id="opIdsubmit_task_entries__entry_name__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /entries/{entry_name} \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
POST /entries/{entry_name} HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/entries/{entry_name}',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.post '/entries/{entry_name}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.post('/entries/{entry_name}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/entries/{entry_name}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/entries/{entry_name}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/entries/{entry_name}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /entries/{entry_name}`

*Submit Task*

Submits a task for execution on the specified algorithm entry.

Parameters:
----------
entry_name : str
    The name of the algorithm entry for which to submit a task.
request : Request
    The request object, used to extract the task parameters.
auth_id : str
    The ID of the user submitting the task.

Returns:
-------
dict
    A dictionary containing the task ID and creation time.

Raises:
------
HTTPException
    If the task parameters cannot be parsed, or if other errors occur.

<h3 id="submit_task_entries__entry_name__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entry_name|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="submit_task_entries__entry_name__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="submit_task_entries__entry_name__post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_entry_doc_entries__entry_name__get

<a id="opIdget_entry_doc_entries__entry_name__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /entries/{entry_name} \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /entries/{entry_name} HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/entries/{entry_name}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/entries/{entry_name}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/entries/{entry_name}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/entries/{entry_name}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/entries/{entry_name}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/entries/{entry_name}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /entries/{entry_name}`

*Get Entry Doc*

Retrieves detailed documentation for an algorithm entry, including inputs and outputs.

Parameters:
----------
entry_name : str
    The name of the algorithm entry.
io : bool
    If true, includes input and output parameter details.
auth_id : str
    The ID of the user requesting the documentation.

Returns:
-------
dict
    A dictionary containing the entry details, including inputs and outputs if requested.

<h3 id="get_entry_doc_entries__entry_name__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entry_name|path|any|true|none|
|io|query|boolean|false|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_entry_doc_entries__entry_name__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_entry_doc_entries__entry_name__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_entry_name_entries__entry_name__name_get

<a id="opIdget_entry_name_entries__entry_name__name_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /entries/{entry_name}/name \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /entries/{entry_name}/name HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/entries/{entry_name}/name',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/entries/{entry_name}/name',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/entries/{entry_name}/name', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/entries/{entry_name}/name', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/entries/{entry_name}/name");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/entries/{entry_name}/name", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /entries/{entry_name}/name`

*Get Entry Name*

Retrieves the name of the specified algorithm entry.

Parameters:
----------
entry_name : str
    The name of the algorithm entry.
auth_id : str
    The ID of the user requesting the entry name.

Returns:
-------
str
    The name of the algorithm entry.

<h3 id="get_entry_name_entries__entry_name__name_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entry_name|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_entry_name_entries__entry_name__name_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_entry_name_entries__entry_name__name_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_entry_version_entries__entry_name__version_get

<a id="opIdget_entry_version_entries__entry_name__version_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /entries/{entry_name}/version \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /entries/{entry_name}/version HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/entries/{entry_name}/version',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/entries/{entry_name}/version',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/entries/{entry_name}/version', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/entries/{entry_name}/version', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/entries/{entry_name}/version");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/entries/{entry_name}/version", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /entries/{entry_name}/version`

*Get Entry Version*

Retrieves the version of the specified algorithm entry.

Parameters:
----------
entry_name : str
    The name of the algorithm entry.
auth_id : str
    The ID of the user requesting the entry version.

Returns:
-------
str
    The version of the algorithm entry.

<h3 id="get_entry_version_entries__entry_name__version_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entry_name|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_entry_version_entries__entry_name__version_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_entry_version_entries__entry_name__version_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_entry_description_entries__entry_name__desc_get

<a id="opIdget_entry_description_entries__entry_name__desc_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /entries/{entry_name}/desc \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /entries/{entry_name}/desc HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/entries/{entry_name}/desc',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/entries/{entry_name}/desc',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/entries/{entry_name}/desc', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/entries/{entry_name}/desc', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/entries/{entry_name}/desc");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/entries/{entry_name}/desc", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /entries/{entry_name}/desc`

*Get Entry Description*

Retrieves the description of the specified algorithm entry.

Parameters:
----------
entry_name : str
    The name of the algorithm entry.
auth_id : str
    The ID of the user requesting the entry description.

Returns:
-------
str
    The description of the algorithm entry.

<h3 id="get_entry_description_entries__entry_name__desc_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entry_name|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_entry_description_entries__entry_name__desc_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_entry_description_entries__entry_name__desc_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_entry_references_entries__entry_name__ref_get

<a id="opIdget_entry_references_entries__entry_name__ref_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /entries/{entry_name}/ref \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /entries/{entry_name}/ref HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/entries/{entry_name}/ref',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/entries/{entry_name}/ref',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/entries/{entry_name}/ref', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/entries/{entry_name}/ref', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/entries/{entry_name}/ref");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/entries/{entry_name}/ref", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /entries/{entry_name}/ref`

*Get Entry References*

Retrieves the references for the specified algorithm entry.

Parameters:
----------
entry_name : str
    The name of the algorithm entry.
auth_id : str
    The ID of the user requesting the entry references.

Returns:
-------
str
    The references of the algorithm entry.

<h3 id="get_entry_references_entries__entry_name__ref_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entry_name|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_entry_references_entries__entry_name__ref_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_entry_references_entries__entry_name__ref_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_entry_input_schema_entries__entry_name__in_get

<a id="opIdget_entry_input_schema_entries__entry_name__in_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /entries/{entry_name}/in \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /entries/{entry_name}/in HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/entries/{entry_name}/in',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/entries/{entry_name}/in',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/entries/{entry_name}/in', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/entries/{entry_name}/in', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/entries/{entry_name}/in");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/entries/{entry_name}/in", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /entries/{entry_name}/in`

*Get Entry Input Schema*

Retrieves the input schema for the specified algorithm entry.

Parameters:
----------
entry_name : str
    The name of the algorithm entry.
auth_id : str
    The ID of the user requesting the entry input schema.

Returns:
-------
dict
    A dictionary of input parameters for the algorithm entry.

<h3 id="get_entry_input_schema_entries__entry_name__in_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entry_name|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_entry_input_schema_entries__entry_name__in_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_entry_input_schema_entries__entry_name__in_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_entry_output_schema_entries__entry_name__out_get

<a id="opIdget_entry_output_schema_entries__entry_name__out_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /entries/{entry_name}/out \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /entries/{entry_name}/out HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/entries/{entry_name}/out',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/entries/{entry_name}/out',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/entries/{entry_name}/out', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/entries/{entry_name}/out', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/entries/{entry_name}/out");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/entries/{entry_name}/out", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /entries/{entry_name}/out`

*Get Entry Output Schema*

Retrieves the output schema for the specified algorithm entry.

Parameters:
----------
entry_name : str
    The name of the algorithm entry.
auth_id : str
    The ID of the user requesting the entry output schema.

Returns:
-------
dict
    A dictionary of output parameters for the algorithm entry.

<h3 id="get_entry_output_schema_entries__entry_name__out_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|entry_name|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_entry_output_schema_entries__entry_name__out_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_entry_output_schema_entries__entry_name__out_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="easyapi-task-management">Task Management</h1>

## get_task_tasks__task_id__get

<a id="opIdget_task_tasks__task_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /tasks/{task_id} \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET /tasks/{task_id} HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/tasks/{task_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/tasks/{task_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/tasks/{task_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/tasks/{task_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/tasks/{task_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/tasks/{task_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /tasks/{task_id}`

*Get Task*

Retrieves and returns the status of a specific task.

Parameters:
----------
task_id : str
    The ID of the task to retrieve.
auth_id : str
    The ID of the user making the request, used for authorization.
    
Returns:
-------
dict
    A dictionary containing the task's status and related information.

Raises:
------
HTTPException
    If the task is not found or if the user is not authorized to view the task.

<h3 id="get_task_tasks__task_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|task_id|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_task_tasks__task_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_task_tasks__task_id__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## cancel_task_tasks__task_id__cancel_post

<a id="opIdcancel_task_tasks__task_id__cancel_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /tasks/{task_id}/cancel \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
POST /tasks/{task_id}/cancel HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/tasks/{task_id}/cancel',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.post '/tasks/{task_id}/cancel',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.post('/tasks/{task_id}/cancel', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/tasks/{task_id}/cancel', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/tasks/{task_id}/cancel");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/tasks/{task_id}/cancel", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /tasks/{task_id}/cancel`

*Cancel Task*

Cancels a task and removes it from the task queue.

Parameters:
----------
task_id : str
    The ID of the task to cancel.
auth_id : str
    The ID of the user making the request, used for authorization.

Returns:
-------
dict
    A dictionary containing the task ID and a success flag.

Raises:
------
HTTPException
    If the task is not found or if the user is not authorized to cancel the task.

<h3 id="cancel_task_tasks__task_id__cancel_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|task_id|path|any|true|none|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="cancel_task_tasks__task_id__cancel_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="cancel_task_tasks__task_id__cancel_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="easyapi-server-information">Server Information</h1>

## root__get

<a id="opIdroot__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET / \
  -H 'Accept: application/json' \
  -H 'easyapi-id: ' \
  -H 'easyapi-key: '

```

```http
GET / HTTP/1.1

Accept: application/json
easyapi-id: 
easyapi-key: 

```

```javascript

const headers = {
  'Accept':'application/json',
  'easyapi-id':'',
  'easyapi-key':''
};

fetch('/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'easyapi-id' => '',
  'easyapi-key' => ''
}

result = RestClient.get '/',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'easyapi-id': '',
  'easyapi-key': ''
}

r = requests.get('/', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'easyapi-id' => '',
    'easyapi-key' => '',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "easyapi-id": []string{""},
        "easyapi-key": []string{""},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /`

*Root*

Root endpoint that returns the server's name and the authenticated user's ID.

Parameters:
----------
auth_id : str
    The authenticated user's ID, retrieved via URL-based authentication.
    
Returns:
-------
dict
    A dictionary containing the server name and the authenticated user's ID.

<h3 id="root__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|easyapi-id|header|any|false|none|
|easyapi-key|header|any|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="root__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="root__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

