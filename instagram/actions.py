class MediaInteraction:
    def __init__(self, instagram_api):
        self.instagram_api = instagram_api
    
    def like(self, media_id):
        self.instagram_api.like(self, mediaId)

    def unlike(self, media_id):
        self.instagram_api.unlike(self, mediaId)

    def comment(self, media_id, comment):
        self.instagram_api.comment(self, mediaId, comment)

    def get_likers(self, media_id):
        self.instagram_api.getMediaLikers(self, mediaId)

class PersonalInteraction:
    def __init__(self, instagram_api):
        self.instagram_api = instagram_api
        
    def follow(self, user_id):
        self.instagram_api.follow(user_id)

    def unfollow(self, user_id):
        self.instagram_api.unfollow(user_id)

    def block(self, user_id):
        self.instagram_api.block(user_id)

    def unblock(self, user_id):
        self.instagram_api.unblock(user_id)
