import redis

def main():
# указываем параметры, которые необходимы для подключения
    host = 'c-c9qouu38glg6oa5asodd.rw.mdb.yandexcloud.net'
    port = 6380
    password = 'mustdayker_redis_password'
    ca_path = 'c:/GitHub/data_engineer/09_yandex_cloud/cert/.redis/YandexInternalRootCA.crt'

# инициализируем клиент, с помощью которого будем подключаться к Redis
    client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            ssl=True,
            ssl_ca_certs=ca_path)

# просто подключиться недостаточно, да и неинтересно: нужно же ещё и поработать с хранилищем

# запишем в Redis ключ here_is_the_key и соответствующее ему строковое значение string value
    client.set("here_is_the_key", "string value")

# получим значение ключа с помощью команды get
    result = client.get("here_is_the_key")
    if not result:
        print("Запись с указанным ключом не найдена.")
        return

    result = result.decode("utf-8")
    print(result)

if __name__ == '__main__':
    main()