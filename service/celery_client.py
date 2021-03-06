import os

from celery import Celery

broker_host = os.environ['BROKER_HOST']
broker_user = os.environ['BROKER_USER']
broker_password = os.environ['BROKER_PASSWORD']
broker_vhost = os.environ['BROKER_VHOST']

broker_config = 'amqp://' + broker_user + ':' + broker_password + '@' + broker_host + '/' + broker_vhost
result_config = 'rpc://'

celery = Celery('nlp_service', broker=broker_config, backend=result_config)
