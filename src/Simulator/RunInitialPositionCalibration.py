from Calibrator import Calibrator
import Pin

if __name__ == "__main__":
  calibrator = Calibrator(Pin.GetTextPin)
  calibrator.calibrateInitialPosition()
