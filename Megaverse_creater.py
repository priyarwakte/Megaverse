import requests  
import time  
import yaml  

def load_config():
    """
    Loads and returns the configuration from a YAML file.
    This allows the script to be configured externally, making it more flexible.
    """
    with open('config.yml', 'r') as file:  # Open the YAML configuration file in read mode
        return yaml.safe_load(file)  # Parse the YAML and return the configuration dictionary

# Load the configuration from the YAML file
config = load_config()

# Assign configuration values to variables for easy reference
CANDIDATE_ID = config['CANDIDATE_ID']
API_BASE_URL = config['API_BASE_URL']

def create_entity(entity_type, row, column, additional_params={}):
    """
    Creates an entity (Polyanet, Soloon, or Cometh) on the megaverse map at the specified location.
    Additional parameters can be provided for entities that require them (e.g., color for Soloon).
    
    Args:
    - entity_type: The type of entity to create (e.g., 'polyanet', 'soloon', 'cometh').
    - row: The row position where the entity should be created.
    - column: The column position where the entity should be created.
    - additional_params: A dictionary of additional parameters required for certain entities.
    """
    url = f"{API_BASE_URL}/{entity_type}s"  # Construct the URL for the entity's API endpoint
    payload = {"candidateId": CANDIDATE_ID, "row": row, "column": column, **additional_params}  # Payload for the POST request
    response = requests.post(url, json=payload)  # Make the POST request
    if response.status_code == 200:  # If the request was successful
        print(f"{entity_type.capitalize()} created at ({row}, {column}) with params {additional_params}")
    else:  # If there was an error
        print(f"Error creating {entity_type} at ({row}, {column}): {response.text}")
    time.sleep(0.5)  # Delay to prevent overwhelming the server

def setup_phase(goal):
    """
    Iterates through the goal configuration and creates the entities on the map accordingly.
    
    Args:
    - goal: A 2D list representing the goal configuration, with each cell specifying what entity (if any) should be there.
    """
    for i, row in enumerate(goal):
        for j, cell in enumerate(row):
            if cell == "POLYANET":
                create_entity('polyanet', i, j)
            elif "SOLOON" in cell:
                color = cell.split("_")[0].lower()
                create_entity('soloon', i, j, {"color": color})
            elif "COMETH" in cell:
                direction = cell.split("_")[0].lower()
                create_entity('cometh', i, j, {"direction": direction})

def fetch_goal_array():
    """
    Fetches the goal configuration array from the API, which specifies where entities should be placed for Phase 2.
    
    Returns:
    A list of lists representing the goal configuration, or an empty list if fetching fails.
    """
    url = f"{API_BASE_URL}/map/{CANDIDATE_ID}/goal"  # URL to fetch the goal array
    response = requests.get(url)  # Make the GET request
    if response.status_code == 200:  # If the request was successful
        goal_data = response.json()  # Parse the JSON response
        return goal_data.get("goal", [])  # Return the goal configuration
    else:  # If fetching fails
        print(f"Failed to fetch the goal array: HTTP Status Code {response.status_code}")
        return []

def main():
    """
    The main function of the script. Fetches the goal configuration and sets up the entities accordingly.
    """
    goal = fetch_goal_array()  # Fetch the goal configuration for Phase 2
    if not goal:  # If fetching failed or the goal is empty
        print("Failed to fetch goal or goal is empty, exiting...")
        return
    print("Setting up Phase ...")
    setup_phase(goal)  # Setup the entities based on the goal configuration

if __name__ == "__main__":
    main()  # Execute the main function
