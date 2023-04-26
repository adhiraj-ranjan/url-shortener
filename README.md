URL Shortener Web App
This is a simple but fast and powerful URL shortener web app built using Flask (a Python web framework) and Firebase Realtime Database (a NoSQL cloud database). It allows users to create short URLs for long URLs, making it easier to share and manage links.

Features
Shorten long URLs: Users can enter a long URL and generate a short URL, which redirects to the original long URL.
Custom short URLs: Users can customize the generated short URL to their preference.
Click tracking: The web app keeps track of the number of clicks for each short URL, providing insights into link performance.
Easy to use: The web app has a simple user interface that makes it easy for users to create, customize, and manage short URLs.
Technologies Used
Flask: A lightweight web framework for Python that makes it easy to build web applications quickly.
Firebase Realtime Database: A NoSQL cloud database that provides real-time synchronization and data storage for web and mobile applications.
Installation
Clone the repository to your local machine.
Install the required Python packages using pip:
Copy code
pip install -r requirements.txt
Create a Firebase project and obtain the Firebase credentials (service account key) in JSON format.
Replace the firebase_credentials.json file in the app directory with your Firebase credentials.
Update the FIREBASE_URL variable in the config.py file with the URL of your Firebase Realtime Database.
Run the Flask application:
Copy code
python app.py
Open your web browser and go to http://localhost:5000 to access the URL shortener web app.
Usage
Enter a long URL in the input field on the home page.
Click the "Shorten" button to generate a short URL.
Optionally, you can customize the short URL by entering a custom alias.
Click the "Copy" button to copy the short URL to the clipboard.
Share the short URL with others, and it will redirect to the original long URL.
To track the number of clicks for a short URL, append /stats to the end of the short URL, e.g., http://localhost:5000/abc/stats.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is open source and available under the MIT License.

Acknowledgements
This web app was developed using Flask and Firebase Realtime Database, and was inspired by various URL shortener tutorials and examples available online.
