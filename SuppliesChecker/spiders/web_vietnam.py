import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
class WebVietnamSpider(scrapy.Spider):
    name = "web-vietnam"
    allowed_domains = ["masothue.com", 
                       #"infodoanhnghiep.com"
                       ]
    start_urls = [
        "https://masothue.com/2901643377-doanh-nghiep-tu-nhan-hoang-sy-linh",
        #"https://infodoanhnghiep.com/tim-kiem/auto/5900992282/"
    ]
    companies = []
    def parse(self, response):
        if 'masothue.com' in response.url: 
            scrapy.FormRequest.from_response(
                response,
                formdata={'search': '5900992282'},
                callback=self.parse_masothue
            )
            yield from self.parse_masothue(response)           
        # elif 'infodoanhnghiep.com' in response.url:
        #     yield from self.parse_infodoanhnghiep(response)

    def parse_masothue(self, response):
        # Trích xuất thông tin cần thiết từ response
        company_name = response.xpath(
            '//*[@id="main"]/section[1]/div/table[1]/thead/tr/th/span/text()').get()
        tax_code = response.xpath(
            '//td[@itemprop="taxID"]/span[@class="copy"]/text()').get()
        address = response.xpath(
            '//td[@itemprop="address"]/span[@class="copy"]/text()').get()
        company_status = response.xpath(
            '//tbody/tr/td/i[@class="fa fa-info"]/../../td[2]/a/text()').get()
        # Tạo một dictionary chứa thông tin đã trích xuất
        company_info = {
            "Company Name": company_name,
            "Tax Code": tax_code,
            "Address": address,
            "Status": company_status
        }
        
        # Trả về dữ liệu cho việc lưu trữ hoặc xử lý tiếp theo
        yield company_info
        self.companies.append(company_info)
        # Convert the list of sippliers to a pandas DataFrame
        df = pd.DataFrame(self.companies)
        df.to_excel("suppliers.xlsx")
        self.log(f'Data saved to "suppliers.xlsx"')
process = CrawlerProcess()
process.crawl(WebVietnamSpider)
process.start()

   
