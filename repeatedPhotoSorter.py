"""
Basic script used to sort photos
I had a dump of roughly 15,000 photos in a single directory
I had hand sorted the majority into albums
There were roughly 4000 left that did not belong in a specific album
I wanted these to be automatically sorted into new albums, grouped by year
This program checks every photo in the original folder to see if it has already been sorted into any album
in the destination folder
If it hasn't, it is copied across to a new album, based on its creation date
"""


import os
import time
import shutil


def get_directory_attributes(directory_path):
	return next(os.walk(directory_path))


def count_items(directory_path, type):
	path, dirs, files = next(os.walk(directory_path))

	if type == "dir":
		return len(dirs)
	elif type == "files":
		return len(files)


def main():
	unsorted_photos_path = "F:\OneDrive - Imperial College London\PhotoLibrary"
	sorted_photos_path = "F:\Photos"

	iteration = 0
	copied_photos_count = 0

	n_albums = count_items(sorted_photos_path, "dir")
	n_photos = count_items(unsorted_photos_path, "files")

	unsorted_path, unsorted_dirs, unsorted_files = get_directory_attributes(unsorted_photos_path)
	sorted_path, original_sorted_dirs, sorted_files = get_directory_attributes(sorted_photos_path)

	t1 = time.perf_counter()

	for item in unsorted_files:
		iteration += 1
		check_count = 0
		for i in range(0, n_albums):

			current_album = original_sorted_dirs[i]
			new_file_to_check = os.path.join(sorted_photos_path, os.path.join(current_album, item))

			if not (os.path.isfile(new_file_to_check)):
				check_count += 1

		if check_count == n_albums:

			time_since_epoch = os.path.getmtime(os.path.join(unsorted_path, item))
			local_time = time.ctime(time_since_epoch)
			year = local_time[-4:]

			sorted_path, sorted_dirs, sorted_files = get_directory_attributes(sorted_photos_path)

			if year + "_misc" in sorted_dirs:
				pass
			else:
				os.mkdir(os.path.join(sorted_photos_path, year + "_misc"))

			copied_photos_count += 1

			shutil.copy2(os.path.join(unsorted_path, item), os.path.join(sorted_photos_path, os.path.join(year + "_misc", item)))

			t2 = time.perf_counter()
			elapsed_time = round(t2 - t1, 2)
			ETA = round((elapsed_time * n_photos) / iteration, 2)

			print("Progress: " + str(iteration) + "/" + str(n_photos) + " <> Copied: " + str(copied_photos_count)
				+ " <> Time: " + str(elapsed_time) + " <> ETA: " + str(ETA) + " <> Remaining: "
				+ str(round(ETA - elapsed_time, 2)))


if __name__ == "__main__":
	main()
