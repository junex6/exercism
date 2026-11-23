from collections import deque

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self._elements = deque()

    def read(self):
        if not self._elements:
            raise BufferEmptyException("Circular buffer is empty")
        return self._elements.popleft()

    def write(self, data):
        if len(self._elements) < self.capacity:
            self._elements.append(data)
        else:
            raise BufferFullException("Circular buffer is full")

    def overwrite(self, data):
        if len(self._elements) < self.capacity:
            self._elements.append(data)
        else:
            self._elements.popleft()
            self._elements.append(data)

    def clear(self):
        self._elements.clear()
