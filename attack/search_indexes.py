from haystack import indexes
from attack.models import Attack


class AttackIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    timestamp = indexes.DateTimeField(model_attr='timestamp')
    ip = indexes.CharField(model_attr='attacker_ip')
    country_code = indexes.CharField(model_attr='country_code', faceted=True)
    attacked_service = indexes.CharField(model_attr='service_name', faceted=True)
    location = indexes.LocationField(model_attr='get_location')

    def get_model(self):
        return Attack

    # def index_queryset(self, using=None):
    #     return self.get_model().objects.filter()

