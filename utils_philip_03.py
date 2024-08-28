''' ITERATION 3

Module: Underwater Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline should be used in every Python analytics project we do.

Process:

In this third iteration, I declare additional variables to show skills with different data types.

'''

#####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Boolean variable to indicate if the company is pet friendly
is_pet_friendly: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# Integer variable for the number of rescues at years_in_operation
has_been_rescued: int = 1 

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of strings representing SCUBA diving destinations
scuba_destinations: list = ["Bali", "Maldives", "Tubataha", "Cabo Pulmo"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# List of floats representing depths of recent dives in meters
scuba_depths_meters: list = [20.1, 32.6, 27.4, 18.3, 39.4]

#####################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------------
Underwater Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Is pet friendly:            {is_pet_friendly}
Years in Operation:         {years_in_operation}
Times Rescued at Sea:       {has_been_rescued}
Skills Offered:             {skills_offered}
Places to SCUBA             {scuba_destinations}
Client Satisfaction Scores: {client_satisfaction_scores}
Recent dive depths (meters):{scuba_depths_meters}
"""

#####################################
# Define the get_byline() Function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
    
