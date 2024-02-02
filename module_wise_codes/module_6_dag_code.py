# Managing Variables in Airflow:
# 1. Variable Class:
# The Variable class in Apache Airflow is used to store and retrieve key-value pairs. It's a convenient way to manage configuration values and share data across tasks.
'''
from airflow.models import Variable
'''	
# 2. Setting and Getting Variables:
# Use Variable.set to set a variable, and Variable.get to retrieve its value.
# Set a variable
'''
Variable.set("my_variable", "my_value")
'''
# Retrieve a variable
'''
my_value = Variable.get("my_variable")
'''	
# 3. Storing JSON Data:
# Variables can store more complex data structures, such as JSON.

# Set a JSON variable
'''
json_data = {'key': 'value'}
Variable.set("my_json_variable", json.dumps(json_data))
'''

# Retrieve and parse the JSON variable
'''
retrieved_json = json.loads(Variable.get("my_json_variable"))
'''
# Communicating Between Tasks Using XCom:
# 1. XComs (Cross-Communication):
# XComs are a mechanism for tasks to exchange small amounts of metadata during the execution of a DAG. Tasks can push key-value pairs to XComs, and other tasks can retrieve this information.
'''
from airflow.operators.python_operator import PythonOperator
'''
# 2. Pushing XComs:
# Use the push method to push data to XComs within a task.
'''
def push_xcom_data(**kwargs):
    xcom_data = {'key': 'value'}
    kwargs['ti'].xcom_push(key='my_xcom_key', value=xcom_data)

push_xcom_task = PythonOperator(
    task_id='push_xcom_task',
    python_callable=push_xcom_data,
    provide_context=True,
    dag=dag,
)
'''

# 3. Pulling XComs:
# Use the xcom_pull method to retrieve data from XComs within another task.

'''
def pull_xcom_data(**kwargs):
    ti = kwargs['ti']
    xcom_data = ti.xcom_pull(task_ids='push_xcom_task', key='my_xcom_key')
    print(xcom_data)

pull_xcom_task = PythonOperator(
    task_id='pull_xcom_task',
    python_callable=pull_xcom_data,
    provide_context=True,
    dag=dag,
)
'''