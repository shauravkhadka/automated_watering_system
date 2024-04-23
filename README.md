Project Description

This project implements an automated watering system that monitors temperature and humidity sensors using MQTT communication. When sensor readings exceed predefined thresholds, it activates actuators for a specified duration to provide water to plants.

Features:

Monitors temperature and humidity sensors using MQTT.
Triggers actuator activation based on threshold breaches.
Provides feedback on sensor readings and actuator status.
Requirements:

Python 3.x
paho-mqtt library (pip install paho-mqtt)
MQTT broker (e.g., Mosquitto)
Sensor devices with MQTT capabilities
Actuator devices controllable via MQTT messages
Installation:

Install the required libraries:

Bash
pip install paho-mqtt
Use code with caution.
Configure the script with your specific MQTT broker address, port, username, password, and topic names.

Usage:

Modify the following variables within the script to match your setup:

server_address: Your MQTT broker address (e.g., "20.106.179.116")
port: MQTT broker port (e.g., 1883)
username: Username for MQTT authentication (if required)
password: Password for MQTT authentication (if required)
client_id: Unique client ID to identify this system
temperature_threshold: Temperature threshold for triggering watering (in degrees Celsius)
humidity_threshold: Humidity threshold for triggering watering (in percentage)
battery_threshold: Battery level threshold (optional, for warning messages)
Topic names for sensor data and actuator control (adjust accordingly)
Run the script:

Bash
python automated_watering_system.py
Use code with caution.
Explanation:

The script connects to the MQTT broker, subscribes to sensor data topics, and publishes commands to actuator control topics. It parses sensor data and triggers actuator activation when thresholds are exceeded.

Contributing:

Pull requests and suggestions are welcome. Feel free to fork the repository and contribute your improvements.

License:

This project is licensed under the (insert your preferred license, e.g., MIT License). See the LICENSE file for details.

Note:
