# photo-sorting

This repository contains `repeatedPhotoSorter.py`, a Python script designed to automate the sorting of a large collection of photos into albums based on their creation year. The script is particularly useful for organizing photos that are not already sorted into specific albums.

## Overview

The script processes an unsorted photo directory, comparing each photo against those already sorted into albums in a separate directory. If a photo hasn't been sorted yet, it's automatically placed into a new album named after its creation year.

## Features

- **Automated Sorting:** Automatically sorts unsorted photos into new albums based on the year of creation.
- **Duplication Check:** Ensures that photos already sorted into albums are not duplicated.
- **Progress Tracking:** Displays ongoing progress, number of photos copied, elapsed time, and estimated time of completion.

## Prerequisites

- Python 3.x

## Usage

1. Set the `unsorted_photos_path` variable to the directory containing the unsorted photos.
2. Set the `sorted_photos_path` variable to the directory where sorted albums are or will be located.
3. Run the script:

    ```bash
    python repeatedPhotoSorter.py
    ```

## Script Details

- **unsorted_photos_path:** Path to the directory containing unsorted photos.
- **sorted_photos_path:** Path to the directory where sorted albums are stored.
- **count_items:** Counts directories or files in a given path.
- **main:** The main function orchestrating the sorting process.

## How It Works

- The script iterates over each photo in the unsorted directory.
- For each photo, it checks if it exists in any of the sorted albums.
- If not found in any album, the photo's creation year is determined.
- The photo is then copied to an album named after its creation year, creating a new album if necessary.

## Note

This script is designed for personal use and may need modifications to suit different directory structures or sorting criteria.