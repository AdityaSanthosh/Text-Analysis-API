from collections import Counter

from flask import Flask, request, jsonify

from text_helper import remove_stop_words, write_to_csv, read_csv
from wikimedia_api import WikiMediaApi

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, User! Try /freq_analysis and /search_history endpoints"


@app.route("/freq_analysis")
def freq_analyser():
    topic = request.args.get("topic")
    n = request.args.get("n", default=10, type=int)

    if not topic:
        return jsonify({"error": "Missing required parameter: topic"}), 400

    text_content = WikiMediaApi().extracts(topic)

    filtered_words = remove_stop_words(text_content)
    word_counter = Counter(filtered_words)

    top_words = word_counter.most_common(n)

    top_words_json = {word[0]: word[1] for word in top_words}

    write_to_csv(topic, top_words_json)

    return jsonify({"content": text_content, "top_words": top_words_json}), 200


@app.route("/search_history")
def search_history():
    history_data = read_csv("search_history.csv")
    return jsonify({"search_history": history_data})


if __name__ == "__main__":
    app.run(debug=True)
