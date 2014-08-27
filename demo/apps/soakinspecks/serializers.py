""" Serializers specific to the soakinspecks app
"""
from rest_framework import serializers

from soakinspecks import models as ss_models


class ProductionBatchSerializer(serializers.ModelSerializer):
    flavor = serializers.PrimaryKeyRelatedField(required=False)
    mixture = serializers.PrimaryKeyRelatedField(required=False)
    class Meta:
        model = ss_models.ProductionBatch


class MixturePartSerializer(serializers.ModelSerializer):
    mixture = serializers.PrimaryKeyRelatedField(required=False)
    class Meta:
        model = ss_models.MixturePart


class MixtureSerializer(serializers.ModelSerializer):
    parts = MixturePartSerializer(many=True)

    class Meta:
        model = ss_models.Mixture

