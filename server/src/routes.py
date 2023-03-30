# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# External modules.
import json
from flask import request

# Internal modules.
from main.app import app
from infra.factories.usecases.auth_factory import AuthFactory
from infra.factories.usecases.jwt_verify_factory import JwtVerifyFactory
from infra.factories.usecases.create_user_factory import CreateUserFactory

@app.route('/jwt/auth', methods=['POST'])
def auth():
    '''Auth route.'''

    data = json.loads(request.data)
    usecase = AuthFactory.build()

    return usecase.execute(data)

@app.route('/jwt/verify/<string:token>', methods=['GET'])
def verify(token):
    '''Verify jwt.'''

    usecase = JwtVerifyFactory.build()
    return usecase.execute(token)

@app.route('/users/create', methods=['POST'])
def create_user():
    '''Verify jwt.'''

    data = json.loads(request.data)
    usecase = CreateUserFactory.build()

    return usecase.execute(data)

if __name__ == '__main__':
    args = {}

    args['host'] = '0.0.0.0'
    args['port'] = 5000

    app.run(**args)

