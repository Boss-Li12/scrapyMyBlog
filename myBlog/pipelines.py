# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class MyblogPipeline:
    def process_item(self, item, spider):
        # we just need that article
        # which being read more than 200
        if item.get('read'):
            # 把 item 的 score 变成整数
            item['read'] = int(item['read'])

            if item['read'] < 200:
                raise DropItem('去掉200阅读量以下的文章')

        return item
