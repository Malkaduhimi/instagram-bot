from instagram.util import Authentication
from instagram.tag import Tag
from instagram.actions import PersonalInteraction, MediaInteraction
from models import User, Account
from datetime import date, timedelta
import sys
import pickle

import random
import time
from base import Session, engine, Base

class Bot:
    def __init__(self, tags):
        self.tags = tags
        self.init_db()
        self.login()

    def init_db(self):
        Base.metadata.create_all(engine)
        self.session = Session()
    
    def start(self):
        while True:
            self.cycle()
            self.wait(120, 1200)
        
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
        nr_followed_in_cycle = 0
        nr_liked_in_cycle = 0
        
        for tag in tag_feed:
            if nr_followed_in_cycle < 2 \
               and not tag['user']['friendship_status']['following'] \
               and not self.is_user_followed(tag['user']['pk']):

                print('  * follow {}'.format(tag['user']['username']))
                personal.follow(tag['user']['pk'])
                self.save_followed_user(tag['user']['pk'], tag['user']['username'])
                nr_followed_in_cycle += 1

            if nr_liked_in_cycle < 3 and not tag['has_liked']:
                print('  * like post {} from user {}'.format(tag['pk'], tag['user']['username']))
                media.like(tag['pk'])
                nr_liked_in_cycle += 1
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

    def login(self):
        authentication = Authentication()
        (username, password) = authentication.get_arguments()
        seven_days_ago = date.today() - timedelta(days=7)
        account = self.session.query(Account).filter(Account.username == username, Account.login_date > seven_days_ago).first()
        if account is None:
            print('- logging in')
            self.instagram_api = authentication.login(username, password)
            account = Account(user_id=self.instagram_api.username_id, username=username, login_date=date.today(), instagram_object=pickle.dumps(self.instagram_api))
            self.session.add(account)
            self.session.commit()
        else:
            print('- found logged in session')
            self.instagram_api = pickle.loads(account.instagram_object)
        
        
if __name__ == "__main__":
    bot = Bot(['coding', 'developer', 'programming', 'developerlife', 'coder', 'pythoncoding', 'ai', 'softwaredeveloper'])
    bot.start()
    
