import redis

r = redis.StrictRedis(
    host="c-c9q3qaothd9jum1o9cgt.rw.mdb.yandexcloud.net",
    port=6380,
    password="mustdayker_redis_password",
    ssl=True,
    ssl_ca_certs="c:/Users/mustd/.redis/YandexInternalRootCA.crt",
)

r.set("foo", "bar")
print(r.get("foo"))