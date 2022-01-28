import scrapy

from image_crawler.items import ImageCrawlerItem

from image_crawler.settings import WEB_TO_CRAWL


class ImageDownloaderCrawler(scrapy.Spider):
    name = "img_crawler"
    start_urls = [
        WEB_TO_CRAWL
    ]

    def parse(self, response, **kwargs):
        item = ImageCrawlerItem()
        rel_img_urls = response.xpath("//img/@src").extract()
        item["image_urls"] = self.url_join(rel_img_urls, response)
        yield item

    @staticmethod
    def url_join(rel_img_urls, response):
        """
        img_urls needs to be a list and needs to contain ABSOLUTE URLs that’s why sometimes you have to create a
         function to transform relative URLs to absolute.
        :param rel_img_urls:
        :param response:
        :return:
        """
        joined_urls = []
        for rel_img_url in rel_img_urls:
            joined_urls.append(response.urljoin(rel_img_url))

        return joined_urls
