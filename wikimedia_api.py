from text_helper import format_html_content


class WikiMediaApi:
    def __init__(self):
        import requests

        self.base_url = "https://en.wikipedia.org/w/api.php"
        self._session = requests.Session()

    def extracts(self, topic, **kwargs) -> str:
        params = {
            "action": "query",
            "prop": "extracts",
            "titles": topic,
            "format": "json",
        }
        url = (
            self.base_url
            + "?"
            + "&".join([k + "=" + str(v) for k, v in params.items()])
        )

        r = self._session.get(url)
        data = r.json()
        if r.status_code != 200:
            raise "Failed to retrieve Wikipedia page"
        page_id = list(data["query"]["pages"].keys())[0]
        if int(page_id) < 0:
            return ""
        content = data["query"]["pages"][page_id]["extract"]
        return format_html_content(content)
