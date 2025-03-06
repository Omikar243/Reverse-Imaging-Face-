# Reverse Image Search (Face)

This project is a **Streamlit** application that uploads an image to Imgur, then performs a reverse image search (using the SERP API) to find visually similar images. It is especially handy for searching the internet for matches to a face image.

## Features

1. **Image Upload**: Upload a `.png`, `.jpg`, or `.jpeg` image from your computer.
2. **Imgur Upload**: Uses the imgurpython library to anonymously upload your image to Imgur, returning a public URL.
3. **Reverse Image Search**: Sends the Imgur URL to the SERP API's Google Reverse Image Search endpoint to look for visually similar images on the web.
4. **Filtering by Similarity**: Filters out results below a specified similarity threshold (default: 85%).

## Requirements

* **Python 3.7+**
* **Streamlit** (for the web interface)
* **imgurpython** (for uploading images to Imgur)
* **requests** (for sending HTTP requests to the SERP API)

You can install these with:

```bash
pip install streamlit imgurpython requests
```

## Setup

### 1. Obtain API Keys

1. **Imgur Client ID & Client Secret**
   * Register a new application on the [Imgur API page](https://api.imgur.com/oauth2/addclient).
   * Copy your **Client ID** and **Client Secret**.
   * The app only needs to perform anonymous uploads, so you won't necessarily need a full OAuth flow.

2. **SERP API Key**
   * Create an account on [SERP API](https://serpapi.com/) to get your free or paid API key.

### 2. Configure Your Credentials

In your code (`reverse_image.py`, for example), locate the following lines:

```python
SERP_API_KEY = "YOUR_SERP_API_KEY"
IMGUR_CLIENT_ID = "YOUR_IMGUR_CLIENT_ID"
IMGUR_CLIENT_SECRET = "YOUR_IMGUR_CLIENT_SECRET"
```

Replace the placeholder strings with your real credentials.

### 3. Check Your File Extension

Make sure your main file is named with a `.py` extension. For example: `reverse_image.py`.
* On Windows, if file extensions are hidden, you may need to enable **File name extensions** in File Explorer's **View** tab.
* If you see a "missing extension" error when running Streamlit, rename the file to ensure it ends with `.py` (and not `.py.txt`).

### 4. Run the App

Once you have your credentials in place and the file named properly:

```bash
streamlit run reverse_image.py
```

## Common Issues

* If you see an error like `Streamlit requires raw Python (.py) files, but the provided file has no extension`, rename the file to ensure it ends with `.py`.
* If you see "No module named imgurpython," install it via `pip install imgurpython`.
* If the SERP API returns an error, ensure your API key is correct and your subscription/usage limits are sufficient.

## Usage

1. **Open the Web App**: After running `streamlit run reverse_image.py`, your browser should open automatically at a local address (usually `http://localhost:8501`).
2. **Upload an Image**: Click **Browse files** (or drag-and-drop) to upload a face image in `.png`, `.jpg`, or `.jpeg` format.
3. **View Uploaded Image**: The app displays the uploaded image.
4. **Imgur Upload**: The image is then uploaded to Imgur, and the app shows you the public Imgur URL.
5. **Reverse Image Search**: The SERP API is called with your image's URL. If a "best guess" or similar images are found, they'll be displayed with their similarity scores.
6. **Inspect Raw Results**: An expandable section at the bottom shows the full JSON response from the SERP API for debugging or deeper inspection.

## Privacy Considerations

* Images uploaded to Imgur are public and accessible via the returned URL.
* Consider implementing image anonymization if you're handling sensitive images.
* This tool should not be used for stalking, harassment, or any unethical purposes.

## Contributing

Feel free to fork this repository and make improvements or add features (such as additional similarity filtering, improved face recognition, or storing results in a database). Pull requests are welcome!

## License

This project is provided as-is under the MIT License. See the LICENSE file for details.

## Contact / Support

For help with:
* **Imgur**: Refer to the [imgurpython README](https://github.com/Imgur/imgurpython) or contact api@imgur.com.
* **SERP API**: Check out the [SERP API documentation](https://serpapi.com/docs) or their support.
* **Streamlit**: See the [Streamlit documentation](https://docs.streamlit.io/) for how to build data apps.

## Disclaimer

This tool is for educational and research purposes only. Users are responsible for adhering to the terms of service of Imgur, Google, and SERP API when using this application.
