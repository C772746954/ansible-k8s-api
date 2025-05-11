# 使用多阶段构建优化镜像大小
# ========== 构建阶段 ==========
FROM python:3.9-slim as builder

# 安装编译依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# 创建虚拟环境
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 先安装需要编译的包
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ========== 运行时阶段 ==========
FROM python:3.9-slim

# 安装运行时依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    openssh-client \
    git \
    && rm -rf /var/lib/apt/lists/*

# 从构建阶段复制虚拟环境
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 创建非root用户
RUN useradd -m -u 1001 appuser && \
    mkdir -p /app/ansible && \
    chown -R appuser:appuser /app
USER appuser
WORKDIR /app

# 安装Ansible集合
RUN ansible-galaxy collection install kubernetes.core:==2.4.0

# 复制应用代码（保持最后以利用缓存）
COPY --chown=appuser:appuser ./app ./app
COPY --chown=appuser:appuser ./ansible ./ansible

# 健康检查
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 服务端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]