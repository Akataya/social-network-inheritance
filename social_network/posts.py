from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None, user=None):
        self.text = text
        self.timestamp = timestamp.strftime("%A, %b %d, %Y")
        self.user = user

    def set_user(self, user):
        self.user = user


# TextPost: Just a simple text post. Should be constructed as TextPost(text="Post Text").
class TextPost(Post):
    
# Example: '@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'
    def __str__(self):
        return '@{first_name} {last_name}: "{post}"\n\t{timestamp}'.format(first_name=self.user.first_name, last_name=self.user.last_name, post=self.text, timestamp=self.timestamp)
    

# PicturePost: A post containing text and the URL of a picture: Should be constructed as PicturePost(text="Post Text", image_url="imgur.com/OAWTSJu").
class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

        
#'Example: @Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'
    def __str__(self):
        return '@{first_name} {last_name}: "{post}"\n\t{url}\n\t{timestamp}'.format(first_name=self.user.first_name, last_name=self.user.last_name, post=self.text, url=self.image_url, timestamp=self.timestamp)

# CheckInPost: A post containing text and coordinates of the user's position. Should be constructed as CheckInPost(text="Post Text", latitude="40.741895", longitude="-73.989308").
class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

# Example: '@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
    def __str__(self):
        return '@{first_name} Checked In: "{post}"\n\t{latitude}, {longitude}\n\t{timestamp}'.format(first_name=self.user.first_name, post=self.text, latitude = self.latitude, longitude = self.longitude, timestamp=self.timestamp)