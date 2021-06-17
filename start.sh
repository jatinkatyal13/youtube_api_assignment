#! /bin/bash

cron && gunicorn youtube_api.wsgi -b 0.0.0.0:8000