# Example: Mapping Over a List

# To illustrate Dynamic Task Mapping, envision a scenario where you have a task, Task A, responsible for processing a list of marks that includes both numerical values and ‘N/A’ entries, ultimately generating an output. In this scenario, the objective is to automate the creation of multiple Task B instances, each tasked with performing additional operations on individual numerical values extracted from the output of Task A.

# Code Example
'''
	from airflow import DAG
	from airflow.decorators import task
	from datetime import datetime

	# Define a simple DAG
	# with DAG(dag_id='example_dynamic_task_mapping', start_date=datetime(2022, 3, 4)) as dag:
	with DAG(dag_id="example_dynamic_task_mapping_v1", start_date=datetime(2023, 5, 1), schedule=None, catchup=False) as dag:

		@task
		def apply_filter(mark):
			return mark if isinstance(mark, int) else None
		
		@task
		def calculate_percentage(marks):
			print(marks)
			print(sum(marks) / (len(marks)))
		
		filtered_values = apply_filter.expand(mark=[68, 96, 67, None, 'N/A', 88, 'N/A'])
		calculate_percentage(filtered_values)
'''	
# Execution and Results
# When executed, this DAG will create tasks ‘apply_filter’ for each input value from the given list mark = [68, 96, 67, None, ‘N/A’, 88, ‘N/A’]. Each task checks if the input is an integer; if it is, the task returns the integer value; otherwise, it returns None.

# Afterward, the ‘calculate_percentage’ task computes and displays the percentage grade for the provided marks. percentage grade for given marks.