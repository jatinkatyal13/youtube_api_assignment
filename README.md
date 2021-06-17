# Youtube API Assignment

## Framework and Tech used
- Django
- Docker
- Postgres
- Django Rest Framework

## Steps to setup using docker
- Copy `sample.env` with the name `.env`
- Build the container using `docker-compose build`
- Pull the dependent containers using `docker-compose pull`
- Run the containers using `docker-compose up -d`
- Run the migrations using `docker-compose exec yt_api python manage.py migrate`

## Steps to setup without docker
- Copy `sample.env` with the name `.env`
- Install postgres and create a database for the application
- Add database credentials as following environment variables
    - `DB_NAME`
    - `DB_USER`
    - `DB_PASSWORD`
    - `DB_HOST`
- Run the migrations `python manage.py migrate`
- Start the server `python manage.py runserver`
- Add the `cron/sync_youtube_videos.py` script to crontab (checkout `cron.cfg`)

## Available endpoints

- `/api/videos/`

```json
{
  "count": 5,
  "next": "http://localhost:8000/api/videos/?page=2",
  "previous": null,
  "results": [
    {
      "video_id": "yKdEzqwv47A",
      "title": "Fognini Faces Cilic; Draper and Norrie Take to the Grass | Queen&#39;s 2021 Highlights Day 3",
      "description": "Tennis TV is the OFFICIAL live streaming service of the ATP Tour. Tennis TV features live streaming and video on demand of ATP tennis matches in full on PC, ...",
      "published_at": "2021-06-16T20:02:23Z",
      "thumbnail_url": "https://i.ytimg.com/vi/yKdEzqwv47A/default.jpg"
    },
    {
      "video_id": "Q0lUlCJAako",
      "title": "Federer Battles Auger-Aliassime; Rublev &amp; Struff in Action | Halle 2021 Highlights Day 3",
      "description": "Tennis TV is the OFFICIAL live streaming service of the ATP Tour. Tennis TV features live streaming and video on demand of ATP tennis matches in full on PC, ...",
      "published_at": "2021-06-16T19:08:09Z",
      "thumbnail_url": "https://i.ytimg.com/vi/Q0lUlCJAako/default.jpg"
    }
  ]
}

```

- `/api/videos/search?search=live%20official`

```json
{
  "count": 3,
  "next": "http://localhost:8000/api/videos/search?page=2&search=live+official",
  "previous": null,
  "results": [
    {
      "video_id": "yKdEzqwv47A",
      "title": "Fognini Faces Cilic; Draper and Norrie Take to the Grass | Queen&#39;s 2021 Highlights Day 3",
      "description": "Tennis TV is the OFFICIAL live streaming service of the ATP Tour. Tennis TV features live streaming and video on demand of ATP tennis matches in full on PC, ...",
      "published_at": "2021-06-16T20:02:23Z",
      "thumbnail_url": "https://i.ytimg.com/vi/yKdEzqwv47A/default.jpg"
    },
    {
      "video_id": "Q0lUlCJAako",
      "title": "Federer Battles Auger-Aliassime; Rublev &amp; Struff in Action | Halle 2021 Highlights Day 3",
      "description": "Tennis TV is the OFFICIAL live streaming service of the ATP Tour. Tennis TV features live streaming and video on demand of ATP tennis matches in full on PC, ...",
      "published_at": "2021-06-16T19:08:09Z",
      "thumbnail_url": "https://i.ytimg.com/vi/Q0lUlCJAako/default.jpg"
    }
  ]
}
```
