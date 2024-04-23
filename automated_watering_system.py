import paho.mqtt.client as mqtt

# Define thresholds
temperature_threshold = 30  # Adjust temperature threshold as needed
humidity_threshold = 60   # Adjust humidity threshold as needed
battery_threshold = 250    # Adjust battery level threshold as needed

# Define MQTT broker connection details
server_address = "20.106.179.116"
port = 1883
username = "server-mqtt"
password = "server-mqtt"
client_id = "bootcamp-6"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribe to sensor data topic
    client.subscribe("D2S/SA/V1/digitest-A")

    # Subscribe to actuator status topic
    client.subscribe("D2S/SA/V1/contest-A")


def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    # Process sensor data
    if topic == "D2S/SA/V1/digitest-A":
        try:
            data = dict(part.split(":") for part in payload.split(";"))
            temperature = int(data["0-T"])
            humidity = int(data["1-H"])

            # Check for threshold breach
            if temperature > temperature_threshold or humidity > humidity_threshold:
                turn_on_command = f"OM:1,TO:15"  # Turn on actuator with 15 min timeout
                client.publish("S2D/SA/V1/contest-A/A/0", turn_on_command)
                print(f"Threshold exceeded, sending turn on command: {turn_on_command}")
        except ValueError:
            print(f"Error parsing sensor data: {payload}")

    # Process actuator status
    if topic == "D2S/SA/V1/contest-A":
        try:
            data = dict(part.split(":") for part in payload.split(";"))
            battery_level = int(data["0-B"])
            actuator_statuses = [int(status) for status in data.values() if status.startswith("1-S")]

            # Check battery level
            if battery_level < battery_threshold:
                print(f"Warning: Battery level is low ({battery_level})!")

            # Check for actuator status change (print only for active actuators)
            for i, status in enumerate(actuator_statuses):
                if status == 1:
                    print(f"Actuator {i} status changed to {'ON' if status else 'OFF'}")
        except ValueError:
            print(f"Error parsing actuator status data: {payload}")


if __name__ == "__main__":
    # Create client with required callback_api_version argument
    client = mqtt.Client(callback_api_version=mqtt.MQTTv5)  # Assuming MQTTv5 support

    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(server_address, port)
    client.loop_forever()
