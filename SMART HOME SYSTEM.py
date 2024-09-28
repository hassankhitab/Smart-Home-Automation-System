# Function to get input from the user
def get_user_input(prompt):
    while True:
        user_input = input(prompt + " (yes/no): ").strip().lower()
        if user_input in ['yes', 'no']:
            return user_input == 'yes'
        else:
            print("Please enter 'yes' or 'no'.")

# Get inputs from the user
is_nighttime = get_user_input("Is it nighttime?")
is_home_occupied = get_user_input("Is the house occupied?")
is_cold_outside = get_user_input("Is it cold outside?")

# Device states
lights_on = False
heating_on = False
security_camera_on = False

# Functions to control devices
def control_lights(is_nighttime, is_home_occupied):
    if is_nighttime and is_home_occupied:
        return True  # Turn on the lights
    else:
        return False  # Turn off the lights

def control_heating(is_home_occupied, is_cold_outside):
    if not is_home_occupied:
        return False  # Turn off heating
    elif is_home_occupied and is_cold_outside:
        return True  # Turn on heating
    else:
        return False  # Turn off heating

def control_security_camera(is_home_occupied, is_nighttime):
    if not is_home_occupied or is_nighttime:
        return True  # Activate security camera
    else:
        return False  # Deactivate security camera

# Applying the rules
lights_on = control_lights(is_nighttime, is_home_occupied)
heating_on = control_heating(is_home_occupied, is_cold_outside)
security_camera_on = control_security_camera(is_home_occupied, is_nighttime)

# Output the states of the devices
print("\nSmart Home System Status:")
print(f"Lights are {'on' if lights_on else 'off'}")
print(f"Heating is {'on' if heating_on else 'off'}")
print(f"Security camera is {'activated' if security_camera_on else 'deactivated'}")