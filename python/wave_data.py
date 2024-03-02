def get_data_source_url(station=STATION_ID, metric=METRIC, hilo_only=True):
    """Build and return the URL for the tides API."""
    date = "{}{:02}{:02}".format(now.tm_year, now.tm_mon, now.tm_mday)

    URL = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?format=json"
    URL += "&product=predictions"
    URL += "&interval=hilo" if hilo_only else ""
    URL += "&datum=mllw"  # MLLW = "tides"
    URL += "&units=metric" if metric else "&units=english"
    URL += "&time_zone=lst_ldt" if DST_ON else "&time_zone=lst"
    URL += "&begin_date=" + date
    URL += "&end_date=" + date
    URL += "&station=" + station

    return URL
