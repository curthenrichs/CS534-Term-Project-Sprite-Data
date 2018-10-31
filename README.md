# Sprite-Data
Repository for all data pertaining to GAN project

## Basic Processing
Current workflow for the data collection system is to provide a sprite-sheet, then apply process.py to generate a set of individual sprite images

process.py will perform the following steps
1) extract sprites from sprite-sheet. Currently this relies on a fixed-grid without separation pixels
2) normalize image to RGBA. Also will crop by center or pad with zero.
3) sort images by shape. Note that a single sprite-sheet will add to a single folder. Reason this is useful is that it can automatically, place the different sprite shapes into appropriate bins between sprite-sheets.

## Other Processing Activities
Individual scripts can be run to get the specific feature needed. (For example if only interested in normalizing sprites)

## Use for GAN
Provided in packaged directory is the compressed dataset generated from finalized directory. Download these files or clone the repository for use in training the GAN.

Alternatively, the project website provides links to cached versions of the dataset. This version may not be up to date.

## <Future> Classifier Neural Net
TODO

## Todo Checklist
* collect more data and further classify the data currently available.
* develop a recursive normalize that copies the directory structure.
* using the manually separated data, train a classifier for easier processing of new data.

## Acknowledgements
All sprite-sheets / datasets aggregated are used for this project in an academic setting. All sources must be credited below as either requested by the source or with an appropriate format. Any reference will include a link to the original. Note that any sprite data stored in this repository should not be considered the original source. Nor does this repository claim ownership of the sprite data. Data contributions should come from sources with licenses that provide for non-commercial, academic use.

* Henrique Laxarini (7Soul1). 496 Pixel Art Icons for Medieval/Fantasy RPG. License: CC0 - Public Domain. Online: https://opengameart.org/content/496-pixel-art-icons-for-medievalfantasy-rpg
* MedicineStorm. Dungeon Crawl 32x32 Tiles Supplemental. License: CC0 - Public Domain. Online: https://opengameart.org/content/dungeon-crawl-32x32-tiles-supplemental
* David E. Gervais. Roguelike Tiles (Large Collection). License: CC-BY 3.0. Online: https://opengameart.org/content/roguelike-tiles-large-collection
