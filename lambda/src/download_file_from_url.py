################################################################################
# Script to download a given file from endpoint to specific local path. It also
# handles the logging for "status" of the download in the meantime.
################################################################################

# Built-in dependencies
from urllib import request
import time
import os

def download_file_from_url(download_file_url, output_folder):
    """
    Function to download a file from a given URL and saves it to desired folder.
    :return: output_file_path (string of the output path of the file)
    """
    filename = download_file_url.split('/')[-1]
    output_file_path = "{}/{}".format(output_folder, filename)

    # Check wether directory exists or not
    dir_exists = os.path.exists(output_folder)
    if not dir_exists:
        print("Creating the folder {}".format(output_folder))
        os.makedirs(output_folder)

    start = time.time()
    print("Starting file download from URL: {} ...".format(download_file_url))
    response = request.urlretrieve(download_file_url, output_file_path)
    print("Total time to download file was: {} seconds".format(time.time() - start))
    print("Output path of the downloaded file is: {}".format(output_file_path))

    return output_file_path


## ONLY FOR LOCAL TESTS! (OWN COMPUTER VALIDATIONS)
if __name__ == "__main__":
    # TESTS
    download_file_url = "https://instagram.com/favicon.ico"
    output_folder = "./tmp"
    print(download_file_from_url(download_file_url, output_folder))
