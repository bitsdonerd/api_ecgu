import requests
import pandas as pd 
from datetime import date 
from itertools import chain 
from task_map import json_final

class Requests:
    def __init__(self):
        self.chave_api = '529f6149ed146ecde0ed5592e1eea2e3'
        self.base_url = 'https://eaud.cgu.gov.br/api/auth/tarefa/gantt/{id}/dto/json'
        self.headers = {'chave-api':self.chave_api,'Accept-Enconding':'gzip,deflate'}
        self.task = json_final
        self.df = None
        self.id = None

    