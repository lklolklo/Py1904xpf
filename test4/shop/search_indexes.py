from haystack import indexes
from .models import Foods,Tag
class FoodsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Foods
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class TagIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Tag
    def index_queryset(self, using=None):
        return self.get_model().objects.all()