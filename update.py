"""
Copyright 2019 Jacques Supcik, HEIA-FR

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import json
import urllib.request

from google.cloud import firestore

API_URL = 'https://lake-level-api.app.supcik.net/v1/data'
COLLECTION_NAME = 'lake'


def main():

    db = firestore.Client()
    with urllib.request.urlopen(API_URL) as url:
        data = json.loads(url.read().decode())

        for k, v in data.items():
            doc_ref = db.collection(COLLECTION_NAME).document(k)
            doc_ref.set(v)


if __name__ == "__main__":
    main()
