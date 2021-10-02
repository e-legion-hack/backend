from typing import Union, List, Dict

from rest_framework import serializers


class SerializerSaver(serializers.BaseSerializer):
    @classmethod
    def save_data(Serializer, data: Union[List, Dict]):
        if isinstance(data, list):
            serializer = Serializer(data=data, many=True)
        elif isinstance(data, dict):
            serializer = Serializer(data=data)
        else:
            raise serializers.ValidationError(
                f"Type of data is not List nor Dict."
            )
        if serializer.is_valid():
            serializer.save()
            return serializer.instance, None
        else:
            print(
                f"serializer {Serializer.__name__} is not valid\n"         
                f"reasons: {serializer.errors}"
            )
            return None, {"errors": serializer.errors}
