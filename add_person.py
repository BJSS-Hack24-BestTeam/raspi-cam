import cognitive_face as CF

# Setting up keys and endpoint
KEY = '030d5c89e600472bba1d148dddcff568'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)
BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# Images
img_url = 'https://how-old.net/Images/faces2/main007.jpg'

img = open('image1.jpg')
img1 = open('image2.jpg')
img2 = open('image3.jpg')

# Setting up person group
person_group_id = 'man'
person_id = 'callum'
#CF.person_group.create(person_group_id)
print("here")
create = CF.person.create(person_group_id, person_id)
print(create['personId'])
CF.person.add_face('image1.jpg', person_group_id, create['personId'])
CF.person.add_face('image2.jpg', person_group_id, create['personId'])
CF.person.add_face('image3.jpg', person_group_id, create['personId'])
CF.person_group.train(person_group_id)