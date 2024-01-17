import asyncio
import sys
from pathlib import Path
from queue import Queue
from threading import Thread

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain.schema.messages import HumanMessage
from langchain_openai import ChatOpenAI

file_path = Path(__file__).resolve()


tests_directory = file_path.parent


base_directory = tests_directory.parent


if base_directory not in sys.path:
    sys.path.insert(0, str(tests_directory))

print(base_directory)

from helpers import StreamingCustomHandler

load_dotenv()


app = FastAPI()

streamer_queue = Queue()
my_handler = StreamingCustomHandler(streamer_queue)

llm = ChatOpenAI(streaming=True, callbacks=[my_handler], temperature=0.7)


def generate(query):
    llm.invoke([HumanMessage(content=query)])


def start_generation(query):
    thread = Thread(target=generate, kwargs={"query": query})
    thread.start()


async def response_generator(query):
    start_generation(query)

    while True:
        value = streamer_queue.get()
        if value == None:
            break
        yield value
        streamer_queue.task_done()
        await asyncio.sleep(0.1)


@app.get("/query-stream/")
async def stream(query: str):
    print(f"Query receieved: {query}")
    return StreamingResponse(response_generator(query), media_type="text/event-stream")
