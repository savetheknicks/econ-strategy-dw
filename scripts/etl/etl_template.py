from abc import ABC, abstractmethod
import pandas as pd
import requests

class ETLTemplate(ABC):
    
    def run(self):
        data = self.extract()
        self.load(data)
        
    @abstractmethod
    def extract(self) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def load(self, data: pd.DataFrame):
        pass
    
    
class ApiETL(ETLTemplate):
    
    def __init__(self, url: str, api_key: str = None):
        super().__init__()
        self.url = url
        self.api_key = api_key
        self.api_client = requests
    
    
    
    
        