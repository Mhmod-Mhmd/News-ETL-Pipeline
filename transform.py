import pandas as pd
import regex
from extract import extract


def transform_news(extracted_data):
    """ Function to transform news data using pandas"""

    # convert data from json to pandas dataframe
    df = pd.DataFrame(extracted_data)

    # removing tales and leading from all columns in dataframe
    df = df.apply(lambda x: x.str.strip() if x.astype == "object" else x)

    # fill null values with the corresponding indecies
    df["author"] = df["author"].fillna(df["source_name"])

    df["description"] = df["description"].fillna(df["title"])

    # Spliting published time column to date and time columns
    df["published_date"] = df["published_at"].str.slice(0, 10)
    df["published_time"] = df["published_at"].str.slice(11, 19)
    df.drop(columns= "published_at", inplace= True)

    # Extract web address from url column
    url_regex = r'^(?:https?://)?(?:www\.)?([^/]+)'

    web_address = []

    for url in df['url']:

        match = regex.search(url_regex, url)
        if match :
            domain = match.group(1)

            if 'www.' in url:
                web_address.append(f'www.{domain}')

            else:
                web_address.append(f'www.{domain}')

    df['web_address'] = web_address

    return df

