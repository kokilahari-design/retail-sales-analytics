
FROM python:3.10                       # Base Image for docker container from public registry
WORKDIR /app                           # set the working directory in the image
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app                            # copy all files from host file system to image file system
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
