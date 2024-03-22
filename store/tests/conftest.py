from rest_framework.test import APIClient
from django.contrib.auth.models import User
import pytest



@pytest.fixture
def api_client():
  return APIClient()

@pytest.fixture
def client_authenticate(api_client):
  def do_client_authentication(is_staff =False):
    return api_client.force_authenticate(user= User(is_staff=is_staff))
  return do_client_authentication