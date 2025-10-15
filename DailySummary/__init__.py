import os
from azure.storage.blob import BlobServiceClient
import logging

import azure.functions as func

# Read the connection string from environment variable
conn_str = os.environ.get("STORAGE_CONNECTION_STRING")
if not conn_str:
    raise ValueError("STORAGE_CONNECTION_STRING is not set in environment variables.")

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(conn_str)

def main(mytimer: func.TimerRequest) -> None:
    logging.info("Python timer trigger function started.")

    try:
        # List all containers as a test
        containers = blob_service_client.list_containers()
        container_names = [c.name for c in containers]
        logging.info(f"Found containers: {container_names}")
    except Exception as e:
        logging.error(f"Error accessing blob storage: {e}")
    
    logging.info("Python timer trigger function completed.")
