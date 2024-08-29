from flask import Flask, request, render_template, send_file
import instaloader
import requests
import io
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_reels():
    url = request.form.get('url')
    if url:
        try:
            loader = instaloader.Instaloader()
            shortcode = url.split('/')[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)

            if post.is_video:
                video_url = post.video_url
                video_data = requests.get(video_url).content

                caption = post.caption[:50] if post.caption else "no_caption"
                caption = re.sub(r'[^\w\s-]', '', caption).strip().replace(' ', '_')
                if not caption:
                    caption = "no_caption"

                filename = f"{caption}_{post.owner_username}_{post.date_utc.strftime('%Y%m%d%H%M%S')}.mp4"
                
                return send_file(
                    io.BytesIO(video_data),
                    mimetype='video/mp4',
                    as_attachment=True,
                    download_name=filename
                )
            else:
                return "The provided URL is not for a video."

        except Exception as e:
            # Logging the exception for debugging
            print(f"Error: {e}")
            return f"Error: {e}"

    return "Please enter a valid Instagram Reels URL."

if __name__ == '__main__':
    app.run(debug=True)
