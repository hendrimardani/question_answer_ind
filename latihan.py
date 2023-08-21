# Import the library
import argparse
# Create the parser
parser = argparse.ArgumentParser(description="Model has been trained by Hendri Mardani")
# Add an argument
parser.add_argument('-f', '--file', type=str, required=True, help="Nama lu siapa")
# Parse the argument
args = parser.parse_args()
# Print "Hello" + the user input argument
if args.file == "hendri":
    print('Hello,', args.file)
else:
    print("wot")
