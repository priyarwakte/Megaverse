# Megaverse

This script automates the setup of entities in the Megaverse challenge. It supports creating Polyanets, Soloons, and Comeths based on a goal configuration fetched from an API. The script uses a YAML file for configuration to enhance flexibility.

## Prerequisites
This script requires Python 3 and the following Python packages:
- requests for making API requests
- pyyaml (or yaml) for parsing YAML configuration files

## How to Run
1.	Open a terminal or command prompt.
2.	Navigate to the directory where the script is saved.
3.	Run the script using the following command:
python Megaverse_creater.py

## Script Functions
- load_config(): Loads API configuration from a YAML file.
- create_entity(): Creates an entity in the Megaverse.
- setup_phase(): Iterates through a goal configuration and creates entities accordingly.
- fetch_goal_array(): Fetches the goal configuration from the API.
- main(): The main function that orchestrates fetching the goal configuration and setting up entities.

