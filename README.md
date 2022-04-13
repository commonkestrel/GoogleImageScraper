# Google Image Scraper

This is a library for retrieving and downloading images from Google Images.  
It uses an input query and arguments to search and retrive image objects.

# Arguments
There is one required argument and two arguments in both of the main functions:

**query:** Either a string or list containing the keywords to search for. If the query is a string, it will be separated into different keywords by spaces.  
***Accepted types:*** *str, list*

**limit:** The amount of images to search for. Cannot be greater then 100 currently. *\*Defaults to 1\**  
***Accepted types:*** *int*

**arguments:** This is a dictionary containing many optional values, all of which will be listed here. They are split into two categories: *Search arguments* and *Download arguments*:    
***Accepted types:*** *dict*

## Download arguments

**download_format:** Specifies a file extension to download all images as. Must be a valid image file extension recognized by *PIL*.

**directory:** This specifies the directory name to download the images to. This will automatically be created in the directory the function is called in, unless the directory already exists or **path** is specified. 

**path:** This specifies the path to create the download directory in.  

## Search Arguments

**color:** Filter images by the dominant color.  
***Accepted Values:*** ('red', 'orange', 'yellow', 'green', 'teal', 'blue', 'purple', 'pink', 'white', 'gray', 'black', 'brown')

**color_type:** Filter images by the color type, full color, grayscale, or transparent.  
***Accepted Values:*** ('full', 'grayscale', 'transparent')

**license:** Filter images by the usage license.  
***Accepted Values:*** ('creative_commons', 'other_licenses')

**type:** Filters by the type of images to search for. \**Not to be confused with format*\*  
***Accepted Values:*** ('face', 'photo', 'clipart', 'lineart', 'gif')

**time:** Only finds images posted in the time specified.  
***Accepted Values:*** ('past_day', 'past_week', 'past_month', 'past_year')

**aspect_ratio** Specifies the aspect ratio of the images.  
***Accepted Values:*** ('tall', 'square', 'wide', 'panoramic')

**search_format:** Filters out images that are not a specified format. If you would like to simply download images as a specific format, use the 'download_format' argument instead.  
***Accepted Values:*** ('jpg', 'gif', 'png', 'bmp', 'svg', 'webp', 'ico', 'raw')

# Usage
There are three available functions, **download**, **urls**, and **image_objects:**

## download:

```python
import GoogleImageScraper

images = GoogleImageScraper(query, limit, arguments)
```
This will download images based on the arguments.
___
The returned values will follow this format:
```python
{'images': [Image List], 'errors': Number of Errors}
```
The images in the list of images will follow a particular format as well:
```python
{'path': Image Path, 'url': Image Url}
```

## urls:
```python
import GoogleImageScraper

urls = GoogleImageScraper.urls(query, limit, arguments)
```

This function simply returns a list of image urls from the search terms.

___

## image_objects:
This function is a little more niche, but it may be useful to some people. Instead of returning a list of image urls like with the **urls** function, it returns a list of image objects containing useful data, structured like so:

```python
{'url': Image url, 'thumbnail': Url of image thumbnail, 'source_url': The webpage the image was found on, 'source': The base url of the source}
```
The usage is similar to the previous functions:
```python
import GoogleImageScraper

image_objects = GoogleImageScraper.image_objects(query, limit, arguments)
```

