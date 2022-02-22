import logging
from dataclasses import dataclass
from streaming.utils import generate_id, Buffer

@dataclass
class TwitchStreamingService:

    buffer: Buffer

    def start_stream(self) -> str:
        reference = generate_id()
        logging.info(f"Starting Twitch stream with reference: {reference}")
        return reference

    def fill_buffer(self, reference) -> None:
        data = self.buffer()
        logging.info(f"Received buffer data: {data}. Sending to Youtube stream: {reference}")

    def stop_stream(self, reference) -> None:
        logging.info(f"Closing Twitch stream with reference: {reference}")