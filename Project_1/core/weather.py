import logging
from Project_1.core.utils import get_url

log = logging.getLogger(__name__)

class weather:
    def __init__(self):
        log.info("LOADED WEATHER")
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, longitude:float,latitude:float,rain:bool):
        new_url = f"{self.url}?longitude={longitude}&latitude={latitude}&hourly=temperature_2m"
        if rain:
            new_url += ",rain"
            log.info("added rain")

        log.info(new_url)
        return get_url(new_url)




