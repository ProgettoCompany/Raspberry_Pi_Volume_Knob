import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import alsaaudio

# Define the ADC channel and gain for the ADS1115
adc_channel = 0

# Initialize the I2C bus and the ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
adc = ADS.ADS1115(i2c)

# Define the volume control parameters
min_volume = 0  # Minimum volume (0%)
max_volume = 100  # Maximum volume (100%)
audio_device = "Master"  # You may need to adjust this based on your system configuration

# Create an ALSA mixer object for volume control
mixer = alsaaudio.Mixer(audio_device)

# Main loop
try:
    while True:
        # Read the analog value from the potentiometer
        analog_value = adc.read(adc_channel)

        # Map the analog value to the volume range
        volume = int((analog_value / 26250) * max_volume)
        volume = max(min_volume, min(volume, max_volume))

        # Set the volume
        mixer.setvolume(volume)

        print(f"Analog Value: {analog_value}, Volume: {volume}%")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
