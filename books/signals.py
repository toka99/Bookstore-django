from django.db.models.signals import post_save , pre_save , post_delete , pre_delete
from django.dispatch import receiver



from .models import Book , Isbn , User

from django.core.mail import send_mail

@receiver(post_save,sender=Book)
def after_book_creation(sender,instance,created,*args,**kwargs):
    if created:
        isbn_instance=Isbn.objects.create(author_title=instance.author.username)

        
        instance.isbn=isbn_instance
        instance.save()


        # send_mail('New Book {}'.format(instance.title),'New Book is created')
    else:
        print("Updating")
