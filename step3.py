#Step 1: Extract job details (industry, experience) from the CSV file.

import pandas as pd

file_path = 'C:/Users/rohin/Downloads/job_descriptions.csv'

# Extract job details function
def extract_job_details(job_id):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Print the column names to check what is available
    print("Columns in the DataFrame:", df.columns)

    # Extract specific columns like industry and experience
    job_details = df.loc[job_id, ['Industry', 'Experience']].to_dict()
    return job_details

job_id = 5  # Specific job identifier
job_details = extract_job_details(job_id)
industry = job_details['Industry']
experience = job_details['Experience']

print("Industry:", industry)
print("Experience:", experience)


#Step 2: Use those job details along with resume data to generate a prompt for relevance rating.
# Example Resume in JSON Format
resume_json = {
    "name": "John Doe",
    "experience": [
        {"title": "Software Engineer", "years": 3, "industry": "IT"},
        {"title": "Data Analyst", "years": 2, "industry": "Analytics"}
    ],
    "skills": ["Python", "SQL", "Machine Learning", "Tableau"]
}

# Create Prompt for Gemini with Separate Skills
def create_gemini_prompt(industry, experience, skills):
    prompt = f"""
    Compare the following job details with the given resume and rate the relevance.

    Job Details:
    - Industry: {industry}
    - Experience Required: {experience} years

    Candidate Resume:
    - Name: {resume_json.get('name', 'N/A')}
    - Total Experience: {sum([exp['years'] for exp in resume_json['experience']])} years
    - Key Skills: {', '.join(skills)}

    Compare the job details with the resume and give a relevance rating from 0 to 10.
    """
    return prompt

# Now include the separate skills input
skills_input = ["Python", "Machine Learning", "Data Analysis"]
gemini_prompt = create_gemini_prompt(industry, experience, skills_input)
# Print the generated Gemini prompt
print(gemini_prompt)

#Step 3: Send the prompt to the Gemini API and retrieve the response, which contains the relevance rating.
# import requests

# # Function to query Gemini API with the prompt
# def query_gemini(prompt):
#     # Replace with the actual Gemini API URL from the documentation
#     url = 'https://actual-gemini-api-url.com/query'  # Update this with the real Gemini API URL

#     # Replace 'YOUR_API_KEY_HERE' with your actual API key from Gemini
#     headers = {
#         'Authorization': 'Bearer YOUR_API_KEY_HERE',  # Bearer token for authentication
#         'Content-Type': 'application/json'  # Make sure the content type is JSON
#     }

#     # Prepare the request payload with the prompt
#     data = {
#         "prompt": prompt
#     }

#     try:
#         # Send a POST request to Gemini API
#         response = requests.post(url, headers=headers, json=data)

#         # Check if the request was successful
#         if response.status_code == 200:
#             return response.json()  # Return the JSON response from Gemini
#         else:
#             return {"error": f"Failed to get a response from Gemini, Status Code: {response.status_code}"}

#     except requests.exceptions.RequestException as e:
#         return {"error": str(e)}

# # Get relevance rating from Gemini
# relevance_response = query_gemini(gemini_prompt)

# # Print the result
# print("Relevance Rating:", relevance_response