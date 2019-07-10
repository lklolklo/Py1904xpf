import xadmin
from .models import *
xadmin.site.register(Category)
xadmin.site.register(Tag)

class ArticleAdmin:
    style_fields = {"body": "ueditor"}


xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Ads)