from urllib.request import urlopen, Request
import json
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from os import getcwd, mkdir
from os.path import exists

class image_scraper:
        def __init__(self):
            self.path = getcwd()

        def urls(self, query=None, limit=100, arguments=None):
            if limit > 100:
                raise Exception('Limit must be under 100')
            
            builtUrl = self.build_url(query, arguments)    
            searchData = self.get_html(builtUrl)
            
            imageObjects = self.get_images(searchData)
            
            if imageObjects:
                urls = []
                for image in range(limit):
                    urls.append(imageObjects[image]['url'])
                            
                return urls
            else:
                return None
                
        def download(self, query=None, limit=1, arguments=None):
            if limit > 100:
                raise Exception('Limit must be under 100')
            
            urls = self.urls(query, arguments=arguments)
                
            if arguments and 'path' in arguments:
                path = arguments['path']
            else:
                path = self.path
            if arguments and 'directory' in arguments:
                currentPath = f"{path}/{arguments['directory']}"
            else:
                currentPath = f"{path}/images"
            try:
                mkdir(currentPath)
            except FileExistsError:
                pass
                
            if type(query) == str:
                    query = query.split(' ')
            prefix = 0
            images = {'images':[]}
            errors = 0
            item = 0
            for i in range(limit):
                skip = False
                url = urls[item]
                
                img = self.open_image(url)
                while img == 1:
                    item += 1
                    try:
                        url = urls[item]
                    except IndexError:
                        errors += 1
                        skip = True
                
                if skip:
                    continue
                
                if arguments and 'download_format' in arguments:
                    downloadPath = currentPath + f"/{'-'.join(query)}-{prefix}.{arguments['download_format'].lower()}"
                else:
                    downloadPath = currentPath + f"/{'-'.join(query)}-{prefix}.{img.format.lower()}"
                while exists(downloadPath):
                    prefix +=1
                    downloadPath = currentPath + f"/{'-'.join(query)}-{prefix}.{img.format.lower()}"
                if arguments and 'download_format' in arguments:
                    img.save(downloadPath, arguments['download_format'].upper().replace('JPG', 'JPEG'))
                else:
                    img.save(downloadPath)
                images['images'].append({'path': downloadPath, 'url': url})
                prefix += 1
                item += 1
            
            images['errors'] = errors
            return images
        
        def open_image(self, url):
            headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
            req=Request(url,None,headers)
            response = urlopen(req)
            try:
                img = Image.open(BytesIO(response.read()))
                return img
            except UnidentifiedImageError:
                return 1
        
        def build_url(self, query, arguments={}):
            
            parameterList = ['search_format',  'color', 'color_type', 'license', 'image_type', 'time', 'aspect_ratio']
            
            parameters = {'color': {'red': 'ic:specific%2Cisc:red', 'orange': 'ic:specific%2Cisc:orange', 'yellow': 'ic:specific%2Cisc:yellow', 'green': 'ic:specific%2Cisc:green', 'teal': 'ic:specific%2Cisc:teel', 'blue': 'ic:specific%2Cisc:blue', 'purple': 'ic:specific%2Cisc:purple', 'pink': 'ic:specific%2Cisc:pink', 'white': 'ic:specific%2Cisc:white', 'gray': 'ic:specific%2Cisc:gray', 'black': 'ic:specific%2Cisc:black', 'brown': 'ic:specific%2Cisc:brown'},
                'color_type': {'color': 'ic:full', 'grayscale': 'ic:gray', 'transparent': 'ic:trans'},
                'license': {'creative_commons': 'il:cl', 'other_licenses': 'il:ol'},
                'type': {'face': 'itp:face', 'photo': 'itp:photo', 'clipart': 'itp:clipart','lineart': 'itp:lineart', 'gif': 'itp:animated'},
                'time': {'past_day': 'qdr:d', 'past_week': 'qdr:w', 'past_month': 'qdr:m','past_year':'qdr:y'},
                'aspect_ratio': {'tall': 'iar:t', 'square': 'iar:s', 'wide': 'iar:w', 'panoramic': 'iar:xw'},
                'search_format': {'jpg': 'ift:jpg', 'gif': 'ift:gif', 'png': 'ift:png', 'bmp': 'ift:bmp', 'svg': 'ift:svg', 'webp': 'webp', 'ico': 'ift:ico', 'raw': 'ift:craw'}}

            if not arguments:
                arguments = {}
            
            for param in parameterList:
                if param not in arguments:
                    arguments[param] = None
            
            if not query:
                raise Exception("'query' is a required argument")
            if type(query) == str:
                query = query.split(' ')
            joinedQuery = '%20'.join(query)
            
            builtArgs = '&tbs='
            counter = 0
            
            for param in parameterList:
                if arguments[param]:
                    try:
                        item = parameters[param][arguments[param]]
                        if counter != 0:
                            builtArgs += ','
                        builtArgs += item
                        counter += 1 
                    except NameError:
                        raise NameError(f"Invalid argument for {param}! Valid arguments are {parameters[param].values}")

            baseUrl = 'https://www.google.com/search?tbm=isch&q='
            
            if counter != 0:
                return baseUrl + joinedQuery + builtArgs
            else:
                return baseUrl + joinedQuery
            
        def get_images(self, page):
            startChar = page.find("AF_initDataCallback({key: \\'ds:1\\'") + 54
            endChar = page.find('</script>', startChar) - 20
            
            pageJson = page[startChar:endChar] 
            pageJson = json.loads(pageJson.encode('utf-8').decode('unicode_escape'))

            imageObjects = pageJson[31][0][12][2]
            
            images = []
            for imageObject in imageObjects:
                if imageObject[1]:
                    image = {}
                    image['thumbnail'] = imageObject[1][2][0]
                    image['url'] = imageObject[1][3][0]
                    sourceInfo = imageObject[1][9]['2003']
                    image['source_url'] = sourceInfo[2]
                    image['source'] = sourceInfo[17]
                    images.append(image)
            return images
        
        def get_html(self, url):
            headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
            req = Request(url, headers=headers)
            searchPage = urlopen(req)
            searchData = str(searchPage.read())
            return searchData
            
if __name__ == '__main__':
        search = image_scraper()
        images = search.download(query='cats', limit=40, arguments={'download_format': 'png', 'color': 'pink'})
        print(images)
