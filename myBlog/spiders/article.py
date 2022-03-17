import scrapy
import requests
from myBlog.items import Article

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['blog.csdn.net']
    # just as a beginner(useless)
    start_urls = ['https://blog.csdn.net']

    # 这里无法产生联动
    # 所以无奈，只能先获取全部article的url
    def get_all_my_articles(self):
        article_urls = []
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'referer': 'https://bridge-killer.blog.csdn.net/'
        }
        menu_url = "https://blog.csdn.net/community/home-api/v1/get-business-list?page={}&size=20&businessType=lately&noMore=false&username=weixin_40986490"
        # 从debug中可以发现只能去到44页
        for page in range(1, 44):
            r = requests.get(menu_url.format(page), headers = header)
            for article in r.json()['data']['list']:
                article_urls.append(article['url'])

        return article_urls

    def parse(self, response):
        article_urls = self.get_all_my_articles()
        for article_url in article_urls:
            yield response.follow(article_url, self.parse_article)

    def parse_article(self, response):
        article = Article()
        article['title'] = response.css('#articleContentId::text').get()
        article['read'] = response.css('.read-count::text').get()
        article['like'] = response.css('#spanCount::text').get().strip()
        article['review'] = response.css('li.tool-item:nth-child(3) > a:nth-child(1) > span:nth-child(2)::text').get().strip()
        article['collect'] = response.css('#get-collection::text').get().strip()

        yield article

