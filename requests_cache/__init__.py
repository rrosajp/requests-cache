# flake8: noqa: E402,F401
from logging import getLogger

__version__ = '0.7.0'

logger = getLogger(__name__)


def get_placeholder_class(original_exception: Exception = None):
    """Create a placeholder type for a class that does not have dependencies installed.
    This allows delaying ImportErrors until init time, rather than at import time.
    """

    class Placeholder:
        def __init__(*args, **kwargs):
            msg = 'Dependencies are not installed for this feature'
            logger.error(msg)
            raise original_exception or ImportError(msg)

    return Placeholder


try:
    from .backends import *
    from .patcher import *
    from .models import *
    from .serializers import *
    from .session import ALL_METHODS, CachedSession, CacheMixin
# Log and ignore ImportErrors, if setup.py is invoked outside a virtualenv
except ImportError as e:
    logger.warning(e)
