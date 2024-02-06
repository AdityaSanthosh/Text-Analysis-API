from bs4 import BeautifulSoup
import json
import csv


def format_html_content(content):
    """
    Parses text content from html and returns it
    :param content:
    :return:
    """
    soup = BeautifulSoup(content, "html.parser")
    text_content = soup.get_text().strip()
    return text_content


def remove_stop_words(text_content):
    """
    This function cleans up escaped characters, removes all the articles(a, an, the)
    and other stop words like in, at, be. This is essential step before natural language
    analysis on any piece of content
    :param text_content: any paragraph or text
    """
    import re
    import nltk

    nltk.download("stopwords")

    from nltk.corpus import stopwords

    text_content = (
        bytes(text_content, "utf-8").decode("unicode_escape").replace("\n", " ")
    )   # Parses escape sequences
    words = re.findall(r"\b\w+\b", text_content.lower())  # Sequences with more than 1 character count as a word
    stop_words = set(stopwords.words("english"))
    filtered_words = [
        word for word in words if (word not in stop_words and not word.isdigit())
    ]
    return filtered_words


def write_to_csv(topic, top_words):
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    filename = f"search_history.csv"

    with open(filename, mode="a+", newline="\n") as file:
        writer = csv.writer(file)

        writer.writerow([timestamp, topic, json.dumps(top_words)])


def read_csv(filename: str):
    result = []
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["freq_words"] = json.loads(row["freq_words"])
            result.append(row)
    return result
