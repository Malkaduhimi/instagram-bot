import sys
from InstagramAPI import InstagramAPI

class Authentication:
    def login_from_arguments(self):
        if len(sys.argv) < 3:
            print('usage: command [username] [password]')
            exit(1)
        
        username=sys.argv[1]
        password=sys.argv[2]
    
        return self.login(username, password)

    def login(self, username, password):
        instagram_api = InstagramAPI(username, password)
        instagram_api.login()
        
        return instagram_api

