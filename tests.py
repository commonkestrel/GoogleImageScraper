import GoogleImageScraper
import time

startTime = time.time()

paths = GoogleImageScraper.download(query='cats', limit=100, arguments={'verbose': True})

endTime = time.time()
execTime = round(endTime-startTime, 3)
print(execTime)