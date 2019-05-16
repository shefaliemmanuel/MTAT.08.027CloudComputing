#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
import sys
from datetime import datetime
from cloudant.client import Cloudant


def getDBdoc(doc_id, username, apikey):
    databaseName = "labdb1"
    client = Cloudant.iam(username, apikey, connect=True)
    myDatabase = client[databaseName]
    db_doc = myDatabase[doc_id]
    return db_doc


def main(param):
    doc = getDBdoc(param['id'], param['username'], param['apikey'])
    mess = doc['message']
    splitM = mess.split()
    if 'word_count' in doc:
        return doc
    doc['word_count'] = len(splitM)
    doc['letters_in_words'] = len(mess) - mess.count(' ')
    doc.save()
    return doc



