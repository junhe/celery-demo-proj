from celery import Celery

app = Celery('proj',
             broker='amqp://',
             backend='amqp://',
             # include tasks.py so we can find tasks
             include=['tasks']
             )

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()
