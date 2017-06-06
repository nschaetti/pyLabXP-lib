from . import models
from rest_framework import serializers


# Serializer for results
class ResultSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.LabLoggerResult
        fields = ('lab', 'exp', 'instance', 'param', 'result', 'value')
    # end Meta

# end ResultSerializer
