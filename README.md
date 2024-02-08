# art_data
Dataset of 32,435 historically significant paintings: img, metadata

Original Dataset is from: https://www.wga.hu/index_database.html

Scraping the images and combining with the given metadata.

ISSUES: Allign original IDX with image url ---> FIXED

Bad indexes are: [11578, 11583]. Filter these out when creating zipped dataset if need be.