import subprocess

def download_mp3():
    
    url = input("Enter the URL to download: ")
    output_path = input("Enter the output path (including filename): ")

    subprocess.run(["spotdl", url, "--output", output_path, "--no-cache"])





    