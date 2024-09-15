import akshare as ak
# 宁德时代
symbol = "300750"
# 贵州茅台 600519
symbol = "600519"
stock_news = ak.stock_news_em(symbol=symbol)
stock_news.shape
stock_news[:15]
news = "新闻列表：\n"
for i in range(15):
    title = stock_news.iloc[i,1]
    date = stock_news.iloc[i,3]
    content=stock_news.iloc[i,2]
    news = news + f"-  新闻发布日期：{date}。新闻标题：{title} \n"
    #news = news + content
print(news)