import subprocess
import pandas as pd
import os

# Define the path to the executable
# Ensure that this path is exactly where the .exe file is located
executable_path = r'C:/Users/FazAri00/Desktop/qawork/QAPipeline/data/WebPrompt/WebPromptTester.exe'

# Check if the executable exists
if not os.path.exists(executable_path):
    raise FileNotFoundError(f"Executable not found at {executable_path}")

# Load the CSV file
file_path = r'\data\WebPrompt\Test-Web-vs-Bing-Search.csv'  # Ensure full path
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Extract the questions
questions = df['question'].tolist()

# Initialize a list to store the responses
responses = []

# Loop through each question, send it to the program, and capture the response
for question in questions:
    try:
        result = subprocess.run([executable_path, question], capture_output=True, text=True, check=True)
        response = result.stdout.strip()  # Read the output from the program
        responses.append({'Question': question, 'Answer': response})
    except subprocess.CalledProcessError as e:
        responses.append({'Question': question, 'Answer': f"Error: {str(e)}"})

# Add the responses back to the DataFrame
df['Automated Answer'] = [response['Answer'] for response in responses]

# Save the DataFrame to an Excel file
output_file = r'\data\WebPrompt\responses_with_automated_answers.xlsx'
df.to_excel(output_file, index=False)

print(f'Responses have been saved to {output_file}')
