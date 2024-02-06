# Wikipedia Text Analysis API

## Introduction

This document provides documentation for the API and the tests implemented. The tests cover various endpoints and functionalities to ensure the proper functioning of the application.

## API

### Frequent Words endpoint

Provides word frequency analysis for a specified Wikipedia topic.

    Endpoint: /freq_analysis
    Method: GET

    Parameters:
    - topic (required): A string representing the subject of a Wikipedia article.
    - n (optional, default=10): An integer specifying the number of top frequent words to return.

    Response:
    Returns a JSON response with content and the top N most frequent words.

    Example:
    Request: GET /freq_analysis?topic=Python_(programming_language)&n=5
    Response: {"content": "...", "top_words": {"python": 210, "language": 40, ...}}
![Screenshot 2024-02-06 at 11.07.57 PM.png](Screenshot%202024-02-06%20at%2011.07.57%E2%80%AFPM.png)

## Search History Endpoint

Retrieves search history data from an external CSV file.

    Endpoint: /search_history
    Method: GET

    Response:
    Returns a JSON response with all the previous searches and their freq_words data.

    Example:
    Request: GET /search_history
    Response: {"search_history": [{"Timestamp": "...", "freq_words": {...}, "topic": "..."}, ...]}
    """
![Screenshot 2024-02-06 at 11.09.19 PM.png](Screenshot%202024-02-06%20at%2011.09.19%E2%80%AFPM.png)
## Running locally
### 0. Clone this repository to your local filesystem
### 1. Create a new virtual environment:

```bash
# On Windows
python -m venv venv

# On macOS/Linux
python3 -m venv venv
```
### 2. Activate the virtual environment
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
### 3. Start the server
```bash
# Run the Flask server
python main.py

# Ensure the Flask server is running at http://localhost:5000 or another specified address.
```

### 4. Start the Flask server:
```bash
For /freq_analysis:

Method: GET
URL: http://localhost:5000/freq_analysis?topic=YourTopic&n=5
For /search_history:

Method: GET
URL: http://localhost:5000/search_history
```

## Test Overview

The tests focus on the following endpoints and functionalities:

1. Testing `/freq_analysis` endpoint
2. Testing `/search_history` endpoint
3. Testing the history after freq_analysis is called

## Running Tests

To run the tests, execute the following command:

```bash
python -m unittest test_flask_api.py
