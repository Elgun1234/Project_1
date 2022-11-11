import logging
import urllib.request

log = logging.getLogger(__name__)

def get_url(url):
    opened_url = urllib.request.urlopen(url)
    read_url = opened_url.read()
    url_content = read_url.decode("utf8")
    opened_url.close()
    log.info("read url successfully")
    return url_content