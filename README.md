# URL Shortener Web App
This is a simple but fast and powerful URL shortener web app built using Flask (a Python web framework) and Firebase Realtime Database (a NoSQL cloud database). It allows users to create short URLs for long URLs, making it easier to share and manage links.

## Ready to use instance
<a href=https://safeurl.onrender.com>https://safeurl.onrender.com</a>

## Features
* Shorten long URLs: Users can enter a long URL and generate a short URL, which redirects to the original long URL.
*. Custom short URLs: Users can customize the generated short URL to their preference.
* Easy to use: The web app has a simple user interface that makes it easy for users to create, customize, and manage short URLs.

## Technologies Used
* Flask: A lightweight web framework for Python that makes it easy to build web applications quickly.
* Firebase Realtime Database: A NoSQL cloud database that provides real-time synchronization and data storage for web and mobile applications.

## Installation
1. Clone the repository to your local machine.
2. Install the required Python packages using pip: `pip install -r requirements.txt`
3. Create a Firebase project and obtain the Firebase credentials (service account key) in JSON format.
4. Replace the fields in utils/api.py with your base64 encoded Firebase JSON credentials and your Firebase realtime database url.
5. Run the Flask application
6. Open your web browser and go to http://localhost:5000 to access the web app.

## Usage
1. Enter a long URL in the input field on the home page.
2. Click the "Shorten" button to generate a short URL.
3. Optionally, you can customize the short URL by entering a custom alias.
4. Click the Short Url to copy the short URL to the clipboard.
5. Share the short URL with others, and it will redirect to the original long URL.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is open source and available under the MIT License.

## Acknowledgements
This web app was developed using Flask and Firebase Realtime Database, and was inspired by the need of robust url shortener that enables any domain to be shorted.

### Find Me on :
<p align="left">
  <a href="https://github.com/adhiraj-ranjan" target="_blank"><img src="https://img.shields.io/badge/Github-adhiraj--ranjan-green?style=for-the-badge&logo=github"></a>
  <a href="https://www.instagram.com/adhirajranjan.i" target="_blank"><img src="https://img.shields.io/badge/IG-adhiraj_ranjan-pink?style=for-the-badge&logo=instagram"></a>
  <a href="https://t.me/adhirajranjan" target="_blank"><img src="https://img.shields.io/badge/TELEGRAM-ADHIRAJ%20RANJAN-blue?style=for-the-badge&logo=telegram"></a>
  
</p>
