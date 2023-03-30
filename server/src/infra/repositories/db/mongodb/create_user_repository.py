# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# Internal modules.
from .mongo_helper import MongoHelper
from domain.repositories.db.create_user_repository import (
    CreateUserRepository
)

class AddUserRepository(CreateUserRepository):

    def create(self, name, email, password):
        '''Create user repository.'''

        user = {'name': name, 'email': email, 'password': password}
        users_collection = MongoHelper.get_collection('users')

        new_user = users_collection.insert_one(user)

        return str(new_user.inserted_id)

