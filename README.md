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
* allow separation / gap pixels in sprite-sheet for extraction
* manually sort sprites generated into classes useful for training
* compress sprites for training, use raw link to get access
* using the manually separated data, train a classifier for new data
