FROM python:3.8-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /website
COPY . .

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD [ "python3", "app.py", "--host=0.0.0.0"]
