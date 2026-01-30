import scrapy


class NeweggSpiderSpider(scrapy.Spider):
    name = "newegg_spider"
    allowed_domains = ["newegg.com"]
    start_urls = ["https://www.newegg.com/Laptops-Notebooks/SubCategory/ID-32"]
    def parse(self, response):
        self.page_number=1
        self.logger.info(f"Entered {response.url}")
        self.logger.info(f"Scraping page no {self.page_number}:{response.url}")

        products = response.css("div.item-cell")
        self.logger.info(f"Found {len(products)} laptops")

        #for i in range(len(products)):
        for i in products:# first 5 for testing
            name = i.css("a.item-title::text").get()
            link = i.css("a.item-title::attr(href)").get()
            rating=i.css("i.rating::attr(class)").get()
            price_main=i.css("div.item-action li.price-current strong::text").get()
            price_decimal=i.css("div.item-action li.price-current sup::text").get()
            total_price=(price_main+(price_decimal or "") if price_main else None)
        
            if name and link:
                yield {
                    "name": name.strip() if name else None,
                    "link": link,
                    "ratings":rating.strip() if rating else None,
                    "Total price":total_price
                }
                
       # next_page = response.xpath("//a[@title='Next']/@href").get()
        next_page = response.css("a[title='Next']::attr(href)").get()
        if next_page:
            self.logger.info(f"Following next page:{next_page}")
            yield response.follow(next_page, callback=self.parse)
