# TaskFlow Api
## Templating
- templated params are defined in the Operator template_fields, template_ext
- for Python Operator they are: templates_dict, op_args and op_kwargs
- for PostgresOperator they are sql and the .sq extenson
- syntax: param: '{{ templated_param}}' or param: 'path/to_file.ext'

## XCOMS
- share data between tasks
- push XCOM -> store in metadata database -> pull XCOM
- ti.xcom_push(key="partner_name", value=partner_name)
    - OR just return in