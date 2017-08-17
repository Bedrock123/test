from storages.backends.s3boto import S3BotoStorage
from HarperUser.serializers import UserSerializer
MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')



def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }