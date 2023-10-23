import redis

def main():
    host = 'c-c9q3qaothd9jum1o9cgt.rw.mdb.yandexcloud.net'
    port = 6380
    password = 'mustdayker_redis_password'
    ca_path = 'c:/Users/mustd/.redis/YandexInternalRootCA.crt'

    client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            ssl=True,
            ssl_ca_certs=ca_path)

    result = client.get("626a81ce9a8cd1920641e264")
    if not result:
        print("Запись с указанным ключом не найдена.")
        return

    result = result.decode("utf-8")
    print(result)

if __name__ == '__main__':
    main()