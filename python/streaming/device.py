from typing import Protocol

from streaming.data import BufferData

class StreamingDevice(Protocol):
    def get_buffer_data(self) -> BufferData:
        ...