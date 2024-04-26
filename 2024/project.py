from intelino.trainlib import TrainScanner, Train
from intelino.trainlib.enums import SnapColorValue as C
from intelino.trainlib.enums import MovementDirection as M
from intelino.trainlib.enums import SteeringDecision as S
import time
from req import sendlog

pass_used_by = None

def random_speed():
    return 15


def handle_snap_commands(train, msg):
    global pass_used_by
    if msg.colors == (C.WHITE, C.MAGENTA, C.BLACK, C.BLACK):
        train.set_next_split_steering_decision(S.RIGHT)
        if pass_used_by is None:
            pass_used_by = train.alias
            sendlog(f"{train.alias} About to ENTER")
        elif pass_used_by != train.alias:
            # there's already a train in the pass
            sendlog(f"{train.alias} has to wait")
            train.stop_driving()
            while pass_used_by is not None:
                time.sleep(1)
            pass_used_by = train.alias
            train.drive_at_speed(random_speed(), direction=train.saved_direction)
            sendlog(f"{train.alias} entered after waiting")
    elif msg.colors == (C.WHITE, C.BLACK, C.BLACK, C.BLACK):
        train.set_next_split_steering_decision(S.LEFT)
        if pass_used_by is None:
            pass_used_by = train.alias
            sendlog(f"{train.alias} About to ENTER")
        elif pass_used_by != train.alias:
            # there's already a train in the pass
            sendlog(f"{train.alias} has to wait")
            train.stop_driving()
            while pass_used_by is not None:
                time.sleep(1)
            pass_used_by = train.alias
            train.drive_at_speed(random_speed(), direction=train.saved_direction)
            sendlog(f"{train.alias} entered after waiting")

def handle_colors(train, msg):
    global pass_used_by
    if msg.color == C.YELLOW:
        if pass_used_by == train.alias:
            pass_used_by = None
            sendlog(f"{train.alias} just Exited")
    elif msg.color == C.GREEN:
        if train.direction == M.FORWARD:
            train.drive_at_speed(random_speed(), direction=M.BACKWARD)
            train.saved_direction = M.BACKWARD
            sendlog(f"{train.alias} is reversing direction to Backward")
        elif train.direction == M.BACKWARD:
            train.drive_at_speed(random_speed(), direction=M.FORWARD)
            train.saved_direction = M.FORWARD
            sendlog(f"{train.alias} is reversing direction to Forward")

trains = TrainScanner().get_trains(count=2)

trains[0].alias = "Red Train"
trains[0].set_top_led_color(255, 0, 0)
trains[0].set_headlight_color(front=(255, 0, 0), back=(255, 0, 0))
trains[1].alias = "Green Train"
trains[1].set_top_led_color(0, 255, 0)
trains[1].set_headlight_color(front=(0, 255, 0), back=(0, 255, 0))

# setup event listener
for train in trains:
    train.clear_custom_snap_commands()
    train.add_snap_command_detection_listener(handle_snap_commands)
    # train.add_front_color_change_listener(handle_colors)

for train in trains:
    train.drive_at_speed(random_speed(), direction=M.FORWARD)
    train.saved_direction = M.FORWARD



_ = input("Press Enter to stop: ")

for train in trains:
    train.stop_driving()
    train.disconnect()
