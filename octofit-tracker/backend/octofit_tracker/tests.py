from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, LeaderboardEntry

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(str(team), "Test Team")

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.team = Team.objects.create(name="Test Team")
    def test_create_activity(self):
        activity = Activity.objects.create(user=self.user, activity_type="run", duration=30, calories=200, date="2024-01-01", team=self.team)
        self.assertEqual(str(activity), f"{self.user.username} - run on 2024-01-01")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Do pushups", difficulty="Easy")
        self.assertEqual(str(workout), "Pushups")

class LeaderboardEntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser2", password="pass")
        self.team = Team.objects.create(name="Test Team 2")
    def test_create_leaderboard_entry(self):
        entry = LeaderboardEntry.objects.create(user=self.user, score=100, team=self.team)
        self.assertEqual(str(entry), f"{self.user.username} - 100.0")
