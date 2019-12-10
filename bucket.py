
from google.cloud import storage

import argparse

parser = argparse.ArgumentParser() 
	
parser.add_argument('--input',           
                      dest='input',
                      required=True,
                      help='Input file to process.')

path_args, pipeline_args = parser.parse_known_args()  

inputs_pattern = path_args.input    



def create_bucket(bucket_name):
    """Creates a new bucket."""
    storage_client = storage.Client()
    storage_client.location = 'europe-west1'
    bucket = storage_client.create_bucket(bucket_name)
    print('Bucket {} created'.format(bucket.name))

create_bucket(inputs_pattern)