################################################################################
# Script to send emails based on result of processes.
################################################################################


def email_handler(from_email, to_emails_list, ses_client, ses_config_set_name, message_title_to_send, message_body_to_send):

    # This for is only for this custom setup, but can be deleted for other e-mails distributors
    processed_message_text = ""
    for category in message_body_to_send["messages"]:
        processed_message_text += "<p>Downloaded files for \"<b>{}</b>\" category were: [<b>{}</b>]</p>\n".format(category, message_body_to_send["messages"][category]["uploaded_files"])
    processed_errors_text = ""
    if len(message_body_to_send["errors"]) > 0:
        processed_errors_text += "<br><b><p>Errors on execution were: [{}]</p></b>".format(message_body_to_send["errors"])
    bucket_name = message_body_to_send["bucket"]

    body_html = f"""
    <html>
        <head></head>
        <body>
            <h2>AWS CMS PROVIDER: {message_title_to_send}</h2>
            <p>The weekly CMS Provider execution finished and was downloaded to the S3 bucket <b><a href=\"https://us-east-1.console.aws.amazon.com/s3/buckets/{bucket_name}\">{bucket_name}</a></b> is:</p>
            {processed_message_text}
            {processed_errors_text}
        </body>
    </html>
    """

    email_message = {
        "Body": {
            "Html": {
                "Charset": "utf-8",
                "Data": body_html,
            },
        },
        "Subject": {
            "Charset": "utf-8",
            "Data": message_title_to_send,
        },
    }

    ses_response = ses_client.send_email(
        Destination={
            "ToAddresses": to_emails_list,
        },
        Message=email_message,
        Source=from_email,
        ConfigurationSetName=ses_config_set_name,
    )

    print("SES Response is: {}".format(ses_response))

    return ses_response


## ONLY FOR LOCAL TESTS! (OWN COMPUTER VALIDATIONS)
if __name__ == "__main__":
    # TESTS
    import boto3
    ses_client = boto3.client("ses")
    from_email = "san99tiagodevsecops2@gmail.com"
    ses_config_set_name = "npi-emails"
    message_title_to_send = "New file found and downloaded successfully!"
    message_body_to_send = "The XXXX solution found a file and you can find it at the s3 bucket <BUCKET_NAME>"
    to_emails_list = ["san99tiagodevsecops@gmail.com", "san99tiagodevsecops2@gmail.com"]
    print(email_handler(from_email, to_emails_list, ses_client, ses_config_set_name, message_title_to_send, message_body_to_send))
