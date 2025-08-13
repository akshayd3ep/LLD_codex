from abc import ABC, abstractmethod


class PrinterInterface(ABC): ...
class ScanInterface(ABC): ...
class FaxInterface(ABC): ...
class NormalPrinter(Printer):
    def print_document(self, document: str):
         print(f"Printing: {document}")

class SecondGenPrinter(Printer, Scan):
    def print_document(self, document: str):
        print(f"Printing: {document}")

    def scan_document(self, document: str):
        print(f"Scan: {document}")

class SmartPrinter(Printer, Scan, Fax):
    def print_document(self, document: str):
        print(f"Printing: {document}")

    def scan_document(self, document: str):
        print(f"Scan: {document}")

    def fax_document(self, document: str):
        print(f"Fax {document}")

    
SmartPrinter().fax_document("fax document this is")



# designing a system for a Smart Home Control application.

# SmartBulb → Can turn on/off, but doesn’t set temperature, play music, or show camera feed.

# SmartThermostat → Can turn on/off, and set temperature, but can’t play music or show camera feed.

# SmartSpeaker → Can turn on/off, play music, but no temperature or camera feed.

# SmartCamera → Can turn on/off, and show camera feed, but no temperature or music.

class Switch(ABC):
    def turn_on(self): pass
    def turn_off(self): pass

class Music(ABC):
    def play_music(self): pass

class Temperature(ABC):
    def show_temprature(self): pass

class Camera(ABC):
    def show_camera(self): pass


class SmartBulb(Switch, Music, Camera):
    def turn_on(self):
        print("bulb turn on")

    def turn_off(self):
        print("bulb turn off")

    def play_music(self):
        print("play music")

    def show_camera(self):
        print("show camera feeds")

class SmartThermostat(Switch, Temperature):
    def turn_on(self):
        print("Thermo turn on")

    def turn_off(self):
        print("Thermo turn off")

    def show_temprature(self):
        print("showing temprature")

class SmartSpeaker(Switch, Music):
    def turn_on(self):
        print("speaker turn on")

    def turn_off(self):
        print("speaker turn off")

    def play_music(self):
        print("play music")

class SmartCamera(Switch, Camera):
    def turn_on(self):
        print("Camera turn on")

    def turn_off(self):
        print("Camera turn off")

    def show_camera(self):
        print("show camera feeds")


