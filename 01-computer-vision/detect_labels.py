import boto3

def analyze_image(filename):
    # 1. Initialize the "Vision Component" (Rekognition)
    client = boto3.client('rekognition')

    # 2. Read the image bytes (Input Signal)
    with open(filename, 'rb') as image:
        image_bytes = image.read()

    print(f"Sending {filename} to AWS Neural Network...")

    # 3. Send to AWS (The actual processing)
    response = client.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=10,
        MinConfidence=80
    )

    # 4. Decode the Output (Read the result)
    print("\n--- ANALYSIS REPORT ---")
    for label in response['Labels']:
        name = label['Name']
        confidence = label['Confidence']
        print(f"Detected: {name:<15} (Confidence: {confidence:.2f}%)")

if __name__ == "__main__":
    analyze_image('test_image.jpg')