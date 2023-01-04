# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


class MakeAuthUseCase:

    def __init__(
        self,
        user_repository,
        ok,
        bad_request,
        encrypt_pass,
        generate_jwt
    ):
        self.user_repository = user_repository
        self.ok = ok
        self.bad_request = bad_request
        self.encrypt_pass = encrypt_pass
        self.generate_jwt = generate_jwt

    def execute(self, data):
        '''Main method for this usecase.'''

        if not data.get('email', ''):
            return self.bad_request('Email not found.')

        if not data.get('password', ''):
            return self.bad_request('Password not found.')

        if not (user := self.user_repository.find_by_email(data['email'])):
            return self.bad_request('User or password incorrect.')

        if user['password'] != self.encrypt_pass.encrypt(data['password']):
            return self.bad_request('User or password incorrect.')

        token = self.generate_jwt.generate(str(user['_id']))
        rep = {}

        rep['token'] = token
        rep['name'] = user['name']
        rep['email'] = user['email']

        return self.ok(rep)
