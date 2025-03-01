import redis

def main():
    host = 'c-c9qouu38glg6oa5asodd.rw.mdb.yandexcloud.net'
    port = 6380
    password = 'mustdayker_redis_password'
    ca_path = 'c:/GitHub/data_engineer/09_yandex_cloud/cert/.redis/YandexInternalRootCA.crt'

    client = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            ssl=True,
            ssl_ca_certs=ca_path)


    keys = client.keys('*')
    for key in keys:
        print(key.decode())

    result = client.get("a51e4e31ae4602047ec52534")

    if not result:
        print("Запись с указанным ключом не найдена.")
        return

    result = result.decode("utf-8")
    print(result)



if __name__ == '__main__':
    main()