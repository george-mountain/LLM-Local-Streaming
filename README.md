
## Local LLM Streaming

### Overview

In this project, FastAPI and Streamlit are utilized to create and demonstrate how to stream LLM response locally. The project is structured with a backend service responsible for handling the interactions with the LLM using Fastapi, and a frontend service that provides a user interface for making queries using streamlit. Though ChatOpenAI from langchain_openai was used in this project, the same concept can be extened to any LLM. 

### Project Demo

![LLM local streaming demo](https://github.com/george-mountain/LLM-Local-Streaming/assets/19597087/a5748865-284c-48b2-a534-a989d0443d9a)


### Prerequisites

Make sure you have Docker installed on your machine if you want to use the Dockerfiles in this project, otherwise, you have to run the application locally.

### Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/george-mountain/LLM-Local-Streaming.git
   cd LLM-Local-Streaming
   ```

2. Create a `.env` file and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openAI_api_key
   ```

### Running the Application

Use the provided Makefile to build and run the Docker containers:

```bash
make build
make up
```

This will build the necessary Docker images and start the services.

### Usage

1. Access the Streamlit interface by navigating to [http://localhost:8501](http://localhost:8501) in your web browser.

2. Enter your query in the input field and click submit.

3. The backend service will process the query using the LLM, and the results will be displayed dynamically in the Streamlit interface.



- **backend/app.py**: FastAPI application handling LLM model interactions.
- **backend/helpers.py**: Helper classes and functions for streaming responses.
- **backend/Dockerfile**: Dockerfile for building the backend docker image.
- **frontend/app.py**: Streamlit application for user interaction.
- **frontend/Dokcerfile**: Dockerfile for building the frontend docker image.
- **docker-compose.yml**: Docker Compose configuration for services (frontend and backend).
- **Makefile**: Makefile for simplifying common tasks.

### Docker Compose

The project uses Docker Compose to manage the deployment of both frontend and backend services. The `docker-compose.yml` file defines two services - `frontend` and `backend`. The services are connected through a bridge network called `app`.

### Makefile Commands

- `make build`: Build Docker images.
- `make up`: Start Docker containers in detached mode.
- `make up-v`: Start Docker containers in the foreground.
- `make down`: Stop and remove Docker containers.
- `make down-v`: Stop and remove Docker containers along with volumes.
- `make status`: Show status of Docker containers.
- `make show-logs`: Display logs of all Docker containers.
- `make server-logs`: Display logs of the backend service.
- `make frontend-logs`: Display logs of the frontend service.
- `make restart`: Restart Docker containers.
- `make prune`: Remove unused Docker resources.
- `make remove-images`: Remove all Docker images.
- `make stop-container`: Stop a specific Docker container.
- `make remove-container`: Remove a specific Docker container.

### Notes

- Make sure to create the `.env` file and add your OpenAI API key as mentioned in the "Getting Started" section.

