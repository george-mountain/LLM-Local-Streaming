import sys
from pathlib import Path

file_path = Path(__file__).resolve()


tests_directory = file_path.parent


base_directory = tests_directory.parent


if base_directory not in sys.path:
    sys.path.insert(0, str(base_directory))
print(base_directory)
from backend.app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_stream():
    response = client.get("/query-stream/?query=testing")
    assert response.status_code == 200
    assert len(response.content) > 0
