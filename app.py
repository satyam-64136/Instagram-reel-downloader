from flask import Flask, request, render_template, send_file, Response
import instaloader
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_reels():
    url = request.form.get('url')
    if url:
        try:
            # Create an Instaloader instance
            loader = instaloader.Instaloader()

            # Download the post
            post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])

            # Check if the post is a video
            if post.is_video:
                video_url = post.video_url
                response = requests.get(video_url)

                if response.status_code == 200:
                    # Define the filename for the downloaded video
                    filename = f"{post.owner_username}_{post.date_utc.strftime('%Y%m%d%H%M%S')}.mp4"

                    # Set the appropriate content headers for the response
                    headers = {
                        'Content-Disposition': f'attachment; filename={filename}',
                        'Content-Type': 'video/mp4',
                    }

                    # Return the file as a response with headers
                    return Response(response.content, headers=headers)
                else:
                    return "Video download failed."
            else:
                return "The provided URL is not for a video."
        except Exception as e:
            return f"Error: {e}"

    return "Please enter a valid Instagram Reels URL."

if __name__ == '__main__':
    app.run(debug=True)
