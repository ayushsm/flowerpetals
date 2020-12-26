# import censusdata
import datetime
# import pandas
# import plotly
import requests
import census


# Have a dictionary to shorten bewteen states
STATECODES = {"AL": 1, "Alabama": 1,
              "AK": 2, "Alaska": 2,
              "AZ": 4, "Arizona": 4,
              "AR": 5, "Arkansas": 5,
              "CA": 6, "California": 6,
              "CO": 8, "Colorado": 8,
              "CT": 9, "Connecticut": 9,
              "DE": 10, "Delaware": 10,
              "DC": 11, "District of Columbia": 11,
              "FL": 12, "Florida": 12,
              "GA": 13, "Georgia": 13,
              "HI": 15, "Hawaii": 15,
              "ID": 16, "Idaho": 16,
              "IL": 17, "Illinois": 17,
              "IN": 18, "Indiana": 18,
              "IA": 19, "Iowa": 19,
              "KS": 20, "Kansas": 20,
              "KY": 21, "Kentucky": 21,
              "LA": 22, "Louisiana": 22,
              "ME": 23, "Maine": 23,
              "MD": 24, "Maryland": 24,
              "MA": 25, "Massachusetts": 25,
              "MI": 26, "Michigan": 26,
              "MN": 27, "Minnesota": 27,
              "MS": 28, "Mississippi": 28,
              "MO": 29, "Missouri": 29,
              "MT": 30, "Montana": 30,
              "NE": 31, "Nebraska": 31,
              "NV": 32, "Nevada": 32,
              "NH": 33, "New Hampshire": 33,
              "NJ": 34, "New Jersey": 34,
              "NM": 35, "New Mexico": 35,
              "NY": 36, "New York": 36,
              "NC": 37, "North Carolina": 37,
              "ND": 38, "North Dakota": 38,
              "OH": 39, "Ohio": 39,
              "OK": 40, "Oklahoma": 40,
              "OR": 41, "Oregon": 41,
              "PA": 42, "Pennsylvania": 42,
              "RI": 44, "Rhode Island": 44,
              "SC": 45, "South Carolina": 45,
              "SD": 46, "South Dakota": 46,
              "TN": 47, "Tennessee": 47,
              "TX": 48, "Texas": 48,
              "UT": 49, "Utah": 49,
              "VT": 50, "Vermont": 50,
              "VA": 51, "Virginia": 51,
              "WA": 53, "Washington": 53,
              "WV": 54, "West Virginia": 54,
              "WI": 55, "Wisconsin": 55,
              "WY": 56, "Wyoming": 56}


if __name__ == "__main__":
    # Ask for the state they'd like to map
    # state = input("Which state would you like to create districts for: ")
    state = "California"

    # Check it's an actual map and keep asking until they do
    while state not in STATECODES:
        state = input("You might have misspelled the state you're looking for. \
            Please put in the correct spelling: ")

    census.dataCreation(STATECODES[state])
