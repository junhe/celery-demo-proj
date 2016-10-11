startworker:
	celery -A celeryapp worker -l info

pushtasks:
	python ./taskspusher.py
