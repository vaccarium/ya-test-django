## URL scheme

`/station/<code>/[year/month/]` --- a calendar listing all trains stopping at a station during a specified month
`/train/<id>/` --- a complete schedule of a train

## Deployment

The application requires Django 1.8 and SQLite.

To load some sample data, use `python manage.py loadsample`.
