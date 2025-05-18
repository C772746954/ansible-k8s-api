import secrets

# 生成 32 字节的随机字符串（可通过调整长度适应需求）
secret_key = secrets.token_urlsafe(32)
print(secret_key)