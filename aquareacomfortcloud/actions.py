class ActionsSet:
    @staticmethod
    def tank_temperature(temperature):
        return {
            "status": [
                {
                    "tankStatus": [
                        {
                            "heatSet": temperature
                        }
                    ]
                }
            ]
        }
    
    @staticmethod
    def zone_temperature(zone, temperature):
        return {
            "status": [
                {
                "zoneStatus": [
                    {
                    "zoneId": zone,
                    "heatSet": temperature
                    }
                ]
                }
            ]
        }
    
    @staticmethod
    def zone_operation_status(zone, status):
        return {
            "status": [
                {
                "operationStatus": 1,
                "zoneStatus": [
                    {
                    "zoneId": zone,
                    "operationStatus": status
                    }
                ]
                }
            ]
        }
    
    @staticmethod
    def tank_operation_status(status):
        return {
            "status": [
                {
                "operationStatus": 1,
                "tankStatus": [
                    {
                    "operationStatus": status
                    }
                ]
                }
            ]
        }