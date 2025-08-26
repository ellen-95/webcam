# Webcam Streamlit App

An interactive **webcam application** built with [Streamlit](https://streamlit.io/).  
This project demonstrates how to capture video frames using your webcam directly inside a web app.

## Features
- Access webcam through Streamlit.
- Display live video stream.
- Capture frames (images).
- Simple and intuitive interface.

## Demo
Try it here [ellen-webcam.streamlit.app](https://ellen-webcam.streamlit.app/)
**If the page shows the reboot the app, please click that button to reboot the webapp.**

---

## Tech Stack
- **Python 3**
- **Streamlit** for web interface
- **OpenCV** for webcam access

---

## Project Structure
```
├── app.py          # Main Streamlit app
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Installation
To run locally:
```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/ellen-webcam.git
cd ellen-webcam

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

## Future Improvements
- Add image processing filters (grayscale, blur, edge detection).
- Save captured images to a local folder or database.
- Enable video recording.
