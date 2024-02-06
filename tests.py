import unittest
from main import app
import pandas as pd


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_analyse_endpoint(self):
        topic = 'kubernetes'
        response = self.app.get(f'/freq_analysis?topic={topic}&n=5')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn(topic.casefold(), data['content'].casefold())
        self.assertIn('top_words', data)
        self.assertIsInstance(data['top_words'], dict)

    def test_search_history_endpoint(self):
        response = self.app.get('/search_history')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('search_history', data)
        self.assertIsInstance(data['search_history'], list)

    def test_analyse_and_search_history(self):
        response_history = self.app.get('/search_history')
        history_before = response_history.get_json()
        historical_row_length = len(history_before['search_history'])

        topic = 'tesla'
        analysis_response = self.app.get(f'/freq_analysis?topic={topic}&n=5')
        self.assertEqual(analysis_response.status_code, 200)

        response_history = self.app.get('/search_history')
        history = response_history.get_json()

        # Check if a new row is added after /freq_analysis api is called and if the topic is matching
        self.assertEqual(history['search_history'][-1]['topic'], topic)
        self.assertEqual(historical_row_length + 1, len(history['search_history']))

    def tearDown(self):
        if self._testMethodName == 'test_analyse_and_search_history':
            # Remove the last added row from the CSV file
            filename = 'search_history.csv'
            df = pd.read_csv(filename)
            # Remove the last row (assuming the last row is the one added during the test)
            df = df.iloc[:-1]

            # Write the updated data back to the CSV file
            df.to_csv(filename, index=False)


if __name__ == '__main__':
    unittest.main()
