import logging

import azure.functions as func
from __app__.modules.library_finder import find_libraries

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        req_body = req.get_json()
        logging.info(f'Request body: {req_body}')
    except:
        return func.HttpResponse('Failed to load json request')
    try:
        text = req_body.get('text').lower()

        if 'libraries' in text:
            city = text.replace('libraries','')
            library_df = find_libraries(city.strip())
            return func.HttpResponse(f'```   \n {library_df.to_string()}')
        else:
            return func.HttpResponse(
                "Please pass a valid command in the request text"
            )
    except:
        return func.HttpResponse('Json in request was not in the correct format')