# 构建Celery镜像
docker build -f Dockerfile.celery -t k8s-celery-worker:1.0 .

# 查看Worker状态
docker exec -it <container_id> celery -A app.celery.tasks status

# 监控任务队列
docker exec -it <container_id> celery -A app.celery.tasks inspect active