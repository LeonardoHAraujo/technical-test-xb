# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# Internal modules.
from utils.http import ok, bad_request
from domain.usecases.create_user_usecase import CreateUserUseCase
from infra.providers.hash.encrypt_password_provider import EncryptPassProvider
from infra.repositories.db.mongodb.create_user_repository import (
    AddUserRepository
)
from infra.repositories.db.mongodb.get_user_by_email_repository import (
    GetUserRepository
)

class CreateUserFactory:

    @staticmethod
    def build():
        '''Return builded use case.'''

        args = {}

        args['ok'] = ok
        args['bad_request'] = bad_request
        args['create_user'] = AddUserRepository()
        args['encrypt_pass'] = EncryptPassProvider()
        args['user_repository'] = GetUserRepository()

        return CreateUserUseCase(**args)

