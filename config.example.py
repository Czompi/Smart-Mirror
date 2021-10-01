#!/usr/local/bin/python
# coding=utf-8

# config.py

ui_locale = '' # e.g. 'fr_FR' fro French, '' as default
time_format = 12 # 12 or 24
date_format = "%b %d, %Y" # check python doc for strftime() for options
news_country_code = 'hu'
weather_api_token = '<TOKEN>' # create account at https://darksky.net/dev/
weather_lang = 'hu' # see https://darksky.net/dev/docs/forecast for full list of language parameters values
weather_unit = 'metric' # see https://darksky.net/dev/docs/forecast for full list of unit parameters values
latitude = 46.366531 # Kaposvar, Hungary | Set this if IP location lookup does not work for you (must be a string)
longitude = 17.782480 # Kaposvar, Hungary | Set this if IP location lookup does not work for you (must be a string)
xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18
