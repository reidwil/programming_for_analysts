from typing import Protocol

class StreamingService(Protocol):
    def start_stream(self) -> str:
        ...
    
    def fill_buffer(self, reference: str) -> None:
        ...
    
    def stop_stream(self, reference: str) -> None:
        ...