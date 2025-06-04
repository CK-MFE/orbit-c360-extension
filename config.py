#!/usr/bin/python3

ROBOT_IP = "192.168.50.3"

# IP address the service can be reached at
SERVICE_IP = "192.168.50.5"
# Port the service can be reached at
SERVICE_PORT = 20000
# Payload preset json proto file
PRESET_FILE = "c360_preset_proto.json"

# Service Information
TCP_SERVER_PORT = 11000
# Unique name of the service instance
SERVICE_NAME = "flir-view-display"
# The rpc service type used to communicate with the service
SERVICE_TYPE = "bosdyn.api.internal.payload.ViewDisplayService"
# Authority to direct requests to the service
AUTHORITY = "view-display-service.spot.robot"
# Require requests to this service to include a token
USER_TOKEN_REQUIRED = True
KEEPALIVE_CHECK_INTERVAL = 30
TIMEOUT_SECS = 75  # 2.5X default rpc interval

ESTOP_NAME = "C360_estop"
FAULT_CLIENT_NAME = "C360_faults"
PUMP_NAME = "C360_pump"

# DAQ parameters
C360_DAQ_CHANNEL = 'data-acquisition-c360-plugin'
DAQ_SERVICE_PORT = 20360

# C360 Params
C360_PORT = "/dev/serial/by-id/usb-Linux_4.14.78-mx6+gaecdf94_with_2184000.usb_Gadget_Serial_v2.4-if00"
C360_QUEUE_SIZE = 100

# Enable Estop on LEL sensor trigger
ENABLE_ESTOP = True
ESTOP_TRIGGER_SENSOR = "LEL"
ESTOP_TRIGGER_UPPER_LIMIT = 5.0
ESTOP_TRIGGER_LOWER_LIMIT = -5.0

# Location where sensor logs will be recorded in real time
LOG_LOCATION = './sensor_logs'
# Location inside the container where sensor logs will be copied on startup.
# Logs will be copied into any subdirectory of this that contains a file named ".log_target"
# If this is an empty string, it will be ignored
LOG_SYNC_PATH = '/media'
# Number of samples to evaluate for negative bias removal (0 = disable)
NEGATIVE_BIAS_SAMPLES = 20
