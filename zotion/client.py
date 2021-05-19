import httpx

from addict import Dict


class Notion:

    api = 'https://api.notion.com/v1/'
    headers = dict()

    def __init__(self, internal_integration_token):
        self.client = httpx.Client()
        self.headers.update({
            'Authorization': f'Bearer {internal_integration_token}',
        })

    def retrieve_database(self, database_id):
        response = self.client.get(
            f'{self.api}databases/{database_id}',
            headers=self.headers
        )
        return Dict(response.json())
