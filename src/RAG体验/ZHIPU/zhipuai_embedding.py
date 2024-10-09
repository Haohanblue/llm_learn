from __future__ import annotations

import logging
from typing import Dict, List, Any
from langchain.embeddings.base import Embeddings
from pydantic import BaseModel, model_validator  # 使用 model_validator 替代 root_validator

logger = logging.getLogger(__name__)

class ZhipuAIEmbeddings(BaseModel, Embeddings):
    """Zhipuai Embeddings embedding models."""

    client: Any = None  # 默认值为 None，避免未初始化的问题

    @model_validator(mode="after")
    def validate_environment(cls, values: Dict) -> Dict:
        """
        实例化ZhipuAI为values["client"]，如果client为空.
        """
        if values.client is None:
            try:
                from zhipuai import ZhipuAI
                values.client = ZhipuAI()
            except ImportError:
                raise ModuleNotFoundError("No module named 'zhipuai'. Please install zhipuai to use this feature.")
        return values

    def embed_query(self, text: str) -> List[float]:
        """
        生成输入文本的 embedding.
        """
        try:
            embeddings = self.client.embeddings.create(
                model="embedding-3",
                input=text
            )
            return embeddings.data[0].embedding
        except Exception as e:
            logger.error(f"Failed to generate embeddings: {e}")
            raise ValueError(f"Error while generating embedding: {e}")

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        生成输入文本列表的 embedding.
        """
        print([self.embed_query(text) for text in texts]) 
        return [self.embed_query(text) for text in texts]

    async def aembed_documents(self, texts: List[str]) -> List[List[float]]:
        """Asynchronous Embed search docs (not supported)."""
        raise NotImplementedError("Please use `embed_documents`. Official does not support asynchronous requests.")

    async def aembed_query(self, text: str) -> List[float]:
        """Asynchronous Embed query text (not supported)."""
        raise NotImplementedError("Please use `embed_query`. Official does not support asynchronous requests.")
