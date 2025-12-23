import pytest
from datetime import date
from src.models import TVShow, Episode, ShowStatus


@pytest.fixture
def raw_show_data():
    return {
        "id": 23,
        "url": "https://www.tvmaze.com/shows/23/once-upon-a-time-in-wonderland",
        "name": "Once Upon a Time in Wonderland",
        "type": "Scripted",
        "language": "English",
        "genres": ["Drama", "Adventure", "Fantasy"],
        "status": "Ended",
        "runtime": 60,
        "averageRuntime": 60,
        "premiered": "2013-10-10",
        "ended": "2014-04-03",
        "officialSite": None,
        "schedule": {"time": "20:00", "days": ["Thursday"]},
        "rating": {"average": 6.8},
        "weight": 92,
        "network": {
            "id": 3,
            "name": "ABC",
            "country": {"name": "United States", "code": "US", "timezone": "America/New_York"},
            "officialSite": "https://abc.com/"
        },
        "webChannel": None,
        "dvdCountry": None,
        "externals": {"tvrage": 35215, "thetvdb": 269654, "imdb": "tt2802008"},
        "image": {
            "medium": "https://static.tvmaze.com/uploads/images/medium_portrait/73/183661.jpg",
            "original": "https://static.tvmaze.com/uploads/images/original_untouched/73/183661.jpg"
        },
        "summary": "<p>In Victorian England...</p>",
        "updated": 1704793800,
        "_links": {
            "self": {"href": "https://api.tvmaze.com/shows/23"},
            "previousepisode": {"href": "https://api.tvmaze.com/episodes/1313", "name": "And They Lived…"}
        }
    }


@pytest.fixture
def raw_episodes_data():
    return [
        {
            "id": 1301,
            "url": "https://www.tvmaze.com/episodes/1301/once-upon-a-time-in-wonderland-1x01-down-the-rabbit-hole",
            "name": "Down the Rabbit Hole",
            "season": 1,
            "number": 1,
            "type": "regular",
            "airdate": "2013-10-10",
            "airtime": "20:00",
            "airstamp": "2013-10-11T00:00:00+00:00",
            "runtime": 60,
            "rating": {"average": 6.9},
            "image": {"medium": "...", "original": "..."},
            "summary": "<p>In the series premiere episode...</p>",
            "_links": {"self": {"href": "..."}, "show": {"href": "..."}}
        },
        {
            "id": 1302,
            "url": "https://www.tvmaze.com/episodes/1302/once-upon-a-time-in-wonderland-1x02-trust-me",
            "name": "Trust Me",
            "season": 1,
            "number": 2,
            "type": "regular",
            "airdate": "2013-10-17",
            "airtime": "20:00",
            "airstamp": "2013-10-18T00:00:00+00:00",
            "runtime": 60,
            "rating": {"average": 6.9},
            "image": {"medium": "...", "original": "..."},
            "summary": "<p>In Wonderland...</p>",
            "_links": {"self": {"href": "..."}, "show": {"href": "..."}}
        }
    ]


@pytest.fixture
def sample_show():
    return TVShow(
        id=1,
        title="Test Show",
        release_date=date(2020, 1, 1),
        end_date=None,
        rating=8.5,
        genres=["Drama"],
        status=ShowStatus.RUNNING
    )


@pytest.fixture
def sample_episodes():
    return [
        Episode(id=101, title="Ep 1", release_date=date(2020, 1, 1),
                rating=8.0, season=1, number=1, runtime=60),
        Episode(id=102, title="Ep 2", release_date=date(2020, 1, 8),
                rating=7.5, season=1, number=2, runtime=45),
        Episode(id=201, title="Ep 3", release_date=date(2021, 1, 1),
                rating=9.0, season=2, number=1, runtime=50),
    ]
