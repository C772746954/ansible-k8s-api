from .configmaps import router as configmaps_router
from .auth import router as auth_router  # 其他路由按需添加

__all__ = ["configmaps_router", "auth_router"]