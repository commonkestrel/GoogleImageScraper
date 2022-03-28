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

# Examples
There are two main functions included: **urls** and **download:**

## Download:

```python
from GoogleImageScraper import GoogleImageScraper

scraper = GoogleImageScraper()
images = scraper.download(query, limit, arguments)
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

## Urls:
```python
from GoogleImageScraper import GoogleImageScraper

scraper = GoogleImageScraper()
urls = scraper.urls(query, limit, arguments)
```

This function simply returns a list of image urls from the search terms     .

___

## Extra

There is one more function that may be of use to some people, but it is a bit more complicated, and there is no limit argument.

```python
from GoogleImageScraper import GoogleImageScraper
scraper = GoogleImageScraper()

builtUrl = scraper.build_url(query, arguments)    
searchData = scraper.get_html(builtUrl)

imageObjects = scraper.get_images(searchData)
```

This will return a list of image objects, stuctured like so:

```python
{'url': Image url, 'thumbnail': Url of image thumbnail, 'source_url': The webpage the image was found on, 'source': The base url of the source}
```
