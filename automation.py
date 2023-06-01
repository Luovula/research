import pyautogui
import pytesseract
import cv2
import re
from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt
import json


# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Elphie\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Function to click the next number on the top right side of the application
def click_next_number(current_number):
    next_number = (current_number + 1)
    pyautogui.press('up')
    #pyautogui.scroll(1)
    


# Locate the next number on screen and click on it
  #  next_number_location = pyautogui.locateOnScreen('next_number_preprocessed.png', confidence=0.7)
   # if next_number_location is not None:
    #    next_number_center = pyautogui.center(next_number_location)
     #   pyautogui.click(next_number_center.x + 50, next_number_center.y)  # Add offset to click to the right of the number
   # else:
    #    print('Next number not found on screen')
    #if next_number < 7:
     #   next_number_location = pyautogui.locateOnScreen(str(next_number) + '.png', confidence=0.8)

    #if  next_number < 6:
       # next_number_center = pyautogui.center(next_number_location)
      #  pyautogui.moveTo(next_number_center)
     #   pyautogui.click()
    #     #Click twice
   # elif next_number > 5:
    #    coord_x = 2280
   #     coord_y = 280
   #     pyautogui.moveTo(coord_x, coord_y)
    #    pyautogui.click()
  #  else:
  #      print("Next number not found.")
    return next_number

# Initialize the current number, the last number, and the list to store results
current_number = 0
last_number = 163  # Replace this with the actual last number
results = []

while True:
    # Locate the "pass" button
    pass_button_location = pyautogui.locateOnScreen('pass.png', confidence=0.7 )
    if pass_button_location is not None:
        # Click the "pass" button
        
        pass_button_center = pyautogui.center(pass_button_location)
        x =303
        y =1384
        pyautogui.moveTo(pass_button_center)
        pyautogui.click()
        
        # Locate the "points lost" text
        time.sleep(2)
        points_lost_location = pyautogui.locateOnScreen('pointslost.png', confidence=0.7)

        if points_lost_location is not None:
            # Define the region of interest (ROI) to capture the result next to the "points lost" text
            x, y, width, height = points_lost_location.left + points_lost_location.width + 150, points_lost_location.top, 100, points_lost_location.height
            roi = (x, y, width, height)
            roi_screenshot = pyautogui.screenshot(region=roi)
           # roi_screenshot.show()
            

            # Convert the screenshot to grayscale for better OCR results
            gray_roi = cv2.cvtColor(np.array(roi_screenshot), cv2.COLOR_RGB2GRAY)
            

            _, binary_roi = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            gray_roi_image = Image.fromarray(binary_roi)

            # Extract the text from the grayscale image using Tesseract OCR
            result_text = pytesseract.image_to_string(gray_roi_image, config='--psm 7')

            # Extract the numeric result using a regular expression and save it to the list
            match = re.search(r'\d+', result_text)
            if match:
                result = int(match.group(0))
                results.append(result)
                print("Result:", result)
            else:
                result = 0
                results.append(result)
                print(f"move {current_number} error")
            # Click the next number and check if it's the last one
            current_number = click_next_number(current_number)
            #time.sleep(1)
            if current_number == last_number + 1:
                break
        else:
            print("Points lost text not found.")
            break
    else:
        print("Pass button not found.")
        break

print("Results:", results)
title = 'game_201'
jsonStr = json.dumps(results)
with open(title, "w") as tiedosto:
    tiedosto.write(jsonStr)
cop = results
moves=list(range(0, len(results)))
x = np.arange(0,len(results),10)
plt.bar(moves,cop,color=['black','grey'], width = 0.5)
plt.xticks(x)
plt.xlabel('moves')
plt.ylabel('cop')
plt.title(title)

plt.show()