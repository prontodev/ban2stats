from haystack import indexes
from attack.models import Attack


class AttackIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    timestamp = indexes.DateTimeField(model_attr='timestamp')

    def get_model(self):
        return Attack