import logging
from streaming.twitch import TwitchStreamingService
from streaming.youtube import YouTubeStreamingService

def main() -> None:
    logging.basicConfig(level=logging.INFO)

    service = YouTubeStreamingService()