# app/routers/configmaps.py
from fastapi import APIRouter, Depends
from app.dependencies.k8s import get_k8s_client  # 修正导入路径

router = APIRouter(prefix="/clusters/{cluster_name}/configmaps", tags=["ConfigMaps"])

@router.post("/")
async def create_configmap(
    cluster_name: str,
    k8s_client=Depends(get_k8s_client)  # 依赖注入
):
    # 示例：调用 Kubernetes API
    return {"message": f"ConfigMap created in cluster {cluster_name}"}