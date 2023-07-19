# Scraping_quotes_from_ULR

The overall goal of this project is to develop a tool that can automatically scrap quotes from provided URL address in .env file. Those quotes are caught and saved in the output file whose name is defined int a .env file. below is a pattern of the .env file
PROXY=
INPUT_URL=http:/example/url.com
OUTPUT_FILE= exampled_output_file_name

## Table of Contents
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Project Status](#project-status)

## Project Description
The objective of this project is to create a program that automatically scrapes all quotes from the website provided in your .env file,  including all quotes from subsequent pages. The program will then save the scraped data to a single JSONL (JSON Lines) file upon execution.

## Technologies Used
The following technologies and libraries are used in this project:
- Python
- JSON
- BeautifulSoup
- requests
- os
- load_dotenv
- time

## Setup
Before using this program you will be needed a .env file to provide the correct inputs to the program
To run the program, follow the steps below:

1. Install the required libraries in the path where is your ".env" and run.py files by using the following command:
 pip install -r requirements.txt

5. Test the trained model using the testing dataset.

6. Evaluate the model's performance using metrics such as confusion matrix, ROC curve, and accuracy.

## Usage

1. Create/paste .env file with mentioned variables in the dedicated path

2. Clone this repository or download the source code.

3. Download requirements.txt in the directory where is code and .env file

4. Install the required libraries by running
``` pip install -r requirements.txt ```

5. Run the project by command ``` python run.py ```


## Project Status
The project is done. The output.jsonl file has collected all quotes from provided ULR and extracted them to further use in other projects.
