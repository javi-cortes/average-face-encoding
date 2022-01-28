# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from io import BytesIO

import face_recognition
from scrapy.pipelines.images import ImagesPipeline


class ImageCrawlerPipeline(ImagesPipeline):
    def media_downloaded(self, response, request, info, *, item=None):

        # img = face_recognition.load_image_file(BytesIO(response.body))
        # print(face_recognition.face_encodings(img))

        return super().media_downloaded(response, request, info, item=item)
