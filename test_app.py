# tests de la calculadora
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_suma():
    r = client.get("/suma?a=10&b=5")
    assert r.json()["resultado"] == 15

def test_suma_decimales():
    r = client.get("/suma?a=1.5&b=2.5")
    assert r.json()["resultado"] == 4.0

def test_resta():
    r = client.get("/resta?a=20&b=8")
    assert r.json()["resultado"] == 12

def test_multi():
    r = client.get("/multi?a=4&b=5")
    assert r.json()["resultado"] == 20

def test_div():
    r = client.get("/div?a=100&b=4")
    assert r.json()["resultado"] == 25

def test_div_entre_cero():
    r = client.get("/div?a=5&b=0")
    assert r.status_code == 400
