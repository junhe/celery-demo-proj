# celery-demo-proj

#### Install requirements

```
sudo apt-get install -y rabbitmq-server
sudo pip install celery
```

#### Run worker

```
make startworker
```

#### Run task pusher in another terminate of the same node

```
make pushtasks
```


