<img src="/images/tulane_long.png" width="128px"><img src="/images/icon_apl.png" width="256px"><img src="/images/icon_long.png" width="128px"> 

# EasyAPI Framework Design

`UPDATED: 2024/10/12, JIARUI LI`

## Service Logic Flow

```mermaid
flowchart TB;

start((start))--credentials-->Authenticator;
subgraph Auth
    direction TB;
    Authenticator--credentials-->File_Authenticator;
    Authenticator--credentials-->Remote_Authenticator;
    Authenticator--credentials-->Memory_Authenticator;
    Authenticator_end{Authentication};
    File_Authenticator--auth_status-->Authenticator_end;
    Remote_Authenticator--auth_status-->Authenticator_end;
    Memory_Authenticator--auth_status-->Authenticator_end;
    Authenticator_end--fail-->End_auth_fail(((Auth-Fail)));
end

Authenticator_end--succ-->Authenticated((Authenticated));
Authenticated-->Entry;
subgraph Entry
    direction LR;
    subgraph Algorithm
        direction LR;
        alg_t1{{Get Entry List}}-->Get_alg[GET /entries]-->list_entries[List of Entries];
        alg_t5{{Get Entry Info}}-->Get_alg_name[GET /entries/name]-->entry_info[Entry Introduction];
        alg_t6{{Get Entry I/O}}-->Get_alg_io[GET /entries/io]-->entry_io[I/O Ref. to DataType];
    end
    subgraph Task
        direction LR;
        alg_t2{{Submit Task}}-->Post_entry[POST /entries/name]-->task_id;
        alg_t3{{Fetch Result / Progress}}-->get_task_entry[GET /task_id]--finished-->result;
        get_task_entry--in_progress-->progress;
        alg_t4{{Cancel Task}}-->delete_task_entry[POST /task_id/cancel]-->Succ;
    end
    subgraph IO
        direction LR;
        alg_t7{{Get I/O Info}}-->Get_io[GET /io/io_id]-->entry_io_id[I/O Info];
        alg_t8{{Get I/O List}}-->Get_io_list[GET /io]-->entry_io_list[I/O List];
    end
end
Entry-->End(((End)))
```

## Entity Relationship
```mermaid
erDiagram
    Authentication {
        string easyapi_id
        string easyapi_key
        list avaliable_entries
    }

    Task {
        string task_id
        string algorithm_id
        string easyapi_id
        datetime create_time
        datetime start_time
        datetime done_time
        boolean in_progress
        boolean finished
        object input_data
        object output_data
        object algorithm_module
        list resource
    }

    Algorithm {
        string algorithm_id
        string algorithm_name
        string algorithm_description
        string version
        list reference
        list input_typeid
        list output_typeid
        object module
    }

    DataType {
        string datatype_id
        string datatype_name
        string description
        datetime create_time
        string meta_types
        string data_regular_expression
    }

    Authentication ||--o{ Task : easyapi_id
    Algorithm ||--o{ Task : algorithm_id
    DataType }o--o{ Algorithm : datatype_id
```

## API Entries
|Module   |Entry URI   |Method   |Description|
|:--------|:-----------|:--------|:----------|
|Algorithm|`/entries`  |`GET`    |Get the list of all accessible algorithms|
|Algorithm|`/entries/{entry}`  |`GET`    |Get the description of the `entry`|
|Algorithm|`/entries/{entry}/name`  |`GET`    |Get the name of the `entry`|
|Algorithm|`/entries/{entry}/version`  |`GET`    |Get the version of the `entry`|
|I/O|`/entries/{entry}/io`  |`GET`    |Get the I/O data type reference ID of the `entry`|
|I/O|`/types/{io_id}`  |`GET`    |Get the I/O type description by `io_id`|
|I/O|`/types/{io_id}/name`  |`GET`    |Get the I/O type name by `io_id`|
|Task|`/entries/{entry}`  |`POST`    |Create the task submitted to `entry`|
|Task|`/task/{task_id}/cancel`  |`POST`    |Cancel the task `task_id`|
|Task|`/task/{task_id}`  |`GET`    |Get the task `task_id` progress or results|