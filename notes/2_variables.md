# Variables
Create in Airflow UI - Admin - Variables /variable/add

```python
from airflow.models import Variable

Variable.get("my_variable") # this is read very often
```

- key, val, description
    - prefix key with dag name to know where is used

- will create a connection to the metadata database
- Use some keywords to hide important keys -> using password, passwd, api key, api_key or secret on the variable name will be hide on code
- You can add some keywords in cofiguration settings -> sensitive_var_conn_names

## Properly fetch your variables
- min_file_processing_intervals: will fetch the variable every x seconds
- if you use the Variable.get outside dags or callbacks - they will be read from the metadata database every time the scheduler reads the files
- use JSON values for multiple variables - with only one connection
    - val:{"key1":"value1", "key2":"value2"}
    - my_var = Variable.get("my_variable", deserialize_json=True)
    - my_var['key1']
- fetch in params with templating: op_args=["{{ var.json.my_variable.key1 }}"]


## The Power of Environment Variables
In the Dockerfile: ENV AIRFLOW_VAR_VARIABLE_NAME_1='{"key1":"value1", "key2":"value2"}'

ps. this variables will be hidden from the users and will not connect or be stored in the metadata database

6 ways to create variables:
- Airflow UI
- Airflow CLI
- REST API
- Environment Variables
    - avoid connections to the DB
    - hide sensitive values in the UI
- Secret Backend - local files or custom backends
- Programmatically

The order that Airflows checks for variables: Secrets Backends -> Environment Variable -> DB

Can also create connections like this:
    - AIRFLOW_CONN_NAME_OF_CONNECTION=your_connection