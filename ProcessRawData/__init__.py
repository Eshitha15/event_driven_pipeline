import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import os

connection_string = os.environ["AzureWebJobsStorage"]
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
raw_container = "raw"
processed_container = "processed"
reports_container = "reports"

def main(myblob: func.InputStream):
    logging.info(f"Processing blob: {myblob.name}, Size: {myblob.length} bytes")

    data = myblob.read().decode("utf-8")
    processed_data = data.upper()  # example processing

    # Upload processed data
    processed_blob_client = blob_service_client.get_blob_client(container=processed_container, blob=myblob.name)
    processed_blob_client.upload_blob(processed_data, overwrite=True)

    # Upload report
    report_name = f"report_{myblob.name}"
    report_blob_client = blob_service_client.get_blob_client(container=reports_container, blob=report_name)
    report_content = f"Blob {myblob.name} processed successfully."
    report_blob_client.upload_blob(report_content, overwrite=True)

    logging.info(f"Processing complete for {myblob.name}")

