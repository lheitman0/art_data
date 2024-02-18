# Painting Dataset
A dataset of 32,435 historically significant paintings, including images and metadata.
The folder of images is currently not included in this repo due to size limitations. It is hosted on Drive.

## Source

The original dataset was obtained from the Web Gallery of Art:
[https://www.wga.hu/index_database.html](https://www.wga.hu/index_database.html)

## Dataset Collection Process

The image dataset compilation involved the following key steps:

1. **URL Analysis**: Evaluated patterns within the base dataset's image URLs to understand access mechanisms.
2. **URL Modification**: Altered URLs for direct scraping, ensuring seamless access to image files.
3. **Image Downloading**: Utilized a scraping script to download images and metadata from the adjusted URLs, automating the collection process.

## Issues & Resolutions

- **IDX Alignment**: Ensured alignment between original indices and image URLs. **Status**: FIXED.
- **Image Quality**: Noted concerns regarding the potential insufficiency of image quality for certain analyses.

### Known Bad Indices

The following indices are known to be problematic: [11578, 11583]. It's recommended to exclude these when creating a zipped version of the dataset for analysis or model training.

## Exploring Other Datasets
### EDA of PNAS and Wikiart dataset
- **PNAS Dataset**: Only Landscapes --> (rows, columns): (14912, 24)
[https://www.pnas.org/doi/10.1073/pnas.2011927117?doi=10.1073%2Fpnas.2011927117](https://www.pnas.org/doi/10.1073/pnas.2011927117?doi=10.1073%2Fpnas.2011927117)
- **Wikiart Dataset**: Wide ranging styles and genres --> (rows, columns): (81444, 3)
[https://huggingface.co/datasets/huggan/wikiart](https://huggingface.co/datasets/huggan/wikiart)

