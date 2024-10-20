import swisseph as swe
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path to the ephemeris files
ephe_path = os.path.join(current_dir, "sweph", "ephe")

# Set the ephemeris path
swe.set_ephe_path(ephe_path)

print(f"Ephemeris path set to: {ephe_path}")

# Test if the path is set correctly by performing a calculation
julday = swe.julday(2023, 10, 20, 12.0)
xx, ret = swe.calc_ut(julday, swe.SUN)

if ret < 0:
    print(f"Error: {swe.get_errmsg(ret)}")
else:
    print(f"Sun's longitude on 2023-10-20: {xx[0]:.2f} degrees")

# List the files in the ephemeris directory
print("\nFiles in the ephemeris directory:")
for file in os.listdir(ephe_path):
    print(file)
