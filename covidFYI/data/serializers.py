from .models import Location, InfoType, Entry
from rest_framework import serializers

class InfoTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfoType
        fields = ('name',)

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('state', 'district',)
        
class EntrySerializer(serializers.ModelSerializer):

    # infotype = InfoTypeSerializer(read_only=True)
    infotype = serializers.CharField(source='infotype.name')
    # location = LocationSerializer()
    # district = serializers.CharField(source='location.district')

    class Meta:
        model = Entry
        # fields = '__all__'
        exclude = ('location', 'added_on',)


class StateListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('state',)
        read_only_fields = fields

class StateRetrieveSerializer(serializers.ModelSerializer):
    
    # district = serializers.CharField(source='district')
    # infotype = serializers.CharField(source='infotype.name')
    entries = serializers.SerializerMethodField(read_only=True)
    # entries = serializers.CharField()

    class Meta:
        model = Location
        exclude = ('state',)
        # extra_fields = ('district',)
        read_only_fields = [f.name for f in Location._meta.get_fields()]

    def get_entries(self, obj):

        entries = obj.entries.all()
        return [EntrySerializer(entry).data for entry in entries]

