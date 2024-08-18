import streamlit as st
import json

st.title('Hello, Generate Cover Letters for any Visa!')
st.write('Use this application to generate cover letters for any of the following country\'s visa')

json_data = '''
{
    "items": {
        "1": {"name": "Schengen", "value": "Dear Sir/Madam,\\n\\nSubject: Application for Schengen Visa\\n\\nI am writing to apply for a Schengen Visa to visit [Schengen Country] for tourism purposes. I plan to travel from [start_date] to [End Date], during which I intend to visit.\\n\\nPurpose of Travel:\\nThe primary purpose of my visit is tourism. I have made all the necessary travel arrangements, including booking flights, accommodation, and travel insurance. Attached to this letter are copies of my flight itinerary, hotel reservations, and travel insurance policy. I have also included my detailed travel itinerary, which outlines my planned activities and visits during my stay.\\n\\nFinancial Means:\\nI am fully capable of covering all my travel expenses during my stay in the Schengen Area. I have attached copies of my bank statements and proof of employment to demonstrate my financial stability. Additionally, I have [mention any other financial support or sponsorship if applicable].\\n\\nTies to Home Country:\\nI assure you that I have strong ties to my home country, which will ensure my return after my trip. I am currently employed at [Your Company Name] as a [Your Job Title], and I have obtained approval for a leave of absence during the travel period. I have also attached a letter from my employer confirming my employment and the leave approval.\\n\\nConclusion:\\nI kindly request that you consider my application for a Schengen Visa. I am looking forward to exploring the culture, history, and natural beauty of [Schengen Country], and I assure you that I will abide by the laws and regulations during my stay. I intend to return to my home country after my visit, as per my travel itinerary.\\n\\nThank you for considering my application. Should you require any additional information or documents, please do not hesitate to contact me.\\n\\nYours faithfully \\n\\n[PAX Name]"},

        "2": {"name": "USA", "value": "Dear Sir/Madam,\\n\\nSubject: Application for USA Visa\\n\\nI am writing to apply for a Schengen Visa to visit [Schengen Country] for tourism purposes. I plan to travel from [Start Date] to [End Date], during which I intend to visit.\\n\\nPurpose of Travel:\\nThe primary purpose of my visit is tourism. I have made all the necessary travel arrangements, including booking flights, accommodation, and travel insurance. Attached to this letter are copies of my flight itinerary, hotel reservations, and travel insurance policy. I have also included my detailed travel itinerary, which outlines my planned activities and visits during my stay.\\n\\nFinancial Means:\\nI am fully capable of covering all my travel expenses during my stay in the Schengen Area. I have attached copies of my bank statements and proof of employment to demonstrate my financial stability. Additionally, I have [mention any other financial support or sponsorship if applicable].\\n\\nTies to Home Country:\\nI assure you that I have strong ties to my home country, which will ensure my return after my trip. I am currently employed at [Your Company Name] as a [Your Job Title], and I have obtained approval for a leave of absence during the travel period. I have also attached a letter from my employer confirming my employment and the leave approval.\\n\\nConclusion:\\nI kindly request that you consider my application for a Schengen Visa. I am looking forward to exploring the culture, history, and natural beauty of [Schengen Country], and I assure you that I will abide by the laws and regulations during my stay. I intend to return to my home country after my visit, as per my travel itinerary.\\n\\nThank you for considering my application. Should you require any additional information or documents, please do not hesitate to contact me.\\n\\nYours faithfully \\n\\n [PAX Name]"},

        "3": {"name": "Singapore", "value": "Dear Sir/Madam,\\n\\nSubject: Application for Singapore Visa\\n\\nI am writing to apply for a Schengen Visa to visit [Schengen Country] for tourism purposes. I plan to travel from [Start Date] to [End Date], during which I intend to visit.\\n\\nPurpose of Travel:\\nThe primary purpose of my visit is tourism. I have made all the necessary travel arrangements, including booking flights, accommodation, and travel insurance. Attached to this letter are copies of my flight itinerary, hotel reservations, and travel insurance policy. I have also included my detailed travel itinerary, which outlines my planned activities and visits during my stay.\\n\\nFinancial Means:\\nI am fully capable of covering all my travel expenses during my stay in the Schengen Area. I have attached copies of my bank statements and proof of employment to demonstrate my financial stability. Additionally, I have [mention any other financial support or sponsorship if applicable].\\n\\nTies to Home Country:\\nI assure you that I have strong ties to my home country, which will ensure my return after my trip. I am currently employed at [Your Company Name] as a [Your Job Title], and I have obtained approval for a leave of absence during the travel period. I have also attached a letter from my employer confirming my employment and the leave approval.\\n\\nConclusion:\\nI kindly request that you consider my application for a Schengen Visa. I am looking forward to exploring the culture, history, and natural beauty of [Schengen Country], and I assure you that I will abide by the laws and regulations during my stay. I intend to return to my home country after my visit, as per my travel itinerary.\\n\\nThank you for considering my application. Should you require any additional information or documents, please do not hesitate to contact me.\\n\\nYours faithfully \\n\\n [PAX Name]"}
    }
}
'''

# Parse JSON
data = json.loads(json_data)
items = data['items']

start_date = st.date_input('Enter Start Date:')
end_date = st.date_input('Enter End Date:')
pax_name = st.text_input('Passenger Name:')

# Create a dictionary of dropdown options
options = {key: value['name'] for key, value in items.items()}

# Create a dropdown
selected_name = st.selectbox('Choose an item:', list(options.values()))

# Find the key associated with the selected name
selected_key = [key for key, value in options.items() if value == selected_name][0]

# Display the selected item details
# st.write(f"**Selected Item:** {items[selected_key]['name']}")
# st.write(f"**Letter Content:**\n\n{items[selected_key]['value']}")

template = items[selected_key]['value']

if pax_name or start_date or end_date:
    updated_letter = template.replace('[start_date]', str(start_date))
    updated_letter = template.replace('[End Date]', str(end_date))
    updated_letter = template.replace('[PAX Name]', str(pax_name))

    # Display the dynamically generated letter
    st.write(f"**Generated Letter:**\n\n{updated_letter}")
else:
    st.write("Please fill in all fields to generate the letter.")
