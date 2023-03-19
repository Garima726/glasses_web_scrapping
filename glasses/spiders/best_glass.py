import scrapy


class BestGlassSpider(scrapy.Spider):
    name = "best_glass"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]

    def parse(self, response):
        for glasses in response.xpath("//div[@id='product-lists']/div"):
            yield{
                'name': glasses.xpath("normalize-space(.//div[@class='p-title-block']/div[@class='mt-3']/div/div/div[@class='p-title']/a/text())").get(),
                'price': glasses.xpath(".//div[@class='p-title-block']/div[@class='mt-3']/div/div/div[@class='p-price']/div/span/text()").get(),
                'image': glasses.xpath(".//div[@class='product-img-outer']/a/img[@class='lazy d-block w-100 product-img-default']/@src").get(),
                'url': glasses.xpath(".//div[@class='product-img-outer']/a/@href").get()
            }
            nxt_page = response.xpath("(//ul[@class='pagination'])[1]/li[position() =7]/a/@href").get()
            if nxt_page:
                yield scrapy.Request(url=nxt_page, callback=self.parse)