import boto3
import json

def analyze_text(text):
    # 1. Initialize the "NLP Processor"
    client = boto3.client('comprehend', region_name='us-east-1')

    print("--- INPUT SIGNAL ---")
    print(f"'{text}'\n")

    # 2. Detect Sentiment (The "Mood" of the signal)
    print("--- PROCESSING: SENTIMENT ---")
    sentiment_response = client.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )
    
    # Extract data
    mood = sentiment_response['Sentiment']
    scores = sentiment_response['SentimentScore']
    
    print(f"Detected Mood: {mood}")
    print(f"Confidence Scores:")
    print(f"  Positive: {scores['Positive']:.4f}")
    print(f"  Negative: {scores['Negative']:.4f}")
    print(f"  Neutral:  {scores['Neutral']:.4f}")

    # 3. Detect Key Phrases (The "Nouns" of the signal)
    print("\n--- PROCESSING: KEY PHRASES ---")
    phrases_response = client.detect_key_phrases(
        Text=text,
        LanguageCode='en'
    )
    
    for phrase in phrases_response['KeyPhrases']:
        print(f"• {phrase['Text']} (Confidence: {phrase['Score']:.2f})")

if __name__ == "__main__":
    # Test Data: A fake review about an electronics board
    sample_text = "I bought the STM32 Nucleo board from Robu.in. The shipping was incredibly fast, but the documentation was a bit confusing and hard to read."
    
    analyze_text(sample_text)
