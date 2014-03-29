"""Python Soundcloud API Wrapper."""

__version__ = '0.4.1'
__all__ = ['Client']

USER_AGENT = 'SoundCloud Python API Wrapper %s' % __version__

from txsoundcloud.client import Client
