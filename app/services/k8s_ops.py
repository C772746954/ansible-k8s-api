from kubernetes import client, config
from kubernetes.client.rest import ApiException
from typing import Dict, List


class K8SOperator:
    def __init__(self, kubeconfig_path: str):
        self.api_client = config.new_client_from_config(kubeconfig_path)

    def list_configmaps(self, namespace: str = "default") -> List[Dict]:
        v1 = client.CoreV1Api(self.api_client)
        try:
            return v1.list_namespaced_config_map(namespace).to_dict()["items"]
        except ApiException as e:
            raise self._handle_api_exception(e)

    def create_configmap(self, name: str, data: Dict, namespace: str = "default") -> Dict:
        v1 = client.CoreV1Api(self.api_client)
        body = client.V1ConfigMap(
            metadata={"name": name},
            data=data
        )
        try:
            return v1.create_namespaced_config_map(namespace, body).to_dict()
        except ApiException as e:
            raise self._handle_api_exception(e)

    def delete_configmap(self, name: str, namespace: str = "default") -> Dict:
        v1 = client.CoreV1Api(self.api_client)
        try:
            return v1.delete_namespaced_config_map(name, namespace).to_dict()
        except ApiException as e:
            raise self._handle_api_exception(e)

    # 类似实现Deployment/Secret/Service的操作方法...

    @staticmethod
    def _handle_api_exception(e: ApiException) -> Exception:
        error_msg = f"K8S API Error ({e.status}): {e.reason}"
        if e.body:
            error_details = json.loads(e.body)
            error_msg += f" - {error_details.get('message')}"
        return HTTPException(status_code=e.status, detail=error_msg)