from GoogleImageScraper import ImageScraper

search = ImageScraper()

urls = search.urls(query='cats', limit=200, arguments={'color': 'pink'})
print(urls)

paths = search.download(query='cats', limit=21, arguments={'color': 'black', 'directory':'testsImages', 'download_format': 'png', 'search_format': 'jpg'})
print(paths)
