# **Instagram Reels Downloader**

This **Flask-based application** allows users to download Instagram Reels by providing the URL of the reel. The application fetches the video and saves it with a filename that includes the caption of the reel, the username of the poster, and the date.

## **Features**

- **Download Instagram Reels:** Provide the URL of an Instagram Reel to download the video.
- **Caption in Filename:** The downloaded video is saved with the reel's caption, the username, and the date in the filename.
- **Error Handling:** Handles rate limiting and other potential errors when accessing Instagram's data.

## **Prerequisites**

- Python 3.x
- Flask
- Instaloader
- Requests

## **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/instagram-reels-downloader.git
   cd instagram-reels-downloader
2. **Install the required dependencies:**

   ```bash
    pip install -r requirements.txt
3. **Set your Instagram credentials:**
 - Replace 'your_username' and 'your_password' in the download_reels() function in app.py with your Instagram login credentials.

## **Usage**
1. **Run the Flask application:**
   ```bash
   python app.py
2. **Open your browser and go to:**
   ```bash[
   python app.py](http://127.0.0.1:5000/)
3. **Enter the URL of the Instagram Reel:**
  - The application will process the URL and provide a download link for the video.

## **File Structure**
- app.py: Main Flask application file.
- templates/index.html: HTML file for the web interface.
-requirements.txt: List of Python dependencies.
-README.md: This file.
## **Contributing**
Feel free to fork this repository, create a branch, make your changes, and submit a pull request. Contributions are always welcome!
   
