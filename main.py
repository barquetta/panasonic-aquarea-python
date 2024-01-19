from aquareacomfortcloud.session import AquareaSession
from aquareacomfortcloud.device import AquareaDevice
from aquareacomfortcloud.actions import ActionsSet

if __name__ == "__main__":
    user_email = "your.addres@email.com"
    user_password = "yourpassword"
    device_guid = "yourdeviceguid"

    session = AquareaSession(user_email, user_password)
    session.login()

    device = AquareaDevice(device_guid, session)
    device.set(ActionsSet.tank_temperature(45))
    
    session.logout()
