# Based on url_handlers.py by Chris Jones <cmsj@tenshu.net?
import re
import terminatorlib.plugin as plugin

# Every plugin you want Terminator to load *must* be listed in 'AVAILABLE'
AVAILABLE = ['GitRemoteSshToHttps']


class GitRemoteSshToHttps(plugin.URLHandler):
    """Convert Git remote SSH to HTTPS"""

    capabilities = ['url_handler']
    handler_name = 'gitssh2https'
    match = r'\s+git\@(.*):(.*)\.git\s+'
    nameopen = "Open remote site https://"
    namecopy = "Copy remote site https://"

    def callback(self, url):
        """Convert URL with git@xxxx:/path to https://xxxxx/path"""
        return(url.replace(":", "/").replace("git@", "https://", 1).strip())
