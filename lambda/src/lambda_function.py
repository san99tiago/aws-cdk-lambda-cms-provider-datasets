# Built-in dependencies
import os
import datetime
import glob
import boto3

# Own dependencies
import download_file_from_url
import s3_helpers
import send_emails_ses

################################################################################
# GLOBAL VARIABLES TO CONFIGURE SOLUTION
# URL SITE CONFIGURATIONS
BASE_URL = os.environ.get("BASE_URL")  # Example --> "https://data.cms.gov/provider-data/sites/default/files"

SCRAPPER_CONFIGURATION = {
    "dialysis-facilities": [
        "{}/archive/Dialysis%20facilities/current/dialysis_facilities_current_data.zip".format(BASE_URL),
        "{}/data_dictionaries/dialysis/DF_Data_Dictionary.pdf".format(BASE_URL),
    ],
    "doctors-and-clinicians": [
        "{}/archive/Doctors%20and%20clinicians/current/doctors_and_clinicians_current_data.zip".format(BASE_URL),
        "{}/data_dictionaries/physician/DOC_Data_Dictionary.pdf".format(BASE_URL),
    ],
    "home-health-service": [
        "{}/archive/Home%20health%20services/current/home_health_services_current_data.zip".format(BASE_URL),
        "{}/data_dictionaries/home_health/HHS_Data_Dictionary.pdf".format(BASE_URL),
    ],
    "hospice-care": [
        "{}/archive/Hospice%20care/current/hospice_care_current_data.zip".format(BASE_URL),
        "{}/data_dictionaries/hospice/HOSPICE_Data_Dictionary.pdf".format(BASE_URL),
    ],
    "hospital-data": [
        "{}/archive/Hospitals/current/hospitals_current_data.zip".format(BASE_URL),
        "{}/data_dictionaries/hospital/HospitalCompare-DataDictionary.pdf".format(BASE_URL),
    ],
    "inpatient-rehabilitation-facilities": [
        "{}/archive/Inpatient%20rehabilitation%20facilities/current/inpatient_rehabilitation_facilities_current_data.zip".format(BASE_URL),
        "{}/data_dictionaries/inpatient/IRF-Data-Dictionary.pdf".format(BASE_URL),
    ],
    "long-term-care-hospitals": [
        "{}/archive/Long-term%20care%20hospitals/current/long-term_care_hospitals_current_data.zip".format(BASE_URL),
        "{}/data_dictionaries/long_term_care_hospital/LTCH-Data-Dictionary.pdf".format(BASE_URL),
    ],
    "nursing-homes-including-rehab-services": [
        "{}/archive/Nursing%20homes%20including%20rehab%20services/current/nursing_homes_including_rehab_services_current_data.zip".format(BASE_URL),
        "{}/data_dictionaries/nursing_home/NH_SNFQRP_Data_Dictionary.pdf".format(BASE_URL),
        "{}/data_dictionaries/nursing_home/NH_SNFVBP_Data_Dictionary.xlsx".format(BASE_URL),
        "{}/data_dictionaries/nursing_home/NH_Primary_Data_Dictionary.xlsx".format(BASE_URL),
    ],
    "supplier-directory": [
        "{}/archive/Supplier%20directory/current/supplier_directory_current_data.zip".format(BASE_URL),
        "{}/data_dictionaries/supplier/Supplier_Directory_Data_Dictionary.pdf".format(BASE_URL),
    ]
}

# AWS CONFIGURATIONS
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
OUTPUT_FOLDER = os.environ.get("OUTPUT_FOLDER")

# EMAIL CONFIGURATIONS
FROM_EMAIL = os.environ.get("FROM_EMAIL")
TO_EMAILS_LIST = os.environ.get("TO_EMAILS_LIST").split(",")
SES_CONFIG_SET_NAME = os.environ.get("SES_CONFIG_SET_NAME")
################################################################################


# AWS resources and clients (best practice is to keep outside handler for efficiency)
s3_client = boto3.client("s3")
s3_resource = boto3.resource("s3")
ses_client = boto3.client("ses")


def lambda_handler(event, context):
    """
    Main lambda handler function.
    """
    print("Event is:")
    print(event)
    print("Context is:")
    print(context)

    # Get latest file from the website
    print("The configuration for the scrapper is: ", SCRAPPER_CONFIGURATION)

    # Get DateTime value from current execution time
    current_date = datetime.datetime.now()
    current_year = current_date.strftime("%Y")
    current_month = current_date.strftime("%m")
    current_day = current_date.strftime("%d")
    print("current_date: ", current_date)

    # Iterate over all urls to get the files and upload them
    email_title = "Weekly CMS Provider Data Download Results"
    complete_body = {
        "messages": {},
        "errors": {},
        "bucket": S3_BUCKET_NAME,
    }
    for key in SCRAPPER_CONFIGURATION:
        print("current_scrapper_target: key is {} and values are {}".format(key, SCRAPPER_CONFIGURATION[key]))
        complete_body["messages"][key] = {}
        complete_body["messages"][key]["uploaded_files"] = ""

        # Iterate over each file to be scrapped
        for inner_url in SCRAPPER_CONFIGURATION[key]:
            try:
                # Download files from inner URLs
                print("downloading_file_from_url: downloading from URL {}".format(inner_url))
                output_file_path = download_file_from_url.download_file_from_url(inner_url, "{}//{}".format(OUTPUT_FOLDER, key))
                downloaded_file_stats = os.stat(output_file_path)
                file_size_in_mb = downloaded_file_stats.st_size / (1024 * 1024)
                print("downloaded_file_size_in_mb: ({}), with size ({} MB)".format(output_file_path, file_size_in_mb))

                # Upload downloaded file to S3 bucket
                print("starting_upload_of_file: ", output_file_path)
                s3_path = "{}/{}/{}-{}/{}".format(key, current_year, current_month, current_day, os.path.basename(output_file_path))
                s3_helpers.upload_file_to_s3(s3_client, S3_BUCKET_NAME, output_file_path, s3_path)
                complete_body["messages"][key]["uploaded_files"] += "{},".format(os.path.basename(output_file_path))

            except Exception as e:
                print("exception_error: {}".format(e))
                complete_body["errors"][key] = str(e)

    # Send e-mail based on process workflow and messages
    print("Starting e-mail process with SES...")
    print("email_title: {}".format(email_title))
    print("complete_body: {}".format(complete_body))
    print(send_emails_ses.email_handler(FROM_EMAIL, TO_EMAILS_LIST, ses_client, SES_CONFIG_SET_NAME, email_title, complete_body))

    return {
        "statusCode": 200,
        "body": complete_body
    }


## ONLY FOR LOCAL TESTS! (OWN COMPUTER VALIDATIONS)
if __name__ == "__main__":
    # TESTS
    print(lambda_handler({"info": "fake event for local validations"}, None))
