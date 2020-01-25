import sys
from InstagramAPI import InstagramAPI
import json

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

        if (hasattr(instagram_api.LastJson, 'message') and instagram_api.LastJson['message'] == 'challenge_required'):
            print(instagram_api.LastJson)
            challenge_message = instagram_api.s.get(instagram_api.API_URL + instagram_api.LastJson['challenge']['api_path'][1:])
            print(json.loads(challenge_message.text))

            challenge_choice = instagram_api.s.post(instagram_api.API_URL + instagram_api.LastJson['challenge']['api_path'][1:], data={'choice': '1'})
            print(json.loads(challenge_choice.text))

            input_code = input('enter code: ')
            print(input_code)

            a = instagram_api.s.post(instagram_api.API_URL + instagram_api.LastJson['challenge']['api_path'][1:], data={'security_code': int(input_code)})
            print(json.loads(a.text))

            instagram_api.login()
        
        return instagram_api

