# app/dependencies/__init__.py
from .k8s import get_k8s_client
from .database import get_db

__all__ = ["get_k8s_client", "get_db"]