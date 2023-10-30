import json
import time
from confluent_kafka import Consumer


def error_callback(err):
    print('Something went wrong: {}'.format(err))


def main():
# Установка параметров консьюмера
    host = 'rc1a-4fb44c03lgap7fli.mdb.yandexcloud.net'
    port = 9091
    user = 'producer_consumer'
    password = 'mustdayker_kafka_password'
    cert_path = 'c:/GitHub/data_engineer/09_yandex_cloud/cert/.kafka/CA.pem'
    group = 'main-consumer-group'

    params = {
        'bootstrap.servers': f'{host}:{port}',
        'security.protocol': 'SASL_SSL',
        'ssl.ca.location': cert_path,
        'sasl.mechanism': 'SCRAM-SHA-512',
        'sasl.username': user,
        'sasl.password': password,
        'group.id': group,
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False,
        'error_cb': error_callback,
        'debug': 'all',
        'client.id': 'someclientkey'
    }

# Инициализация консьюмера
    consumer = Consumer(params)

# Подписка консьюмера на топик Kafka
    topic = 'order-service_orders'
    consumer.subscribe([topic])




# Запуск бесконечного цикла
    while True:
        msg = consumer.poll(timeout=3.0)
        if msg:
            val = msg.value().decode()
            print(val)
        
        

if __name__ == '__main__':
    main() 