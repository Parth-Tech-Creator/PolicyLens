import os
from typing import Any, Dict, List, Optional

try:
    from pymongo import MongoClient
except Exception:  # pragma: no cover - optional dependency
    MongoClient = None  # type: ignore


class MongoClientWrapper:
    """
    Lightweight wrapper around pymongo for the prototype.
    If MONGO_URI is not set or pymongo is unavailable, all operations are no-ops.
    """

    def __init__(self, uri_env: str = "MONGO_URI", db_name: str = "policy_ai"):
        self._client = None
        self._db = None

        uri = os.getenv(uri_env)
        if uri and MongoClient is not None:
            try:
                self._client = MongoClient(uri)
                self._db = self._client[db_name]
            except Exception:
                self._client = None
                self._db = None

    @property
    def enabled(self) -> bool:
        return self._db is not None

    def store_document(
        self,
        filename: str,
        summary: str,
        chunks: List[str],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        if not self.enabled:
            return
        doc = {
            "filename": filename,
            "summary": summary,
            "chunks": chunks,
            "metadata": metadata or {},
        }
        try:
            self._db.documents.insert_one(doc)
        except Exception:
            # Fail silently in prototype
            pass

    def log_query(
        self,
        filename: str,
        question: str,
        answer: str,
        sources: List[str],
    ) -> None:
        if not self.enabled:
            return
        entry = {
            "filename": filename,
            "question": question,
            "answer": answer,
            "sources": sources,
        }
        try:
            self._db.query_logs.insert_one(entry)
        except Exception:
            pass

