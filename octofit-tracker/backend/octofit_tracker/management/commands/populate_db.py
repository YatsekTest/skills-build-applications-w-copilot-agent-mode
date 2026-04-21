from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from pymongo import IndexModel, ASCENDING
from django.conf import settings
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        db = connection.cursor().db_conn

        # Очистка коллекций
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Создание уникального индекса на email
        db.users.create_index([('email', ASCENDING)], unique=True)

        # Данные
        marvel_team = {'name': 'Marvel', 'members': ['Iron Man', 'Captain America', 'Thor']}
        dc_team = {'name': 'DC', 'members': ['Superman', 'Batman', 'Wonder Woman']}
        db.teams.insert_many([marvel_team, dc_team])

        users = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Steve Rogers', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': 'DC'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': 'DC'},
        ]
        db.users.insert_many(users)

        activities = [
            {'user': 'Tony Stark', 'activity': 'Run', 'distance': 5},
            {'user': 'Steve Rogers', 'activity': 'Swim', 'distance': 2},
            {'user': 'Clark Kent', 'activity': 'Fly', 'distance': 100},
            {'user': 'Bruce Wayne', 'activity': 'Cycle', 'distance': 10},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {'team': 'Marvel', 'points': 150},
            {'team': 'DC', 'points': 170},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {'user': 'Tony Stark', 'workout': 'Chest'},
            {'user': 'Steve Rogers', 'workout': 'Legs'},
            {'user': 'Clark Kent', 'workout': 'Full Body'},
            {'user': 'Bruce Wayne', 'workout': 'Back'},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db успешно заполнена тестовыми данными!'))
