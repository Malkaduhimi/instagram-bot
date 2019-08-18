from instagram.util import Authentication
from instagram.tag import Tag
from instagram.actions import PersonalInteraction, MediaInteraction
from models import User
from datetime import date, timedelta

import random
import time
from base import Session, engine, Base

class Bot:
    def __init__(self, tags):
        authentication = Authentication()
        self.instagram_api = authentication.login_from_arguments()
        self.tags = tags
        self.init_db()

    def init_db(self):
        Base.metadata.create_all(engine)
        self.session = Session()
    
    def start(self):
        while True:
            self.cycle()
            self.wait(120,420)
        
        self.session.close()
            
    def cycle(self):
        self.unfollow_step()
        self.follow_and_like_step()
        
    def follow_and_like_step(self):
        print('----------follow and like step')
        tag_name = random.choice(self.tags)
        tag = Tag(self.instagram_api)
        tag_feed = tag.get_feed(tag_name)
        personal = PersonalInteraction(self.instagram_api)
        media = MediaInteraction(self.instagram_api)
        followed_in_cycle = False
        
        for tag in tag_feed:
            if not followed_in_cycle \
               and not tag['user']['friendship_status']['following'] \
               and not self.is_user_followed(tag['user']['pk']):

                print('  * follow {}'.format(tag['user']['username']))
                personal.follow(tag['user']['pk'])
                self.save_followed_user(tag['user']['pk'], tag['user']['username'])
                followed_in_cycle = True

            if not tag['has_liked']:
                print('  * like post {} from user {}'.format(tag['pk'], tag['user']['username']))
                media.like(tag['pk'])
                self.wait(1, 6)
            

    def unfollow_step(self):
        print('----------unfollow step')
        unfollow_date = date.today() - timedelta(days=7)
        users = self.session.query(User).filter(User.unfollow_date == None, User.follow_date < unfollow_date).all()
        
        for user in users:
            print('  * unfollow {}'.format(user.username))
            print('BUUUTTT that\'s not implemented yet')

    def wait(self, lower_range, upper_range):
        time.sleep(random.choice(range(lower_range,upper_range)))
        
    def is_user_followed(self, user_id):
        return self.session.query(User).filter(User.user_id == user_id, User.unfollow_date == None).count() > 0

    def save_followed_user(self, user_id, username):
        user = User(username=username, user_id=user_id, follow_date=date.today())
        self.session.add(user)
        self.session.commit()

if __name__ == "__main__":
    bot = Bot(['coding', 'developer', 'programming', 'developerlife', 'coder', 'python', 'ai', 'softwaredeveloper'])
    bot.start()
    
