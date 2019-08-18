from util import Authentication
import time

class Tag:
    def __init__(self, instagram_api):
        self.instagram_api = instagram_api
        
    def search(self, text):
        self.instagram_api.searchTags(text)
        return self.instagram_api.LastJson['results']

    def get_feed(self, tag, ranked=False):
        self.instagram_api.tagFeed(tag)
        return self.instagram_api.LastJson['ranked_items'] if ranked else self.instagram_api.LastJson['items']

if __name__ == "__main__":
    authentication = Authentication()
    instagram_api = authentication.login_from_arguments()

    tag = Tag(instagram_api)
    print(tag.get_feed('coding'))
