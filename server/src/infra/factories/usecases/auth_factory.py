# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# Internal modules.
from utils.http import ok, bad_request
from domain.usecases.make_auth_usecase import MakeAuthUseCase
from infra.providers.hash.encrypt_password_provider import EncryptPassProvider
from infra.providers.jwt.generate_jwt_provider import GenJwtProvider
from infra.repositories.db.mongodb.get_user_by_email_repository import (
    GetUserRepository
)

class AuthFactory:

    @staticmethod
    def build():
        '''Return builded use case.'''

        args = {}

        args['user_repository'] = GetUserRepository()
        args['ok'] = ok
        args['bad_request'] = bad_request
        args['encrypt_pass'] = EncryptPassProvider()
        args['generate_jwt'] = GenJwtProvider()

        return MakeAuthUseCase(**args)
