import Authenticator from instagram.utils
import sqlite3

class Bot:
    def __init__(self):
        self.conn = sqlite3.connect('data/db.sqlite')
        authentication = Authentication()
        self.instagram_api = authentication.login_from_arguments()
        
    def start(self):
        self.cycle()

    def cycle(self):
        tag = Tag(self.instagram_api)
        tag_feed = tag.get_feed()
        print()
    
    def unfollow_step(self):
        
        

if __name__ == "__main__":
    bot = Bot()
    bot.start()
    
