import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess

class WebUsSpider(scrapy.Spider):
    name = "web-us"
    allowed_domains = ["www.hipaaspace.com"]
    start_urls = ["https://www.hipaaspace.com/ein/ein_verification/113242334"]
    uk_suppliers = []
    def parse(self, response):
        # Trích xuất thông tin cần thiết từ response
        company_name = response.xpath(
            '//tbody/tr[4]/td[2]/strong/text()').get()
        tax_code = response.xpath(
            '//*[@id="masterForm"]/div[3]/div/div/main/div/div[10]/div[1]/table/tbody/tr[2]/td[2]/strong').get()
        address = response.xpath(
            '//*[@id="masterForm"]/div[3]/div/div/main/div/div[10]/div[1]/table/tbody/tr[14]/td[2]/strong').get()
        # company_status = response.xpath('').get()
        # Tạo một dictionary chứa thông tin đã trích xuất
        company_info = {
            "Company Name": company_name,
            "Tax Code": tax_code,
            "Address": address,
            # "Status": company_status
        }
        self.uk_suppliers.append(company_info)
            # Trả về dữ liệu cho việc lưu trữ hoặc xử lý tiếp theo
        yield company_info
            # Convert the list of suppliers to a pandas DataFrame
        # df = pd.DataFrame(self.uk_suppliers)
        # df.to_excel("suppliers.xlsx")
        # self.log(f'Data saved to "suppliers.xlsx"')


process = CrawlerProcess()
process.crawl(WebUsSpider)
process.start()
