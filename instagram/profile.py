from .util import Authentication
import time

class OwnProfile:
    def __init__(self, instagram_api):
        self.instagram_api = instagram_api

    def get_user_id(self):
        self.instagram_api.getProfileData()
        return self.instagram_api.LastJson['user']['pk']

    def get_data(self):
        self.instagram_api.getProfileData()
        return self.instagram_api.LastJson['user']

    def get_feed(self):
        myposts=[]
        has_more_posts = True
        max_id=""
        
        while has_more_posts:
            self.instagram_api.getSelfUserFeed(maxid=max_id)
            if self.instagram_api.LastJson['more_available'] is not True:
                has_more_posts = False #stop condition
                
            max_id = self.instagram_api.LastJson.get('next_max_id','')
            myposts.extend(self.instagram_api.LastJson['items']) #merge lists
            time.sleep(2) # Slows the script down to avoid flooding the servers 
            
        return myposts
    
    def get_timeline(self):
        self.instagram_api.getTimeline()
        return self.instagram_api.LastJson
    
class Profile:
    def __init__(self, instagram_api):
        self.instagram_api = instagram_api
    
    def get_user_id(self, username):
        self.instagram_api.searchUsername(username)
        return self.instagram_api.LastJson['user']['pk']

    def get_data(self, user_id):
        self.instagram_api.getUsernameInfo(user_id)
        return self.instagram_api.LastJson['user']
    
    def get_feed(self, user_id):
        myposts=[]
        has_more_posts = True
        max_id=""
        
        while has_more_posts:
            self.instagram_api.getUserFeed(user_id, maxid=max_id)
            if self.instagram_api.LastJson['more_available'] is not True:
                has_more_posts = False #stop condition
                
            max_id = self.instagram_api.LastJson.get('next_max_id','')
            myposts.extend(self.instagram_api.LastJson['items']) #merge lists
            time.sleep(2) # Slows the script down to avoid flooding the servers 
            
        return myposts

if __name__ == "__main__":
    authentication = Authentication()
    instagram_api = authentication.login_from_arguments()

    profile = Profile(instagram_api)
    user_id = profile.get_user_id('thewiseminds')
    print(profile.get_data(user_id))

    #own_profile = OwnProfile(instagram_api)
    #print(own_profile.get_timeline())
