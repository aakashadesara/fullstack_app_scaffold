ALLOWED_HOSTS=['*']
CORS_ALLOW_ALL_ORIGINS=True

class CORSMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
        response['Access-Control-Allow-Credentials'] = 'true'

        return response