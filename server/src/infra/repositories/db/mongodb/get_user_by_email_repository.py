# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# Internal modules.
from .mongo_helper import MongoHelper
from domain.repositories.db.get_user_by_email_repository import (
    GetUserByEmailRepository
)

class GetUserRepository(GetUserByEmailRepository):

    def find_by_email(self, email):
        '''Get user by email.'''

        users_collection = MongoHelper.get_collection('users')
        user = users_collection.find_one({'email': email})

        return user
