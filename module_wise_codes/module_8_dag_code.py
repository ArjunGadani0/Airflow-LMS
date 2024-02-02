# ExternalTaskSensor Example:
# Let's consider the ExternalTaskSensor as an example. This sensor waits for the completion of an external task before allowing the workflow to continue.

'''
    external_task_sensor = ExternalTaskSensor(
        task_id='external_task_sensor',
        external_dag_id='external_dag_id',
        external_task_id='external_task_id',
        timeout=600,  # Maximum time to wait (in seconds)
        poke_interval=60,  # Time in seconds that the job should wait in between each try
        mode='reschedule',  # Other modes: 'poke' and 'reschedule'
        dag=dag,
    )
'''

# This sensor will poke (checks) every 60 seconds to check provided external DAG run is completed or not till 600 seconds / 10 minutes, once exteranl DAG run is completed it will move further with upcoming tasks.
