# Sprite-Data
Repository for all data pertaining to GAN project

## Basic Processing
Current workflow for the data collection system is to provide a sprite-sheet,
then apply process.py to generate a set of individual sprite images

process.py will perform the following steps
1) extract sprites from sprite-sheet. Currently this relies on a fixed-grid
without separation pixels
2) normalize image to RGBA. Also will crop by center or pad with zero.
3) sort images by shape. Note that a single sprite-sheet will add to a single
folder. Reason this is useful is that it can automatically, place the different
sprite shapes into appropriate bins between sprite-sheets.

## Use for GAN
TODO

## <Future> Classifier Neural Net
TODO

## Todo Checklist
* manually sort sprites generated into classes useful for training
* compress sprites for training, use raw link to get access. The data file should be in a form that is easily extracted for numpy.
* using the manually separated data, train a classifier for new data.

## Acknowledgements
All sprite-sheets / datasets aggregated are used for this project in an academic setting. All sources must be credited below as either requested by the source or with an appropriate format. Any reference will include a link to the original. Note that any sprite data stored in this repository should not be considered the original source. Nor does this repository claim ownership of the sprite data. Data contributions should come from sources with licenses that provide for non-commercial, academic use.

* Henrique Laxarini (7Soul1). 496 Pixel Art Icons for Medieval/Fantasy RPG. License: CC0 - Public Domain. Online: https://opengameart.org/content/496-pixel-art-icons-for-medievalfantasy-rpg
* MedicineStorm. Dungeon Crawl 32x32 Tiles Supplemental. License: CC0 - Public Domain. Online: https://opengameart.org/content/dungeon-crawl-32x32-tiles-supplemental
* David E. Gervais. Roguelike Tiles (Large Collection). License: CC-BY 3.0. Online: https://opengameart.org/content/roguelike-tiles-large-collection
