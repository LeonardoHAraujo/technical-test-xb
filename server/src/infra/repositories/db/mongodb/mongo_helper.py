# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# External modules.
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Init dotenv
load_dotenv()

class MongoHelper:

    @staticmethod
    def get_collection(name):
        '''To get collection from database.'''

        URI = os.getenv('MONGO_URI')
        client = MongoClient(URI)

        return client['xb_test'][name]
