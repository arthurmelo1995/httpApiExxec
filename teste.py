import unittest
from scrapy.http import HtmlResponse, Request
from scrapy.spiders import Spider
from your_module_name import WikiSpider  # Substitua 'your_module_name' pelo nome do módulo onde seu spider está definido

class WikiSpiderTest(unittest.TestCase):

    def setUp(self):
        self.spider = WikiSpider()

    def test_parse(self):
        html_content = '''
            <html>
                <body>
                    <h1 id="firstHeading">Web scraping</h1>
                    <div class="mw-parser-output">
                        <a href="/wiki/Data_extraction">Data extraction</a>
                        <a href="/wiki/Extraction">Extraction</a>
                    </div>
                </body>
            </html>
        '''
        request = Request(url='https://en.wikipedia.org/wiki/Web_scraping')
        response = HtmlResponse(url='https://en.wikipedia.org/wiki/Web_scraping', body=html_content, encoding='utf-8', request=request)
        results = list(self.spider.parse(response))

        self.assertEqual(results[0].url, 'https://en.wikipedia.org/wiki/Data_extraction')
        self.assertEqual(results[1].url, 'https://en.wikipedia.org/wiki/Extraction')

    def test_parse_secondary(self):
        html_content = '''
            <html>
                <body>
                    <h1 id="firstHeading">Data extraction</h1>
                </body>
            </html>
        '''
        request = Request(url='https://en.wikipedia.org/wiki/Data_extraction')
        response = HtmlResponse(url='https://en.wikipedia.org/wiki/Data_extraction', body=html_content, encoding='utf-8', request=request)
        self.spider.parse_secondary(response)

if __name__ == '__main__':
    unittest.main()
