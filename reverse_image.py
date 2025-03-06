import streamlit as st
import requests
import tempfile
import os
from imgurpython import ImgurClient

# --- Configuration ---
# Replace these with your actual API keys.
SERP_API_KEY = "e0e6c161e3223d65745b6ca2b966750fc79789edb6903f29d6930e4ec3ab9cb3"           # Get your key from https://serpapi.com/
IMGUR_CLIENT_ID = "80798573167140b"      # See README.md for details on registering your app.
IMGUR_CLIENT_SECRET = "3153343d485ace3c6523c0627d4f0a64ac603478"

def upload_to_imgur(image_path):
    """
    Uploads the image to Imgur using imgurpython and returns the public image URL.
    This uses an anonymous upload (anon=True). For more details, check the README.
    """
    client = ImgurClient(IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET)
    # The README from the imgurpython project shows usage for anonymous uploads.
    uploaded_image = client.upload_from_path(image_path, config=None, anon=True)
    return uploaded_image["link"]

def search_reverse_image(image_url):
    """
    Calls the SERP API with the image URL for reverse image search.
    Returns the JSON results.
    """
    params = {
        "engine": "google_reverse_image",
        "image_url": image_url,
        "api_key": SERP_API_KEY
    }
    response = requests.get("https://serpapi.com/search", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error in SERP API request.")
        return None

def filter_similar_results(results, threshold=85):
    """
    Filters the search results and returns those with a similarity score
    greater than or equal to the threshold (if such a field is provided).
    """
    filtered = []
    # Check for keys where similar images might be stored.
    for key in ["visually_similar_images", "similar_images", "image_results"]:
        if key in results:
            for item in results[key]:
                similarity = item.get("similarity")
                if similarity:
                    try:
                        # Convert similarity to a float (supports "85%" string or numeric value)
                        if isinstance(similarity, str) and "%" in similarity:
                            similarity_value = float(similarity.replace("%", ""))
                        else:
                            similarity_value = float(similarity)
                        if similarity_value >= threshold:
                            filtered.append(item)
                    except Exception:
                        continue
    return filtered

def main():
    st.title("Reverse Image Search for Faces")
    st.write("Upload an image of a face to search for similar faces on the internet.")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        
        # Save the uploaded image to a temporary file so we can upload it to Imgur
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_file_path = tmp_file.name
        
        st.write("Uploading image to Imgur...")
        try:
            image_url = upload_to_imgur(temp_file_path)
            st.write("Image uploaded successfully. URL:", image_url)
        except Exception as e:
            st.error(f"Error uploading image: {e}")
            os.unlink(temp_file_path)
            return

        os.unlink(temp_file_path)  # Clean up the temporary file

        st.write("Performing reverse image search...")
        results = search_reverse_image(image_url)
        if results is None:
            return

        # Display the best guess if available
        if "best_guess" in results:
            st.subheader("Best Guess")
            st.write(results["best_guess"])
        
        # Filter and display similar images based on a threshold (85% here)
        similar_results = filter_similar_results(results, threshold=85)
        if similar_results:
            st.subheader("Similar Images (>= 85% similarity)")
            for idx, item in enumerate(similar_results, 1):
                st.write(f"Result {idx}:")
                if "thumbnail" in item:
                    st.image(item["thumbnail"], use_column_width=True)
                st.write(item)
        else:
            st.write("No results found with 85% or higher similarity.")
        
        # Optionally, display all raw API results for debugging/inspection
        with st.expander("Raw Results"):
            st.json(results)

if __name__ == "__main__":
    main()
