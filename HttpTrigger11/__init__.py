import azure.functions as func
import json
import logging

def main(req: func.HttpRequest, inputDocument: func.DocumentList,  outputDocument: func.Out[func.DocumentList]) ->str:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.route_params.get('name')
    for name in inputDocument:
        logging.info(name.to_json())
    if name:
        newdocs = func.DocumentList()
        logging.info('things are getting there, right about func.documentlist is processed')
        visitorname = name.to_json()
        visitor = json.loads(visitorname)
        logging.info('json is loaded')
        key = "visitor"
        if key in visitor:
            visitor[key] +=1
        newdocs_load_json= json.dumps(visitor)
        newdocs.append(func.Document.from_json(newdocs_load_json))
        outputDocument.set(newdocs)
        return func.HttpResponse(f"Hello, new value: {newdocs_load_json} .....")
      