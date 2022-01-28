FROM python:3.9.5

RUN apt update && apt-get -y install cmake

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONBUFFERED=1

COPY . /app
WORKDIR /app/image_crawler/

CMD ["scrapy", "crawl", "img_crawler", "--nolog"]
