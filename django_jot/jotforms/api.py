from django.conf import settings

import requests


class JotformDataAPI(object):
    def get_user(self):
        jotform_api_key = settings.JOTFORMS_API_KEY
        url = f'https://api.jotform.com/user?apiKey={jotform_api_key}'
        response = requests.get(url)
        return response.json()

    def get_all_form(self): 
        jotform_api_key = settings.JOTFORMS_API_KEY

        headers = {
            'APIKEY': jotform_api_key,
        }
        url = f'https://api.jotform.com/user/forms'

        response = requests.get(url, headers=headers)
        return response.json()

    def get_submission_data_from_form(self):
        jotform_api_key = settings.JOTFORMS_API_KEY
        formID = '81992524911462'
        url = f'https://api.jotform.com/form/{formID}/submissions?apiKey={jotform_api_key}'
        response = requests.get(url)
        return response.json()

    
        

