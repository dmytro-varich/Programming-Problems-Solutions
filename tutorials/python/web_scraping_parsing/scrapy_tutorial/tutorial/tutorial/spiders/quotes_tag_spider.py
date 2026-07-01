import scrapy


class QuotesTagSpider(scrapy.Spider):
    """A spider to scrape quotes and their tags from http://quotes.toscrape.com"""
    name = "quotes_tag"

    async def start(self):
        url = "http://quotes.toscrape.com/"
        tag = getattr(self, "tag", None)
        if tag is not None:
            url = url + "tag/" + tag
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Parse the response and extract quotes, authors. and tags"""
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
