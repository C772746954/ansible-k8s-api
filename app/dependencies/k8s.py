# app/dependencies/k8s.py
from kubernetes import client, config
from fastapi import Depends, HTTPException

def get_k8s_client(cluster_name: str):
    try:
        # 假设 kubeconfig 文件路径为 configs/kubeconfigs/{cluster_name}.yaml
        kubeconfig_path = f"configs/kubeconfigs/{cluster_name}.yaml"
        config.load_kube_config(kubeconfig_path)
        return client.CoreV1Api()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"K8S Client Error: {str(e)}")