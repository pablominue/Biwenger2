FROM python:3.11-slim

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY pyproject.toml poetry.lock /app/

# Install any dependencies specified in requirements.txt
RUN pip install poetry
# COPY ./Biwenger /app/Biwenger
# COPY ./FutbolFantasy /app/FutbolFantasy

COPY ./ /app/
# Make port 5000 available to the world outside this container
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
EXPOSE 5119

# Define environment variable for Flask
ENV FLASK_APP=api.py

# Run the command to start the Flask API
#CMD ["poetry", "run", "flask", "--app", "api", "run", "--host=0.0.0.0", "--port=5119"]

CMD ["poetry", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5119", "api:app"]
