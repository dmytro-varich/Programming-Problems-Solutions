# from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    """A spider to scrape quotes from http://quotes.toscrape.com"""
    name = "quotes"
    start_urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/",
        ]

    # EXAMPLE 1:
    # async def start(self):
    #     urls = [
    #         "http://quotes.toscrape.com/page/1/",
    #         "http://quotes.toscrape.com/page/2/",
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     """Parse the response and save the HTML content to a file."""
    #     page = response.url.split("/")[-2]
    #     filename = f"quotes-{page}.html"
    #     Path(filename).write_bytes(response.body)
    #     self.log(f"Saved file {filename}")
    #

    # EXAMPLE 2:  
    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         yield {
    #             "text": quote.css("span.text::text").get(),
    #             "author": quote.css("small.author::text").get(),
    #             "tags": quote.css("div.tags a.tag::text").getall(),
    #         }

    def parse(self, response):
        """Parse the response and extract quotes, authors, and tags.
        
        Also follows pagination links to scrape quotes from multiple pages.
        """
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            # 1 options:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            # 2 options: 
            yield response.follow(next_page, callback=self.parse)
