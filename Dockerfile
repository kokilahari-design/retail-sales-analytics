# Base Image for docker container from public registry
FROM python:3.10

# set the working directory in the image
WORKDIR /app

# copy the files from host file system to image file system
COPY . /app

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
