import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QPushButton
from PyQt5.QtCore import Qt
from gpiozero import PWMLED

class LEDController(QWidget):
    def __init__(RGB):
        super().__init__()
        RGB.initUI()

    def initUI(RGB):
        RGB.setWindowTitle("LED Slider")
        # Define LED pins
        RGB.LED_pins = [18, 23, 24]
        # Setup LED objects
        RGB.leds = [PWMLED(pin) for pin in RGB.LED_pins]
        # Create sliders for LED intensity control
        RGB.sliders = []
        for led in RGB.leds:
            slider = QSlider(Qt.Horizontal, RGB)
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.valueChanged.connect(lambda value, led=led: RGB.set_intensity(value, led))
            RGB.sliders.append(slider)
        # Create exit button
        RGB.exit_button = QPushButton("Exit", RGB)
        RGB.exit_button.clicked.connect(RGB.close)
        # Layout setup
        layout = QVBoxLayout()
        for slider in RGB.sliders:
            layout.addWidget(slider)
        layout.addWidget(RGB.exit_button)

        RGB.setLayout(layout)
        RGB.show()

    # Function to set LED intensity
    def set_intensity(RGB, value, led):
        led.value = value / 100.0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LEDController()
    sys.exit(app.exec_())
