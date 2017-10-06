from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from chat .models import  Chat
from employee .models import Karyawan


class KaryawanSerializer(serializers.ModelSerializer):
    chats = serializers.StringRelatedField(many=True)

    class Meta:
        model = Karyawan
        fields=('namaKaryawan')


class ChatSerializer(serializers.ModelSerializer):
    karyawans= KaryawanSerializer(many=True, read_only=True)
    class Meta :
        model =Chat
        fields= ('__all__')
        depth = 1
