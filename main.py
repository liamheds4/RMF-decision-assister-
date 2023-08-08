# RMF Decider
INDUSTRY_WEIGHT = 2
ORG_SIZE_WEIGHT = 1

# NIST = {
#     "industry": {"finance": 5, "healthcare": 3...},
#     "size by employees": 
# }

# Do basic work to setup for the program.
def main():
    # Prompt user for input
    # - company name?
    # - industry (one of: finance | healthcare | tech)
    # - amount of sensitive datata being stored (PCI, SSN, etc.)
    # - what kinds of systems they use (workstations, mobile, remote, tbd..)
    # - Which employees/how they access
    # - are you privvy to government work/data
    #
    # Allen's suggestions
    # - Where they are located
    # - Size of company
    # - type of org (nonprofit, private, public, school, military)
    # - current security maturioty level
    # - current rmf?
    # - government regulations that affect them
    # - risk apetite
    #
    # Example:
    # risk_appetite_input = prompt("what is your risk apetite on level 1-10")
    # calculate_risk_app_level = int(risk_appetite_input)

    # Call helper functions to parse the input into quantifyable data

    # Bring all the data together into a struct

    # Make the decision based on the input info (and list next best alternatives)

    # Make visual based on the decision (matplotlib)

    # Prompt openai with input data and decisions to generate an explanation of the decision.

    print("whatever")


# Define the entrypoint into the 
if __name__ == "__main__":
    main()
