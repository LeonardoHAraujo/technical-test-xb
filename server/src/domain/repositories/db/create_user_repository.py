# Copyright (C) LA Sistemas - All Rights Reserved.
#
# Written by Leonardo - ledharaujo@gmail.com, February 2022.
#
# Unauthorized copying of this file, via any medium, is strictly prohibited.
# Proprietary and confidential.


# External modules.
from abc import ABC, abstractmethod

class CreateUserRepository(ABC):

    @abstractmethod
    def create(self, name, email, password):
        '''Create user.'''

        raise Exception('Method not implemented')

