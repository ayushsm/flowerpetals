# import censusdata
import datetime
# import pandas
import plotly
import requests
# from bs4 import BeautifulSoup
import tabula

def chloropleth(df):
    fig = plotly.figure_factory.create_chloropleth(fips=["06001"], binning_endpoints=[10000], scope=["CA"], simplify_county=0, simplify_state=0)

def dataCreation(state):
    # Get the current year
    currYear = datetime.date.today().year

    # Iterate until the most recent census is found
    # YOUR CODE HERE (check on acs1 vs acs5, how search works)
    pdf_path = "countyvotes.pdf"
    df = tabula.read_pdf(pdf_path)

    chloropleth(df)
