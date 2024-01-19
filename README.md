# panasonic-aquarea-python
# Aquarea Comfort Cloud Python API

This Python package provides a simple interface for interacting with the Panasonic Aquarea Comfort Cloud API, allowing you to control and monitor your Aquarea heat pump devices programmatically.

## Usage

### Prerequisites
- Python 3.x

### Example Usage

#### main.py
```python
from aquareacomfortcloud.session import AquareaSession
from aquareacomfortcloud.device import AquareaDevice
from aquareacomfortcloud.actions import ActionsSet

if __name__ == "__main__":
    user_email = "your.address@email.com"
    user_password = "yourpassword"
    device_guid = "yourdeviceguid"

    session = AquareaSession(user_email, user_password)
    session.login()

    device = AquareaDevice(device_guid, session)
    device.set(ActionsSet.tank_temperature(45))
    
    session.logout()
```