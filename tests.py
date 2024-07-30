import unittest
from unittest.mock import patch, MagicMock
import sys
import main

class TestMain(unittest.TestCase):

    @patch('main.OpenAI')
    @patch('builtins.input', side_effect=['chat', 'Hello', 'exit'])
    @patch('builtins.print')
    def test_chat_interaction(self, mock_print, mock_input, MockOpenAI):
        mock_client = MockOpenAI.return_value
        mock_client.chat.completions.create.return_value.choices[0].message.content = "Hi there!"

        with self.assertRaises(SystemExit):
            main.main()

        mock_client.chat.completions.create.assert_called_once_with(
            messages=[{"role": "user", "content": "Hello"}],
            model="gpt-3.5-turbo"
        )
        mock_print.assert_any_call("Hi there!")

    @patch('main.OpenAI')
    @patch('builtins.input', side_effect=['talk', 'Hello', 'exit'])
    @patch('builtins.print')
    def test_talk_interaction(self, mock_print, mock_input, MockOpenAI):
        mock_client = MockOpenAI.return_value
        mock_response = MagicMock()
        mock_client.audio.speech.create.return_value = mock_response

        with self.assertRaises(SystemExit):
            main.main()

        mock_client.audio.speech.create.assert_called_once_with(
            model="tts-1",
            voice="alloy",
            input="Hello"
        )
        mock_response.write_to_file.assert_called_once_with("example.mp3")

    @patch('main.OpenAI')
    @patch('builtins.input', side_effect=['exit'])
    @patch('builtins.print')
    def test_exit_interaction(self, mock_print, mock_input, MockOpenAI):
        with self.assertRaises(SystemExit):
            main.main()

    @patch('main.OpenAI')
    @patch('builtins.input', side_effect=['invalid', 'exit'])
    @patch('builtins.print')
    def test_invalid_interaction(self, mock_print, mock_input, MockOpenAI):
        with self.assertRaises(SystemExit):
            main.main()

        mock_print.assert_any_call("Sorry I don't understand.")

if __name__ == '__main__':
    unittest.main()