# Examples:
A few real examples are listed here:
## urls:
```python
import GoogleImageScraper
urls = GoogleImageScraper.urls(query='cats', limit=10, arguments={'color': 'black'})
```
Result:
```python
['https://www.rd.com/wp-content/uploads/2021/01/GettyImages-1175550351.jpg', 
'https://www.history.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTg0NTEzNzgyNTMyNDE2OTk5/black-cat-gettyimages-901574784.jpg', 
'https://www.thesprucepets.com/thmb/kF3_dQW_JT1ClMQDlISxq3BgeT4=/6843x5132/smart/filters:no_upscale()/facts-about-black-cats-554102-hero-7281a22d75584d448290c359780c2ead.jpg', 
'https://i.guim.co.uk/img/media/c5e73ed8e8325d7e79babf8f1ebbd9adc0d95409/2_5_1754_1053/master/1754.jpg?width=465&quality=45&auto=format&fit=max&dpr=2&s=065f279099ded1062688e357b155dc29', 
'https://cdn.cnn.com/cnnnext/dam/assets/141030105303-kiki-irpt.jpg', 
'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F34%2F2021%2F09%2F27%2Fblack-cat-kitchen-rug-getty-0921-2000.jpg', 
'https://www.gannett-cdn.com/presto/2021/10/28/USAT/1bf79c6a-5d88-4e64-b398-c40418a79829-XXX_iStock_000017680551Large.jpg',
'https://cdn.sanity.io/images/0vv8moc6/dvm360/f28cc9b680aed62edd018ce47a5cbb96c4f78f3b-4860x3024.jpg', 
'https://vbspca.com/wp-content/uploads/2019/10/Image-e1570199876255.jpeg', 
'https://ichef.bbci.co.uk/news/976/cpsprodpb/AECE/production/_99805744_gettyimages-625757214.jpg']
```

---
## download:
```python
import GoogleImageScraper
images = GoogleImageScraper.download(query='dogs', limit=10, arguments={'color':'brown', 'download_format': 'png'})
```
Result:
```python
{'images':[{'path': '<path>\\images\\dogs-0.png', 'url': 'https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-800x825.jpg'}, 
{'path': '<path>\\images\\dogs-1.png', 'url': 'https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_3x4.jpg'}, 
{'path': '<path>\\images\\dogs-2.png', 'url': 'https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_2x1.jpg'}, 
{'path': '<path>\\images\\dogs-3.png', 'url': 'https://static01.nyt.com/images/2019/06/17/science/17DOGS/17DOGS-facebookJumbo.jpg?year=2019&h=550&w=1050&s=1201a06f5b085be8367096c545bffccc2ddca33ca3dcf57236468efcf911d023&k=ZQJBKqZ0VN'}, 
{'path': '<path>\\images\\dogs-4.png', 'url': 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg?crop=0.672xw:1.00xh;0.166xw,0&resize=640:*'}, 
{'path': '<path>\\images\\dogs-5.png', 'url': 'https://kb.rspca.org.au/wp-content/uploads/2018/11/golder-retriever-puppy.jpeg'}, 
{'path': '<path>\\images\\dogs-6.png', 'url': 'https://d.newsweek.com/en/full/1979380/dog-running-through-autumn-leaves.jpg'}, 
{'path': '<path>\\images\\dogs-7.png', 'url': 'https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2012/11/dog-how-to-select-your-new-best-friend-thinkstock99062463.jpg?bust=1513996287'}, 
{'path': '<path>\\images\\dogs-8.png', 'url': 'https://www.thesprucepets.com/thmb/KAgiRA9eovA6l_xJz-Dz6Q3axHU=/1414x1414/smart/filters:no_upscale()/GettyImages-1201198563-fe6114423c714faa8cb1418a9b98e192.jpg'}, 
{'path': '<path>\\images\\dogs-9.png', 'url': 'https://i.guim.co.uk/img/media/684c9d087dab923db1ce4057903f03293b07deac/205_132_1915_1150/master/1915.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=14a95b5026c1567b823629ba35c40aa0'}], 'errors': 0}
```

---

## image_objects:

