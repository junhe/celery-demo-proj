import tasks
import time

t = tasks.add.delay(2, 3)

print 'ready?', t.ready()
time.sleep(1)
print 'ready?', t.ready()



