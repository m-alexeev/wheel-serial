"""
ConfigHandler

Handles configuration changes, saving and loading 

Author: Mikhail Alexeev
Last Modified: Nov 4, 2023
"""

class ConfigHandler:
    def __init__(self) -> None:
        self.loaded_configuration = None
    
    def set_configuration(self, config) -> None:
        self.loaded_configuration = config
        
    def update_config(self, key: str, value: str) -> None: 
        if key in self.loaded_configuration:
            self.loaded_configuration[key] = value
        