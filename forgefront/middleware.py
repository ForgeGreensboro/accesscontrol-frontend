from django.utils.deprecation import MiddlewareMixin
from debug_toolbar.middleware import DebugToolbarMiddleware

class ForgeToolBarMiddleWare(MiddlewareMixin, DebugToolbarMiddleware):
    pass

