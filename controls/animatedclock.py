import time
import random
from math import pi
from flet import (Stack,
                  Container,
                  Image,
                  ImageFit,
                  AnimationCurve,
                  animation,
                  transform,
                  alignment)


class AnimatedLock(Stack):
    def __init__(self, rotate_angle):
        super().__init__()
        self.rotate_angle = rotate_angle
        self.controls = [
                Container(
                    content=Image(
                        src="assets/Lock_frame.png",
                        fit=ImageFit.CONTAIN
                    ),
                    width=200,
                    height=200,
                    border_radius=100,
                    animate_rotation=animation.Animation(700, AnimationCurve.EASE_IN_OUT)
                ),
                Container(
                    content=Image(
                        src="assets/new_lock-0.png",
                        fit=ImageFit.CONTAIN
                    ),
                    width=164,
                    height=164,
                    border_radius=100,
                    offset=transform.Offset(0.11, 0.12),
                    rotate=transform.Rotate(self.rotate_angle, alignment=alignment.center),
                    animate_rotation=animation.Animation(700, AnimationCurve.EASE_IN_OUT)
                )
            ]

    def animate_lock(self):
        clock_wise_rotate = pi / 4
        lock = self.controls[1]
        counter = 0
        if counter == 0:
            while True:
                if 0 <= counter <= 3:
                    lock.rotate = transform.Rotate(
                        clock_wise_rotate, alignment=alignment.center
                    )
                    lock.update()

                    clock_wise_rotate += pi / 2
                    counter += 1
                    time.sleep(0.9)

                if 4 <= counter <= 8:
                    lock.rotate = transform.Rotate(
                        clock_wise_rotate, alignment=alignment.center
                    )
                    lock.update()

                    clock_wise_rotate -= pi / 2
                    counter += 1
                    time.sleep(0.9)
                if counter > 8:
                    counter = 0

