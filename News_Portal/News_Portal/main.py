from News_Portal.Models.models import *

class SQL_request:
    def __init__(self,user:str):
        self.user=User.objects.get(username=user)
        self.author=Author.objects.get(user=self.user)
        self.post=Post.objects.get(author=self.author)
        self.comments=Comment.objects.get(user=self.user.user)
    # def get_data():
    #     u1 = User.objects.get(username='Достоевский')
    #     u2 = User.objects.get(username='Толстой')
    #     u3 = User.objects.get(username='Mark Twain')
    #
    #     a1 = Author.objects.get(user=u1)
    #     a2 = Author.objects.get(user=u2)
    #     a3 = Author.objects.get(user=u3)
    #
    #     p1 = Post.objects.get(author=a1)
    #     p2 = Post.objects.get(author=a2)
    #     p3 = Post.objects.get(author=a3)
    #
    #     c1 = Comment.objects.get(user=a1.user)
    #     c2 = Comment.objects.get(user=a2.user)
    #     c3 = Comment.objects.get(user=a3.user)

u1=SQL_request('Достоевский')
print(u1.user)
