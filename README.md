# AWS AI Services Showcase

This repository demonstrates the integration of AWS Artificial Intelligence services into Python applications.
Built on **Arch Linux** using the **Boto3 SDK**.

## 🛠 Modules Built

### 1. Computer Vision (AWS Rekognition)
* **Function:** Detects objects and labels in images with >99% confidence.
* **Tech:** `boto3.client('rekognition')`

### 2. Text-to-Speech (AWS Polly)
* **Function:** Converts text strings into lifelike "Neural" speech (MP3).
* **Tech:** `boto3.client('polly')`, Neural Engine.

### 3. Speech-to-Text (AWS Transcribe)
* **Function:** Asynchronous transcription of audio files to text.
* **Tech:** `boto3.client('transcribe')`, S3 Bucket Integration.

### 4. Natural Language Processing (AWS Comprehend)
* **Function:** Analyzes customer sentiment and extracts key phrases.
* **Tech:** `boto3.client('comprehend')`

## 🚀 Status
* **Rekognition & Polly:** Fully Operational ✅
* **Transcribe & Comprehend:** Code complete; awaiting AWS Account Verification (24h Sandbox).
