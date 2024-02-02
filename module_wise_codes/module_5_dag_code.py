'''
You can add Params to a DAG by initializing it with the params keyword argument. Use a dictionary that maps Param names to either a Param or an object indicating the parameter's default value. For example:

from airflow import DAG
from airflow.models.param import Param

with DAG(
	"the_dag",
	params={
		"value": Param(5, type="integer", minimum=3),
		"my_int_param": 6
	},
):
'''

from airflow import DAG
from airflow.models.param import Param
from airflow.operators.python_operator import PythonOperator

with DAG(
	"the_dag",
	params={
		"value": Param(5, type="integer", minimum=3)
	}
):

	def print_my_int_param(**kwargs):
		value = kwargs['params']['value']
		print(f"Selected Value: {value}")

	param_task = PythonOperator(
		task_id="print_my_int_param",
		python_callable=print_my_int_param,
		provide_context=True
	)

	param_task
