import cv2 # To create a VideoWriter object to write the captured frames to a video file.
import pyautogui # To get the screen size and capture screenshots.
import numpy as np

# Define the screen resolution
screen_width, screen_height = pyautogui.size()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_record.avi", fourcc, 20.0, (screen_width, screen_height))

# Set the recording region
record_region = (0, 0, screen_width, screen_height)

try:
    while True:
        # Capture the screen
        screenshot = pyautogui.screenshot(region=record_region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write the frame to the video file
        out.write(frame)

        # Break the loop when the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    pass

# Release the video writer and destroy all OpenCV windows
out.release()
cv2.destroyAllWindows()

