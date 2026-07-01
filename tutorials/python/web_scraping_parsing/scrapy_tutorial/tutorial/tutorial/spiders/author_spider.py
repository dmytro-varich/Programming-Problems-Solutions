import scrapy


class AuthorSpider(scrapy.Spider):
    """A spider to scrape author details from http://quotes.toscrape.com"""
    name = "author"

    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        """Parse the response and extract author page links and pagination links."""
        author_page_links = response.css(".author + a")
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css("li.next a")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        """Parse the response and extract author details."""
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }
