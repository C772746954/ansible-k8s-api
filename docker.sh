# 构建镜像
docker build -t k8s-operator-api:1.0 .

# 查看镜像大小
docker images | grep k8s-operator-api

# 预期输出（经过优化后）：
# k8s-operator-api   1.0    180MB