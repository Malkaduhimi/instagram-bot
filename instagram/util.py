import sys
from InstagramAPI import InstagramAPI

class Authentication:
    def login_from_arguments(self):
        (username, password) = self.get_arguments()
        return self.login(username, password)

    def get_arguments(self, command_name='command'):
        if len(sys.argv) < 3:
            print('usage: {} [username] [password]'.format(command_name))
            exit(1)
        
        username=sys.argv[1]
        password=sys.argv[2]
        return (username, password)

    
    def login(self, username, password):
        instagram_api = InstagramAPI(username, password)
        instagram_api.login()
        
        return instagram_api

