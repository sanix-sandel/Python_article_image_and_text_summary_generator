from newspaper import Article

url="https://arstechnica.com/science/2018/06/first-space-then-auto-now-elon-musk-quietly-tinkers-with-education/"
article=Article(url)

if __name__=='__main__':
    article.download()
    article.parse()
    print(article.images)