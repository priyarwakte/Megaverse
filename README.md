# Megaverse

This script automates the creation of entities within a virtual megaverse as part of a challenge. It is designed to interact with a specific API, fetch a goal configuration, and set up entities (Polyanets, Soloons, and Comeths) based on the fetched configuration.
Features
•	Fetches goal configuration for entity placement from a RESTful API.
•	Automatically sets up entities in the megaverse according to the fetched goal configuration.
•	Supports creating three types of entities: Polyanets, Soloons, and Comeths, with customizable parameters (e.g., color for Soloons, direction for Comeths).

## Prerequisites
•	Python 3.x installed on your system.
•	requests library installed. You can install it using pip

## How to Run
1.	Open a terminal or command prompt.
2.	Navigate to the directory where the script is saved.
3.	Run the script using the following command:
python Megaverse_creater.py

## Configuration  	
•	Candidate ID: The script uses a hard-coded candidate ID for API authentication.
•	API Base URL: The base URL for the API endpoints is configured at the beginning of the script. 
