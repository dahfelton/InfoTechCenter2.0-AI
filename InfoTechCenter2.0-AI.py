# Displaying a header for the Gasoline Branch
print("*****************************************")
print("Gasoline Branch\n\n")

# Importing necessary libraries
import random
from time import sleep


# Function that returns the current gas level randomly
def gas_level_gauge():
    """
    Returns the current gas level.
    """
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gas_level_list)


# Function that returns a randomly chosen gas station
def list_of_gas_stations():
    """
    Returns a randomly chosen gas station.
    """
    gas_stations = ["Shell", "Speedway", "Marathon", "Circle K", "Mobile", "Costco", "Meijer", "7Eleven"]
    return random.choice(gas_stations)


# Function to provide gas level alerts and information about nearby gas stations
def gas_level_alert():
    """
    Provides gas level alert and information about nearby gas stations.
    """
    # Generating random distances to gas stations
    miles_to_gas_stations_low = round(random.uniform(1, 25), 1)
    miles_to_gas_stations_quarter_tank = round(random.uniform(25.1, 50), 1)

    # Getting the current gas level
    gas_level_indicator = gas_level_gauge()

    # Displaying appropriate message based on the gas level
    if gas_level_indicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(2.5)
        print("\n    ***Calling Triple AAA***")
    elif gas_level_indicator == "Low":
        print("Your gas tank is LOW, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is", list_of_gas_stations(), "which is", miles_to_gas_stations_low,
              "miles away.")
    elif gas_level_indicator == "Quarter Tank":
        print("Your gas tank is on a QUARTER TANK, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is", list_of_gas_stations(), "which is", miles_to_gas_stations_quarter_tank,
              "miles away.")
    elif gas_level_indicator == "Half Tank":
        print("Your gas tank is on a HALF TANK which is plenty to get to your destination")
    elif gas_level_indicator == "Three Quarter Tank":
        print("Your gas tank is on a THREE QUARTER TANK which is plenty to get to your destination")
    else:
        print("Your gas tank is FULL, HORRAYYYYYYY VROOOM VROOOM!!")


# Calling the gas level alert function to initiate the alert process
gas_level_alert()
