import sys
from pathlib import Path

file_path = Path(__file__).resolve()


tests_directory = file_path.parent


base_directory = tests_directory.parent

if base_directory not in sys.path:
    sys.path.insert(0, str(base_directory))


print(file_path)
print(tests_directory)
print(base_directory)

from backend.helpers import StreamingCustomHandler
from langchain.schema import LLMResult


def test_on_llm_new_token():
    queue = MockQueue()
    handler = StreamingCustomHandler(queue)
    handler.on_llm_new_token("token")
    assert queue.get() == "token"


def test_on_llm_end():
    queue = MockQueue()
    handler = StreamingCustomHandler(queue)

    llm_result = LLMResult(generations=[], output="result")

    handler.on_llm_end(llm_result)

    assert queue.get() == None


class MockQueue:
    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)

    def task_done(self):
        pass
