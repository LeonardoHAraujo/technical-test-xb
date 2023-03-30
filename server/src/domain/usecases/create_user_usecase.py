# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


class CreateUserUseCase:

    def __init__(
        self,
        ok,
        bad_request,
        create_user,
        encrypt_pass,
        user_repository
    ):
        self.ok = ok
        self.bad_request = bad_request
        self.create_user = create_user
        self.encrypt_pass = encrypt_pass
        self.user_repository = user_repository

    def execute(self, data):
        '''Main method for this usecase.'''

        if not data.get('name', ''):
            return self.bad_request('Name not found.')

        if not data.get('email', ''):
            return self.bad_request('Email not found.')

        if not data.get('password', ''):
            return self.bad_request('password not found.')

        if self.user_repository.find_by_email(data['email']):
            return self.bad_request('User already exists.')

        encrypted_pass = self.encrypt_pass.encrypt(data['password'])
        args = {}

        args['name'] = data['name']
        args['email'] = data['email']
        args['password'] = encrypted_pass

        user_id = self.create_user.create(**args)

        return self.ok({'insertedUser': user_id})

