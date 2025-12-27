import boto3
import time
import urllib.request
import json
import uuid

# --- CONFIGURATION ---
# We need a unique bucket name (Buckets are global, like website domains)
# We use a random ID to ensure it works instantly for you.
BUCKET_NAME = f"transcribe-demo-{uuid.uuid4().hex[:8]}"
FILE_NAME = "output.mp3"
JOB_NAME = f"TranscribeJob-{uuid.uuid4().hex[:8]}"
REGION = "us-east-1"

def transcribe_demo():
    s3 = boto3.client('s3')
    transcribe = boto3.client('transcribe')

    # 1. Create a temporary S3 Bucket (The Buffer)
    print(f"Creating bucket: {BUCKET_NAME}...")
    try:
        s3.create_bucket(Bucket=BUCKET_NAME)
    except Exception as e:
        print(f"Bucket might already exist or error: {e}")

    # 2. Upload the MP3 to the Bucket
    print(f"Uploading {FILE_NAME} to S3...")
    s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)

    # 3. Trigger the Transcription Job
    file_uri = f"s3://{BUCKET_NAME}/{FILE_NAME}"
    print(f"Starting Job: {JOB_NAME}...")
    
    transcribe.start_transcription_job(
        TranscriptionJobName=JOB_NAME,
        Media={'MediaFileUri': file_uri},
        MediaFormat='mp3',
        LanguageCode='en-US'
    )

    # 4. Polling Loop (Waiting for the result)
    print("Waiting for transcription...", end="")
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=JOB_NAME)
        job_status = status['TranscriptionJob']['TranscriptionJobStatus']
        
        if job_status in ['COMPLETED', 'FAILED']:
            break
        print(".", end="", flush=True)
        time.sleep(2) # Wait 2 seconds before checking again

    print(f"\nJob Status: {job_status}")

    # 5. Fetch and Print the Text
    if job_status == 'COMPLETED':
        transcript_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
        # Download the JSON result from the URL AWS gives us
        with urllib.request.urlopen(transcript_uri) as url:
            data = json.loads(url.read().decode())
            text = data['results']['transcripts'][0]['transcript']
            
        print("\n--- FINAL TRANSCRIPT ---")
        print(text)
        print("------------------------")
    
    # Cleanup (Optional: Delete the job to keep things clean)
    transcribe.delete_transcription_job(TranscriptionJobName=JOB_NAME)

if __name__ == "__main__":
    transcribe_demo()
