from typing import Dict
from abc import ABC, abstractmethod


class DatabaseRepositoryInterface(ABC):
    """Responsible for implementing queries in the database"""

    @classmethod
    @abstractmethod
    def insert_artist(cls, data: Dict) -> None:
        """Inserts artist information into the database"""