```python
import GoogleImageScraper
objects = GoogleImageScraper.image_objects(query='birds', limit=10, arguments={'color':'yellow'})
```
Results:
```python
[{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwDI5y3_n2rwFQLZKrBXs5VL_J38zlZVvdZAooD8F8d7lY8ZA9iLEb1-AoBBWpGftpdoc&usqp=CAU', 'url': 'https://www.sfvaudubon.org/wp-content/uploads/2020/03/YEWAcrop.jpg', 'source_url': 'https://www.sfvaudubon.org/sfv-backyard-bird-identification/', 'source': 'sfvaudubon.org'}, 
{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqLCldfnxEi3J7fEVaLyW5oLSdzZwb4R15gXtbLs9oUw6SIDuzFChRsnUpsPp4PgQ5BhY&usqp=CAU', 'url': 'https://www.allaboutbirds.org/guide/assets/photo/297046671-480px.jpg', 'source_url': 'https://www.allaboutbirds.org/guide/Yellow_Warbler/id', 'source': 'allaboutbirds.org'}, 
{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1k5IhGCAPgU468tyPrgkuY9WC3T83zRxzFrTOOUs0OL_kanPG8VPKXV3euijAlzW9AsE&usqp=CAU', 'url': 'https://ca.audubon.org/sites/default/files/styles/article_teaser/public/yellowwarbler_peter_latourrette.jpg?itok=PFRtxcGN', 'source_url': 'https://ca.audubon.org/birds-0', 'source': 'ca.audubon.org'}, 
{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVY-K2RIFC-utN12LFlVcq1CtrlzqcmqpZtcQSWOZQMM_3rLDp8ZGSlAq-68U-F6qyBV4&usqp=CAU', 'url': 'https://www.allaboutbirds.org/guide/assets/photo/297046811-480px.jpg', 'source_url': 'https://www.allaboutbirds.org/guide/Yellow_Warbler/id', 'source': 'allaboutbirds.org'}, 
{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSI_PXGH6G-O1c6Rh5wI9WdKK4HEU0kjycO6uknyoWmDdGULbsiztifo_05CEZBD6Rx3w&usqp=CAU', 'url': 'https://wildbirdrevolution.org/wp-content/uploads/2020/03/Black-hooded-oriole-Oriolus-xanthornus-Vazhani-Kerala-by-Vidjit-Vijaysanker.jpg', 'source_url': 'https://wildbirdrevolution.org/top-25-birds-of-the-week-yellow-feathers/', 'source': 'wildbirdrevolution.org'}, 
{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRza5NoqQ99BwgDyddU2R_1ld190YL75ZIWJ6PUaGyGTQWEVOiBmrbAqzFSdmUQGfrBpJY&usqp=CAU', 'url': 'https://images.unsplash.com/photo-1618098750285-9402745c67e7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8eWVsbG93JTIwYmlyZHxlbnwwfHwwfHw%3D&w=1000&q=80', 'source_url': 'https://unsplash.com/s/photos/yellow-bird', 'source': 'unsplash.com'}, 
{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW-0-Z8T52RQC8n4Sy5LYRPbhanZA1NZG6vAOFxBPVZy0FT5ArqE03auGcqdKb9ZxZVqU&usqp=CAU', 'url': 'https://travisaudubon.org/home/wp-content/uploads/2018/02/APA-2017_Yellow_Warbler_P1_4700_2_Sheen_Watkins_KK-800x600.jpg', 'source_url': 'https://travisaudubon.org/tx-backyard-birds-galleries', 'source': 'travisaudubon.org'}, 
{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTP0lFA-BPPAABhRwdugJKGdr_wnAHIcJLPAJdH6JBH2tKCR4pmJXH3wPXjgUh3IhV9op8&usqp=CAU', 'url': 'https://www.thevetexpert.com/wp-content/uploads/2021/01/Small-Yellow-Birds.jpg', 'source_url': 'https://www.thevetexpert.com/12-most-famous-small-yellow-birds-you-should-know-as-a-bird-lover/', 'source': 'thevetexpert.com'}, 
{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu9LZhIV7nrmPvIiYRfXPjKdP9y6fqURdVO5Jcz9zyI9LlMu0nehtPVZLwhVlyHR9GKlM&usqp=CAU', 'url': 'https://nc.audubon.org/sites/default/files/styles/hero_mobile/public/aud_apa-2018_prothonotary-warbler_a1-6856-3_kk_photo-michael-witt_1.jpg?itok=zcoDcNw9', 'source_url': 'https://nc.audubon.org/2020-summit', 'source': 'nc.audubon.org'}, 
{'thumbnail': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_H6mHY3G5C_oZeO5pMyPObuqDsfPM6W8L6xlYlsPTaoXYF8dricV1datP20nHPG5EPWY&usqp=CAU', 'url': 'https://www.allaboutbirds.org/guide/assets/og/75216491-1200px.jpg', 'source_url': 'https://www.allaboutbirds.org/guide/Yellow_Warbler/id', 'source': 'allaboutbirds.org'}]
```