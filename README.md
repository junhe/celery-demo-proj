# celery-demo-proj

1. Install requirements

```
sudo apt-get install -y rabbitmq-server
sudo pip install celery
```

2. Run worker

```
make startworker
```

3. Run task pusher in another terminate of the same node

```
make pushtasks
```


