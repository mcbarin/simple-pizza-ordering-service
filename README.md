# Simple Pizza Order Service

Main purpose of this project is to create an API for a simple pizza order service.


## Prerequisites
- docker
- docker-compose

## Build and Run
```bash
docker-compose up --build
```

Navigate to this using browser:
[http://localhost:8000/api/](http://localhost:8000/api/)


## Run Tests
While container is running, run this command in another terminal.
```
docker-compose exec backend sh -c "python manage.py test"
```

## Versions

```bash
$ docker -v
Docker version 19.03.6, build 369ce74a3c
```
```bash
$ docker-compose version
docker-compose version 1.26.2, build unknown
docker-py version: 4.2.2
CPython version: 3.6.11
OpenSSL version: OpenSSL 1.1.1f  31 Mar 2020
```

## Notes

* A customer object and couple of Flavor objects are pre-populated using data migrations.
* Customer model is kept simple which only contains name and surname (If authentication is needed, then it'd be implemented by extending Django's built-in User object using AbstractUser)
* For the nested writing of the model objects, `drf-writable-nested` package is used for the simplicity. It'd also be implemented by overriding the serializer's `save` and `update` methods.
* Example order create data,
```
{
    "information": "Please come fast, thank you!",
    "customer": 1,
    "pizzas": [{"size": 1, "flavors": [1,2], "count": 1}]
}
```
