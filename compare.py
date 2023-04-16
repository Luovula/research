import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have three lists: opening_cop, middle_cop, and end_cop
opening_cop = np.array([12.0, 13.0, 12.0, 13.0, 12.0, 12.0, 12.0, 12.0, 12.0, 13.0, 15.0, 15.0, 14.0, 13.0, 12.0, 13.0, 12.0, 18.0, 12.0, 11.0, 12.0, 12.0, 14.0, 15.0, 16.0, 19.0, 17.0, 15.0, 19.0, 14.0, 12.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 11.0, 12.0, 12.0, 12.0, 12.0, 13.0, 13.0, 12.0, 14.0, 13.0, 16.0, 15.0, 13.0, 12.0, 11.0, 12.0, 11.0, 12.0, 11.0, 12.0, 14.0, 12.0, 12.0, 12.0, 12.0, 12.0, 13.0, 12.0, 12.0, 12.0, 12.0, 12.0, 15.0, 14.0, 16.0, 12.0, 12.0, 12.0, 13.0, 13.0, 12.0, 14.0, 15.0, 17.0, 13.0, 15.0, 14.0, 14.0, 14.0, 13.0, 12.0, 13.0, 12.0, 9.0, 20.0, 13.0, 27.0, 11.0, 36.0, 11.0, 8.0, 28.0, 8.0, 12.0, 17.0, 14.0, 7.0, 10.0, 8.0, 16.0, 12.0, 12.0, 10.0, 13.0, 13.0, 14.0, 8.0, 10.0, 8.0, 14.0, 15.0, 15.0, 8.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 11.0, 10.0, 13.0, 11.0, 13.0, 13.0, 13.0, 14.0, 15.0, 14.0, 16.0, 13.0, 13.0, 12.0, 11.0, 11.0, 11.0, 11.0, 11.0, 15.0, 14.0, 14.0, 17.0, 14.0, 12.0, 12.0, 12.0, 11.0, 11.0, 12.0, 11.0, 12.0, 11.0, 12.0, 12.0, 12.0, 15.0, 11.0, 12.0, 12.0, 11.0, 13.0, 11.0, 12.0, 12.0, 12.0, 13.0, 13.0, 12.0, 11.0, 19.0, 12.0, 13.0, 14.0, 12.0, 12.0, 12.0, 12.0, 12.0, 11.0, 11.0, 11.0, 13.0, 14.0, 15.0, 14.0, 17.0, 14.0, 12.0, 12.0, 11.0, 23.0, 13.0, 11.0, 12.0, 11.0, 12.0, 11.0, 14.0, 12.0, 12.0, 12.0, 14.0, 12.0, 12.0, 12.0, 12.0, 11.0, 13.0, 12.0, 13.0, 13.0, 13.0, 11.0, 12.0, 11.0, 11.0, 12.0, 11.0, 15.0, 12.0, 10.0, 13.0, 12.0, 11.0, 17.0, 12.0, 12.0, 12.0, 12.0, 13.0, 13.0, 11.0, 11.0, 13.0, 11.0, 11.0, 15.0, 11.0, 12.0, 11.0, 12.0, 12.0, 11.0, 17.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 11.0, 14.0, 11.0, 13.0, 11.0, 11.0, 13.0, 12.0, 13.0, 11.0, 13.0, 14.0, 11.0, 12.0, 11.0, 11.0, 11.0, 12.0, 11.0, 13.0, 11.0, 13.0, 11.0, 11.0, 13.0, 12.0, 15.0, 13.0, 13.0, 13.0, 11.0, 11.0, 11.0, 22.0, 11.0, 13.0, 12.0, 13.0, 24.0, 13.0, 12.0, 11.0, 12.0, 12.0, 12.0, 11.0, 12.0, 11.0, 16.0, 11.0, 12.0, 11.0, 11.0, 11.0, 13.0, 11.0, 14.0, 13.0, 14.0, 15.0, 13.0, 12.0, 13.0, 13.0, 12.0, 11.0, 11.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 13.0, 17.0, 12.0, 12.0, 11.0, 11.0, 10.0, 13.0, 11.0, 12.0, 10.0, 13.0, 10.0, 12.0, 11.0, 15.0, 11.0, 12.0, 11.0, 13.0, 13.0, 15.0, 17.0, 12.0, 12.0, 12.0, 11.0, 13.0, 14.0, 12.0, 11.0, 13.0, 12.0, 13.0, 11.0, 13.0, 11.0, 12.0, 11.0, 11.0, 11.0, 13.0, 12.0, 12.0, 11.0, 10.0, 11.0, 11.0, 11.0, 12.0, 12.0, 12.0, 12.0, 12.0, 11.0, 11.0, 12.0, 13.0, 11.0, 10.0, 10.0, 11.0, 11.0, 12.0, 12.0, 11.0, 11.0, 11.0, 11.0, 13.0, 11.0, 12.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 12.0, 12.0, 10.0, 11.0, 10.0, 11.0, 13.0, 13.0, 12.0, 18.0, 12.0, 12.0, 12.0, 11.0, 12.0, 13.0, 13.0, 13.0, 13.0, 12.0, 13.0, 13.0, 10.0, 12.0, 10.0, 12.0, 18.0, 10.0, 10.0, 10.0, 12.0, 12.0, 13.0, 13.0, 11.0, 12.0, 13.0, 13.0, 12.0, 12.0, 14.0, 13.0, 15.0, 13.0, 15.0, 15.0, 18.0, 15.0, 13.0, 18.0, 12.0, 12.0, 12.0, 12.0, 13.0, 13.0, 11.0, 12.0, 11.0, 12.0, 11.0, 11.0, 12.0, 11.0, 12.0, 11.0, 10.0, 14.0, 11.0, 15.0, 11.0, 16.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 11.0, 11.0, 11.0, 13.0, 12.0, 12.0, 11.0, 13.0, 14.0, 13.0, 12.0, 12.0, 11.0, 12.0, 11.0, 13.0, 12.0, 13.0, 11.0, 14.0, 13.0, 13.0, 12.0, 12.0, 11.0, 12.0, 11.0, 12.0, 11.0, 13.0, 15.0, 13.0, 13.0, 10.0, 10.0, 11.0, 12.0, 12.0, 11.0, 13.0, 13.0, 13.0, 14.0, 12.0, 12.0, 14.0, 12.0, 11.0, 12.0, 11.0, 11.0, 11.0, 10.0, 11.0, 12.0, 15.0, 11.0, 12.0, 12.0, 12.0, 11.0, 13.0, 12.0, 13.0, 11.0, 13.0, 12.0, 12.0, 13.0, 11.0, 12.0, 12.0, 12.0, 12.0, 19.0, 12.0, 13.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 11.0, 11.0, 10.0, 11.0, 10.0, 12.0, 10.0, 12.0, 10.0, 11.0, 11.0, 12.0, 12.0, 11.0, 12.0, 11.0, 12.0, 12.0, 12.0, 10.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 13.0, 12.0, 13.0, 10.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 12.0, 13.0, 15.0, 12.0, 12.0, 12.0, 12.0, 11.0, 11.0, 10.0, 11.0, 11.0, 12.0, 11.0, 12.0, 11.0, 13.0, 12.0, 13.0, 13.0, 12.0, 14.0, 12.0, 12.0, 12.0, 12.0, 11.0, 11.0, 11.0, 12.0, 11.0, 11.0, 10.0, 11.0, 10.0, 14.0, 17.0, 13.0, 14.0, 17.0, 20.0, 13.0, 13.0, 15.0, 13.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 11.0, 14.0, 12.0, 11.0, 11.0, 11.0, 11.0, 13.0, 13.0, 13.0, 10.0, 13.0, 22.0, 16.0, 15.0, 14.0, 39.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 11.0, 12.0, 10.0, 11.0, 13.0, 10.0, 13.0, 11.0, 12.0, 12.0, 12.0, 11.0, 12.0, 12.0, 13.0, 15.0, 11.0, 10.0, 12.0, 12.0, 12.0, 12.0, 13.0, 13.0, 12.0, 11.0, 11.0, 11.0, 11.0, 13.0, 12.0, 12.0, 15.0, 13.0, 11.0, 14.0, 13.0, 13.0, 13.0, 12.0, 12.0, 12.0, 12.0, 13.0, 12.0, 12.0, 13.0, 15.0, 14.0, 15.0, 13.0, 14.0, 17.0, 18.0, 16.0, 14.0, 15.0, 20.0, 14.0, 22.0, 15.0, 17.0, 12.0, 12.0, 12.0, 11.0, 11.0, 14.0, 11.0, 12.0, 10.0, 11.0, 11.0, 11.0, 11.0, 11.0, 12.0, 11.0, 11.0, 12.0, 11.0, 12.0, 10.0, 14.0, 10.0, 12.0, 12.0, 12.0, 12.0, 12.0, 14.0, 11.0, 12.0, 11.0, 11.0, 11.0, 11.0, 13.0, 12.0, 12.0, 11.0, 10.0, 11.0, 10.0, 11.0, 10.0, 12.0, 10.0, 12.0, 10.0, 11.0, 12.0, 12.0, 12.0, 12.0, 11.0, 11.0, 11.0, 11.0, 12.0, 11.0, 12.0, 12.0, 12.0, 14.0, 14.0, 12.0, 12.0, 11.0, 12.0, 10.0, 11.0, 11.0, 13.0, 11.0, 12.0, 11.0, 13.0, 12.0, 14.0, 11.0, 11.0, 12.0, 12.0, 11.0, 12.0, 13.0, 12.0, 12.0, 13.0, 11.0, 13.0, 14.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 10.0, 12.0, 11.0, 11.0, 11.0, 12.0, 11.0, 11.0, 13.0, 12.0, 12.0, 12.0, 14.0, 12.0, 12.0, 14.0, 12.0, 12.0, 12.0, 12.0, 14.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 11.0, 11.0, 12.0, 11.0, 12.0, 11.0, 13.0, 11.0, 13.0, 12.0, 12.0, 13.0, 13.0, 13.0, 11.0, 10.0, 12.0, 12.0, 11.0, 11.0, 12.0, 12.0, 12.0, 12.0, 11.0, 12.0, 12.0, 11.0, 11.0, 11.0, 11.0, 12.0, 11.0, 10.0, 14.0, 13.0, 14.0, 15.0])
middle_cop = np.array([23.0, 13.0, 29.0, 24.0, 22.0, 25.0, 24.0, 35.0, 28.0, 28.0, 25.0, 29.0, 27.0, 28.0, 26.0, 33.0, 25.0, 41.0, 24.0, 27.0, 27.0, 44.0, 24.0, 35.0, 25.0, 38.0, 25.0, 30.0, 22.0, 17.0, 37.0, 51.0, 40.0, 56.0, 22.0, 53.0, 24.0, 47.0, 32.0, 78.0, 29.0, 82.0, 30.0, 85.0, 14.0, 59.0, 20.0, 87.0, 27.0, 36.0, 27.0, 40.0, 27.0, 29.0, 23.0, 18.0, 15.0, 9.0, 12.0, 11.0, 16.0, 13.0, 14.0, 16.0, 15.0, 16.0, 22.0, 24.0, 21.0, 16.0, 19.0, 16.0, 17.0, 21.0, 18.0, 16.0, 11.0, 13.0, 12.0, 15.0, 29.0, 15.0, 26.0, 14.0, 10.0, 21.0, 10.0, 16.0, 9.0, 14.0, 12.0, 12.0, 20.0, 11.0, 17.0, 12.0, 23.0, 16.0, 25.0, 9.0, 15.0, 10.0, 19.0, 11.0, 15.0, 11.0, 15.0, 11.0, 23.0, 16.0, 28.0, 20.0, 29.0, 22.0, 28.0, 18.0, 27.0, 23.0, 30.0, 21.0, 23.0, 13.0, 23.0, 20.0, 21.0, 21.0, 21.0, 15.0, 20.0, 15.0, 21.0, 14.0, 16.0, 11.0, 21.0, 15.0, 14.0, 14.0, 17.0, 14.0, 15.0, 16.0, 16.0, 14.0, 21.0, 16.0, 16.0, 10.0, 29.0, 11.0, 10.0, 9.0, 10.0, 13.0, 10.0, 9.0, 10.0, 10.0, 12.0, 15.0, 13.0, 12.0, 17.0, 13.0, 15.0, 11.0, 22.0, 14.0, 19.0, 17.0, 13.0, 29.0, 20.0, 22.0, 24.0, 23.0, 29.0, 20.0, 31.0, 19.0, 9.0, 16.0, 8.0, 27.0, 8.0, 9.0, 8.0, 20.0, 6.0, 25.0, 7.0, 15.0, 27.0, 13.0, 14.0, 17.0, 13.0, 14.0, 7.0, 19.0, 8.0, 14.0, 23.0, 23.0, 11.0, 35.0, 11.0, 25.0, 10.0, 43.0, 8.0, 16.0, 8.0, 27.0, 8.0, 9.0, 8.0, 20.0, 7.0, 27.0, 7.0, 15.0, 27.0, 14.0, 13.0, 17.0, 12.0, 14.0, 7.0, 16.0, 7.0, 12.0, 24.0, 25.0, 10.0, 36.0, 11.0, 25.0, 10.0, 43.0, 10.0, 12.0, 13.0, 11.0, 21.0, 13.0, 27.0, 13.0, 28.0, 17.0, 25.0, 21.0, 12.0, 13.0, 13.0, 15.0, 14.0, 19.0, 11.0, 9.0, 19.0, 10.0, 30.0, 9.0, 10.0, 27.0, 10.0, 12.0, 11.0, 20.0, 15.0, 11.0, 13.0, 10.0, 13.0, 9.0, 12.0, 9.0, 12.0, 11.0, 12.0, 10.0, 14.0, 9.0, 18.0, 9.0, 17.0, 11.0, 16.0, 14.0, 17.0, 12.0, 21.0, 11.0, 24.0, 7.0, 18.0, 11.0, 18.0, 15.0, 12.0, 15.0, 11.0, 9.0, 14.0, 8.0, 11.0, 8.0, 15.0, 8.0, 12.0, 7.0, 12.0, 11.0, 11.0, 8.0, 15.0, 10.0, 14.0, 25.0, 20.0, 16.0, 17.0, 12.0, 17.0, 11.0, 25.0, 9.0, 13.0, 19.0, 30.0, 26.0, 24.0, 56.0, 27.0, 25.0, 29.0, 25.0, 33.0, 18.0, 38.0, 49.0, 25.0, 14.0, 14.0, 16.0, 15.0, 16.0, 19.0, 13.0, 20.0, 14.0, 14.0, 16.0, 15.0, 53.0, 14.0, 20.0, 18.0, 32.0, 36.0, 24.0, 30.0, 19.0, 17.0, 29.0, 25.0, 13.0, 20.0, 11.0, 13.0, 25.0, 15.0, 11.0, 16.0, 12.0, 21.0, 11.0, 12.0, 9.0, 8.0, 10.0, 12.0, 9.0, 19.0, 8.0, 18.0, 9.0, 9.0, 8.0, 12.0, 14.0, 12.0, 11.0, 12.0, 10.0, 18.0, 13.0, 17.0, 13.0, 20.0, 37.0, 18.0, 40.0, 23.0, 41.0, 23.0, 32.0, 21.0, 29.0, 16.0, 24.0, 13.0, 16.0, 12.0, 14.0, 14.0, 23.0, 12.0, 25.0, 18.0, 16.0, 22.0, 21.0, 17.0, 11.0, 23.0, 13.0, 19.0, 15.0, 19.0, 21.0, 25.0, 15.0, 13.0, 27.0, 12.0, 11.0, 27.0, 12.0, 20.0, 11.0, 14.0, 10.0, 11.0, 12.0, 11.0, 12.0, 14.0, 11.0, 14.0, 11.0, 13.0, 9.0, 14.0, 9.0, 12.0, 11.0, 17.0, 14.0, 20.0, 17.0, 21.0, 13.0, 17.0, 15.0, 15.0, 20.0, 21.0, 19.0, 25.0, 13.0, 27.0, 15.0, 23.0, 22.0, 24.0, 18.0, 25.0, 11.0, 14.0, 10.0, 10.0, 12.0, 15.0, 13.0, 10.0, 15.0, 13.0, 16.0, 15.0, 22.0, 10.0, 13.0, 9.0, 11.0, 10.0, 10.0, 10.0, 10.0, 10.0, 15.0, 10.0, 10.0, 9.0, 23.0, 10.0, 10.0, 17.0, 10.0, 25.0, 23.0, 21.0, 17.0, 24.0, 15.0, 46.0, 15.0, 34.0, 16.0, 50.0, 16.0, 55.0, 14.0, 33.0, 19.0, 45.0, 17.0, 16.0, 15.0, 23.0, 12.0, 13.0, 37.0, 16.0, 26.0, 13.0, 10.0, 13.0, 14.0, 10.0, 15.0, 12.0, 11.0, 10.0, 8.0, 10.0, 9.0, 10.0, 8.0, 12.0, 9.0, 13.0, 10.0, 12.0, 8.0, 12.0, 7.0, 23.0, 15.0, 20.0, 15.0, 26.0, 9.0, 12.0, 19.0, 13.0, 12.0, 23.0, 15.0, 8.0, 6.0, 8.0, 5.0, 10.0, 6.0, 7.0, 5.0, 10.0, 5.0, 6.0, 6.0, 26.0, 6.0, 6.0, 6.0, 6.0, 11.0, 6.0, 6.0, 7.0, 5.0, 6.0, 5.0, 5.0, 5.0, 6.0, 4.0, 5.0, 6.0, 15.0, 12.0, 14.0, 13.0, 15.0, 12.0, 16.0, 12.0, 15.0, 13.0, 14.0, 12.0, 11.0, 11.0, 12.0, 13.0, 21.0, 13.0, 29.0, 15.0, 26.0, 11.0, 11.0, 13.0, 9.0, 15.0, 9.0, 17.0, 8.0, 23.0, 20.0, 26.0, 12.0, 31.0, 14.0, 20.0, 18.0, 32.0, 13.0, 35.0, 16.0, 18.0, 16.0, 35.0, 13.0, 44.0, 12.0, 45.0, 13.0, 14.0, 12.0, 14.0, 18.0, 18.0, 19.0, 22.0, 15.0, 27.0, 15.0, 25.0, 15.0, 17.0, 16.0, 17.0, 18.0, 20.0, 17.0, 21.0, 20.0, 23.0, 23.0, 20.0, 37.0, 27.0, 21.0, 31.0, 22.0, 30.0, 19.0, 32.0, 28.0, 25.0, 32.0, 27.0, 13.0, 29.0, 12.0, 29.0, 19.0, 25.0, 17.0, 13.0, 15.0, 21.0, 15.0, 17.0, 14.0, 20.0, 14.0, 17.0, 14.0, 19.0, 19.0, 31.0, 15.0, 37.0, 12.0, 12.0, 12.0, 17.0, 13.0, 16.0, 14.0, 10.0, 13.0, 12.0, 13.0, 12.0, 12.0, 12.0, 16.0, 17.0, 15.0, 18.0, 17.0, 20.0, 18.0, 22.0, 18.0, 30.0, 20.0, 21.0, 17.0, 26.0, 23.0, 26.0, 22.0, 35.0, 23.0, 38.0, 19.0, 51.0, 15.0, 24.0, 15.0, 18.0, 15.0, 17.0, 13.0, 18.0, 19.0, 23.0, 31.0, 29.0, 33.0, 19.0, 27.0, 21.0, 34.0, 35.0, 38.0, 19.0, 43.0, 19.0, 42.0, 36.0, 42.0, 19.0, 26.0, 20.0, 42.0, 16.0, 43.0, 20.0, 26.0, 22.0, 41.0, 20.0, 46.0, 14.0, 14.0, 11.0, 21.0, 15.0, 13.0, 12.0, 33.0, 12.0, 18.0, 12.0, 13.0, 14.0, 12.0, 8.0, 10.0, 22.0, 9.0, 23.0, 11.0, 8.0, 10.0, 9.0, 10.0, 13.0, 11.0, 15.0, 11.0, 16.0, 10.0, 16.0, 14.0, 13.0, 14.0, 11.0, 11.0, 12.0, 11.0, 15.0, 12.0, 20.0, 15.0, 18.0, 16.0, 14.0, 14.0, 17.0, 14.0, 17.0, 12.0, 24.0, 14.0, 17.0, 16.0, 16.0, 16.0, 14.0, 18.0, 16.0, 24.0, 16.0, 11.0, 11.0, 23.0, 12.0, 11.0, 11.0, 23.0, 11.0, 16.0, 11.0, 10.0, 11.0, 18.0, 11.0, 21.0, 12.0, 12.0, 12.0, 11.0, 11.0, 13.0, 21.0, 12.0, 20.0, 12.0, 13.0, 23.0, 13.0, 12.0, 13.0, 15.0, 13.0, 21.0, 10.0, 13.0, 12.0, 14.0, 14.0, 11.0, 14.0, 12.0, 11.0, 14.0, 12.0, 16.0, 14.0, 16.0, 12.0, 11.0, 16.0, 19.0, 17.0, 10.0, 19.0, 13.0, 18.0, 11.0, 20.0, 13.0, 15.0, 22.0, 10.0, 22.0, 26.0, 22.0, 20.0, 22.0, 21.0, 29.0, 23.0, 31.0, 9.0, 12.0, 8.0, 18.0, 11.0, 11.0, 11.0])
end_cop = np.array([17.0, 15.0, 25.0, 13.0, 27.0, 17.0, 36.0, 12.0, 37.0, 7.0, 24.0, 8.0, 23.0, 9.0, 24.0, 9.0, 34.0, 5.0, 15.0, 5.0, 34.0, 21.0, 36.0, 31.0, 37.0, 5.0, 12.0, 6.0, 29.0, 5.0, 7.0, 15.0, 9.0, 16.0, 60.0, 17.0, 147.0, 17.0, 59.0, 17.0, 7.0, 40.0, 116.0, 41.0, 5.0, 8.0, 4.0, 16.0, 75.0, 10.0, 131.0, 9.0, 6.0, 10.0, 8.0, 6.0, 14.0, 4.0, 21.0, 4.0, 7.0, 12.0, 11.0, 13.0, 13.0, 14.0, 6.0, 6.0, 6.0, 9.0, 7.0, 5.0, 12.0, 5.0, 6.0, 18.0, 4.0, 22.0, 60.0, 21.0, 5.0, 3.0, 6.0, 4.0, 4.0, 4.0, 9.0, 3.0, 16.0, 3.0, 7.0, 14.0, 4.0, 4.0, 30.0, 4.0, 45.0, 3.0, 3.0, 2.0, 2.0, 3.0, 5.0, 2.0, 12.0, 2.0, 3.0, 5.0, 2.0, 2.0, 4.0, 2.0, 10.0, 3.0, 3.0, 9.0, 3.0, 7.0, 22.0, 7.0, 9.0, 9.0, 8.0, 9.0, 8.0, 8.0, 10.0, 7.0, 8.0, 8.0, 9.0, 16.0, 8.0, 21.0, 8.0, 17.0, 8.0, 42.0, 6.0, 9.0, 7.0, 6.0, 8.0, 6.0, 7.0, 6.0, 12.0, 11.0, 9.0, 11.0, 1.0, 18.0, 1.0, 2.0, 22.0, 1.0, 9.0, 1.0, 2.0, 17.0, 2.0, 1.0, 2.0, 6.0, 2.0, 2.0, 2.0, 7.0, 2.0, 2.0, 5.0, 2.0, 2.0, 3.0, 2.0, 15.0, 2.0, 1.0, 9.0, 1.0, 12.0, 21.0, 33.0, 24.0, 13.0, 15.0, 10.0, 26.0, 33.0, 27.0, 10.0, 17.0, 13.0, 15.0, 13.0, 22.0, 15.0, 23.0, 21.0, 16.0, 21.0, 20.0, 18.0, 22.0, 21.0, 17.0, 22.0, 14.0, 19.0, 22.0, 35.0, 11.0, 25.0, 10.0, 43.0, 10.0, 62.0, 12.0, 68.0, 12.0, 79.0, 9.0, 12.0, 9.0, 11.0, 9.0, 10.0, 11.0, 11.0, 15.0, 13.0, 16.0, 17.0, 13.0, 10.0, 13.0, 34.0, 11.0, 35.0, 13.0, 4.0, 4.0, 3.0, 4.0, 4.0, 7.0, 3.0, 17.0, 4.0, 16.0, 4.0, 33.0, 5.0, 21.0, 9.0, 17.0, 12.0, 20.0, 12.0, 16.0, 20.0, 12.0, 9.0, 22.0, 10.0, 51.0, 1.0, 32.0, 19.0, 31.0, 24.0, 27.0, 25.0, 32.0, 20.0, 33.0, 19.0, 42.0, 19.0, 29.0, 19.0, 25.0, 17.0, 14.0, 16.0, 47.0, 25.0, 12.0, 32.0, 13.0, 96.0, 32.0, 26.0, 29.0, 12.0, 35.0, 25.0, 31.0, 3.0, 9.0, 5.0, 5.0, 4.0, 5.0, 15.0, 4.0, 3.0, 6.0, 4.0, 4.0, 11.0, 44.0, 1.0, 9.0, 6.0, 5.0, 6.0, 5.0, 3.0, 34.0, 2.0, 7.0, 2.0, 6.0, 4.0, 1.0, 1.0, 1.0, 39.0, 1.0, 5.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 74.0, 7.0, 2.0, 72.0, 1.0, 3.0, 29.0, 2.0, 5.0, 4.0, 2.0, 14.0, 2.0, 16.0, 3.0, 3.0, 46.0, 3.0, 43.0, 6.0, 5.0, 5.0, 3.0, 2.0, 9.0, 4.0, 4.0, 3.0, 77.0, 2.0, 5.0, 4.0, 3.0, 4.0, 5.0, 2.0, 7.0, 3.0, 3.0, 3.0, 4.0, 3.0, 7.0, 4.0, 1.0, 5.0, 1.0, 1.0, 1.0, 3.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 17.0, 9.0, 17.0, 6.0, 2.0, 1.0, 15.0, 2.0, 2.0, 30.0, 2.0, 1.0, 2.0, 2.0, 3.0, 13.0, 2.0, 12.0, 21.0, 13.0, 29.0, 13.0, 48.0, 13.0, 14.0, 15.0, 17.0, 24.0, 14.0, 20.0, 14.0, 22.0, 16.0, 19.0, 15.0, 25.0, 22.0, 32.0, 19.0, 50.0, 24.0, 44.0, 33.0, 18.0, 32.0, 14.0, 43.0, 3.0, 2.0, 37.0, 2.0, 3.0, 2.0, 2.0, 2.0, 6.0, 2.0, 3.0, 4.0, 4.0, 4.0, 3.0, 46.0, 4.0, 2.0, 2.0, 49.0, 1.0, 62.0, 17.0, 17.0, 15.0, 58.0, 1.0, 59.0, 2.0, 45.0, 7.0, 5.0, 7.0, 12.0, 8.0, 4.0, 5.0, 2.0, 2.0, 2.0, 2.0, 27.0, 1.0, 2.0, 8.0, 2.0, 13.0, 2.0, 17.0, 3.0, 1.0, 1.0, 1.0, 3.0, 1.0, 1.0, 3.0, 1.0, 1.0, 1.0, 15.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 16.0, 2.0, 33.0, 7.0, 1.0, 2.0, 45.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 44.0, 4.0, 5.0, 4.0, 3.0, 13.0, 3.0, 47.0, 3.0, 44.0, 3.0, 2.0, 2.0, 1.0, 6.0, 1.0, 3.0, 2.0, 9.0, 2.0, 5.0, 2.0, 5.0, 3.0, 7.0, 17.0, 8.0, 1.0, 2.0, 12.0, 3.0, 4.0, 2.0, 3.0, 40.0, 5.0, 2.0, 3.0, 2.0, 13.0, 17.0, 10.0, 7.0, 58.0, 7.0, 16.0, 8.0, 2.0, 2.0, 2.0, 2.0, 3.0, 1.0, 1.0, 8.0, 1.0, 1.0, 1.0, 1.0, 1.0, 5.0, 14.0, 7.0, 2.0, 7.0, 2.0, 6.0, 6.0, 5.0, 2.0, 15.0, 1.0, 3.0, 1.0, 2.0, 8.0, 16.0, 7.0, 5.0, 6.0, 8.0, 6.0, 8.0, 6.0, 5.0, 9.0, 5.0, 4.0, 6.0, 4.0, 11.0, 5.0, 26.0, 6.0, 5.0, 22.0, 5.0, 30.0, 3.0, 44.0, 3.0, 5.0, 5.0, 44.0, 40.0, 15.0, 45.0, 21.0, 31.0, 16.0, 18.0, 14.0, 14.0, 26.0, 11.0, 14.0, 11.0, 13.0, 12.0, 14.0, 13.0, 15.0, 14.0, 13.0, 21.0, 15.0, 21.0, 14.0, 16.0, 14.0, 15.0, 12.0, 18.0, 12.0, 1.0, 16.0, 1.0, 27.0, 1.0, 5.0, 1.0, 15.0, 2.0, 5.0, 8.0, 5.0, 2.0, 11.0, 1.0, 13.0, 6.0, 12.0, 94.0, 14.0, 17.0, 16.0, 15.0, 25.0, 16.0, 29.0, 18.0, 16.0, 16.0, 33.0, 16.0, 29.0, 18.0, 22.0, 17.0, 22.0, 13.0, 20.0, 13.0, 18.0, 14.0, 15.0, 17.0, 19.0, 20.0, 22.0, 12.0, 21.0, 10.0, 20.0, 16.0, 37.0, 23.0, 36.0, 33.0, 39.0, 15.0, 22.0, 18.0, 20.0, 19.0, 30.0, 17.0, 35.0, 17.0, 40.0, 17.0, 45.0, 14.0, 22.0, 17.0, 25.0, 20.0, 19.0, 8.0, 12.0, 9.0, 20.0, 12.0, 37.0, 44.0, 9.0, 23.0, 9.0, 44.0, 5.0, 18.0, 7.0, 7.0, 7.0, 4.0, 24.0, 3.0, 15.0, 3.0, 2.0, 3.0, 2.0, 3.0, 8.0, 3.0, 39.0, 3.0, 14.0, 3.0, 13.0, 3.0, 2.0, 12.0, 5.0, 5.0, 45.0, 15.0, 27.0, 4.0, 3.0, 10.0, 3.0, 2.0, 25.0, 2.0, 3.0, 17.0, 1.0, 7.0, 1.0, 9.0, 1.0, 20.0, 1.0, 2.0, 1.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 17.0, 5.0, 6.0, 28.0, 6.0, 5.0, 16.0, 5.0, 4.0, 13.0, 4.0, 12.0, 4.0, 12.0, 4.0, 44.0, 5.0, 44.0, 13.0, 4.0, 12.0, 3.0, 9.0, 4.0, 10.0, 4.0, 3.0, 4.0, 2.0, 2.0, 1.0, 22.0, 34.0, 34.0, 33.0, 23.0, 16.0, 22.0, 29.0, 22.0, 23.0, 18.0, 26.0, 15.0, 20.0, 34.0, 25.0, 22.0, 23.0, 49.0, 24.0, 26.0, 28.0, 18.0, 29.0, 9.0, 14.0, 7.0, 29.0, 45.0, 6.0, 8.0, 21.0, 8.0, 31.0, 8.0, 36.0, 10.0, 40.0, 19.0, 47.0, 23.0, 19.0, 9.0, 19.0, 8.0, 26.0, 10.0, 9.0, 8.0, 25.0, 20.0, 26.0, 19.0, 19.0, 19.0, 18.0, 33.0, 11.0, 34.0, 5.0, 6.0, 6.0, 11.0, 8.0, 8.0, 9.0, 8.0, 6.0, 10.0, 5.0, 14.0, 5.0, 5.0, 4.0, 5.0, 4.0, 32.0, 4.0, 5.0, 7.0, 5.0, 4.0, 30.0, 4.0, 5.0, 47.0])
print(len(opening_cop))
print(len(middle_cop))
print(len(end_cop))
data = {
    'Opening': opening_cop,
    'Middle': middle_cop,
    'End': end_cop
}

# Calculate descriptive statistics
df = pd.DataFrame(data)
stats = df.describe()
print(stats)

# Calculate percentiles
for stage in data.keys():
    percentiles = np.percentile(df[stage], [25, 50, 75])
    print(f"{stage} percentiles: {percentiles}")

# Create histograms
fig, ax = plt.subplots(3, 1, figsize=(6, 9), sharex=True)
for i, stage in enumerate(data.keys()):
    ax[i].hist(df[stage], bins=10, alpha=0.5, color='blue')
    ax[i].set_title(f"{stage} CoP Distribution")
    ax[i].set_ylabel("Frequency")
plt.xlabel("CoP Value")
plt.tight_layout()
plt.show()

# Create box plots
fig, ax = plt.subplots(figsize=(6, 6))
df.boxplot(ax=ax)
plt.title("CoP Distributions for Different Stages")
plt.ylabel("CoP Value")
plt.show()
