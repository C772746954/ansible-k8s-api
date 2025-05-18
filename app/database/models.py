from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base  # 关键导入

# 创建声明基类
Base = declarative_base()  # 必须在所有模型类之前定义


class User(Base):
    """用户模型"""
    __tablename__ = "users"

    username = Column(String(50), primary_key=True, index=True)
    hashed_password = Column(String(256), nullable=False)


class Cluster(Base):
    """集群模型"""
    __tablename__ = "clusters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    kubeconfig = Column(Text, nullable=False)

    labels = relationship("ClusterLabel", back_populates="cluster")


class ClusterLabel(Base):
    """集群标签模型"""
    __tablename__ = "cluster_labels"

    id = Column(Integer, primary_key=True, index=True)
    cluster_id = Column(Integer, ForeignKey("clusters.id"), nullable=False)
    label_key = Column(String(50), nullable=False)
    label_value = Column(String(100), nullable=False)

    cluster = relationship("Cluster", back_populates="labels")