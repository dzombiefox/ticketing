from rest_framework.serializers import ModelSerializer
from chat .models import  Chat

class ChatSerializer(ModelSerializer):
    class Meta :
        model =Chat
        fields=[
            'chat','karyawan'

        ]

