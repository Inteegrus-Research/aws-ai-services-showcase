import boto3
import os

def speak(text):
    # 1. Initialize the "Voice Component"
    client = boto3.client('polly')

    print(f"Synthesizing: '{text}' ...")

    # 2. Send the Signal (Request Audio)
    response = client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Joanna',  # A popular US English Female voice
        Engine='neural'    # The high-quality Deep Learning engine
    )

    # 3. Save the Output Stream (Write MP3 to disk)
    output_file = "output.mp3"
    if "AudioStream" in response:
        with open(output_file, 'wb') as file:
            file.write(response['AudioStream'].read())
        print(f"Success! Audio saved to: {output_file}")
        
        # Optional: Auto-play on Linux (if you have mpv or vlc installed)
        # os.system(f"mpv {output_file}") 
    else:
        print("Error: No audio stream returned.")

if __name__ == "__main__":
    my_text = "Hello Keerthi. I am your cloud assistant running on Arch Linux. Systems are fully operational."
    speak(my_text)

