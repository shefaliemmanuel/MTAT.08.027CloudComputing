#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
import sys
from cloudant.client import Cloudant


def addDocToDB(new_doc, username, apikey):
    databaseName = "labdb1"
    client = Cloudant.iam(username, apikey, connect=True)
    myDatabase = client[databaseName]
    return myDatabase.create_document(new_doc)


def main(param):
    user = ""
    if 'user' in param:
        user = param['user']

    message = ""
    if 'message' in param:
        message = param['message']

    doc = {'message': message, 'user': user}

    modified_doc = addDocToDB(doc, param['username'], param['apikey'])

    return modified_doc
