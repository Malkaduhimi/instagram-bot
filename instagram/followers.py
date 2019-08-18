from .util import Authentication
from .profile import OwnProfile
import time

class Followers:
    def __init__(self, instagram_api):
        self.instagram_api = instagram_api
    
    def get_followers_list(self, user_id):
        next_max_id = True
        followers = []
        
        while next_max_id:
            if next_max_id == True: next_max_id=''
            self.instagram_api.getUserFollowers(user_id, maxid=next_max_id)
            followers.extend(self.instagram_api.LastJson.get('users', []))
            next_max_id = self.instagram_api.LastJson.get('next_max_id', '')
            time.sleep(2)
        
        return followers

    def get_following_list(self, user_id):
        next_max_id = True
        following = []
        
        while next_max_id:
            if next_max_id == True: next_max_id=''
            self.instagram_api.getUserFollowings(user_id, maxid=next_max_id)
            following.extend(self.instagram_api.LastJson.get('users', []))
            next_max_id = self.instagram_api.LastJson.get('next_max_id', '')
            time.sleep(2)
        
        return following

    def get_stats(self, user_id):
        followers_list = followers_helper.get_followers_list(user_id)
        following_list = followers_helper.get_following_list(user_id)
        
        user_list = map(lambda x: x['username'] , following_list)
        following_set= set(user_list)
        
        user_list = map(lambda x: x['username'] , followers_list)
        followers_set= set(user_list)
        
        not_following_back_set = following_set - followers_set
        fans_set = followers_set - following_set

        return {
            "followers": followers_list,
            "following": following_list,
            "not_following_back": list(not_following_back_set),
            "fans": list(fans_set)
        }

if __name__ == "__main__":
    authentication = Authentication()
    instagram_api = authentication.login_from_arguments()
    followers_helper = Followers(instagram_api)
    profile_helper = OwnProfile(instagram_api)

    user_id = profile_helper.get_user_id()
    print('user id is {}'.format(user_id))

    stats = followers_helper.get_stats(user_id)
    
    print('following: {}'.format(len(stats['following'])))
    print('followers: {}'.format(len(stats['followers'])))
    print('not following back: {}'.format(len(stats['not_following_back'])))
    print('fans: {}'.format(len(stats['fans'])))

    print('not following back:')
    print(stats['not_following_back'])

    print('fans:')
    print(stats['fans'])
