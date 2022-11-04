from . import _version
from .notifications import DiscordWebhook  # noqa

__version__ = _version.get_versions()["version"]

__all__ = [
    "DiscordWebhook"
]
