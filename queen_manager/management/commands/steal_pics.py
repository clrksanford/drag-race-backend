from django.core.management.base import BaseCommand
import cloudinary
import cloudinary.uploader


from ...models import Queen


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        cloudinary.config(
            cloud_name='ddnibgj3z',
            api_key='539497515485452',
            api_secret='MkB8Jjk2jt9tzd8Lyz-c7nWX70U'
        )

        queens = Queen.objects.all()
        errs = ''

        for queen in queens:
            try:
                img = cloudinary.uploader.upload(queen.image_url)
                queen.image_url = img['url']
                queen.save()
            except Exception as msg:
                print(msg, queen.name, queen.image_url)
