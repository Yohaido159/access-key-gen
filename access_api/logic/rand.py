from users.models import User
import random



def set_to_user(user , post):

    num_list = []
    for x in range(10):
        num = random.randint(1, 20)
        num_list.append(num)
    
    access_key = "".join(map(str , num_list))

    user.set_access(access_key)
    user.save()

    post.set_post_access(post.id , access_key)