from typing import Callable


class Button:
    def is_pressed(self) -> bool: ...
    def was_pressed(self) -> bool: ...
    def presses(self) -> int: ...
    def callback(self, function: Callable[[int], None]) -> None: ...


left: Button
right: Button
center: Button
connect: Button
