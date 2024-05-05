from intelino.trainlib import TrainScanner
from intelino.trainlib.enums import SnapColorValue as C
from intelino.trainlib.enums import MovementDirection as M
from intelino.trainlib.enums import SteeringDecision as S
from intelino.trainlib.train_scanner import TrainNotFoundError
import time
from req import sendlog, debug

stop_requested = False
pass_used_by = None
num_stopped = 0

JUNCTION_RIGHT = {"colors": (C.WHITE, C.MAGENTA), "direction": S.RIGHT}
JUNCTION_LEFT = {"colors": (C.WHITE, C.GREEN), "direction": S.LEFT}
JUNCTIONS = (JUNCTION_RIGHT, JUNCTION_LEFT)
REVERSE = (C.WHITE, C.RED)


def random_speed():
    return 15


def handle_snap_commands(train, msg):
    global pass_used_by, num_stopped
    # sendlog(msg.colors)
    for j in JUNCTIONS:
        if msg.colors == j['colors']:
            debug("MATCH!")
            train.set_next_split_steering_decision(j['direction'])
            if pass_used_by is None:
                pass_used_by = train.alias
                sendlog(f"<div class='log'>🟢 <span class='{train.c}'>{train.alias}</span> about to enter shared track</div>")
            elif pass_used_by == train.alias:
                pass_used_by = None
                sendlog(f"<div class='log'>🎉 <span class='{train.c}'>{train.alias}</span> just exited shared track</div>")
            else:
                sendlog(f"<div class='log'>🔴 <span class='{train.c}'>{train.alias}</span> has to wait</div>")
                train.stop_driving()
                while pass_used_by is not None:
                    time.sleep(0.25)
                pass_used_by = train.alias
                train.drive_at_speed(random_speed(), direction=train.saved_direction)
                sendlog(f"<div class='log'>🟢 <span class='{train.c}'>{train.alias}</span> entered shared track after waiting</div>")

            return
    if msg.colors == REVERSE:
        debug("REVERSE!")
        new_direction = M.FORWARD if train.direction == M.BACKWARD else M.BACKWARD
        if stop_requested and new_direction == M.FORWARD:
            debug("STOP!!!!")
            train.stop_driving()
            num_stopped += 1
            return

        train.drive_at_speed(random_speed(), direction=new_direction)
        train.saved_direction = new_direction
        sendlog(f"↩ {train.alias} is reversing direction")

trains = []

try:
    trains = TrainScanner().get_trains(count=2)

    trains[0].alias = "Red Train"
    trains[0].c = 'red'
    trains[0].set_top_led_color(255, 0, 0)
    trains[0].set_headlight_color(front=(255, 0, 0), back=(255, 0, 0))
    trains[1].alias = "Green Train"
    trains[0].c = 'green'
    trains[1].set_top_led_color(0, 255, 0)
    trains[1].set_headlight_color(front=(0, 255, 0), back=(0, 255, 0))

    # setup event listener
    for train in trains:
        train.clear_custom_snap_commands()
        train.add_snap_command_detection_listener(handle_snap_commands)

    for train in trains:
        train.drive_at_speed(random_speed(), direction=M.FORWARD)
        train.saved_direction = M.FORWARD

    _ = input("Press Enter to stop: ")
except TrainNotFoundError as e:
    print(e)
except KeyboardInterrupt:
    print("Cntr-C detected")


stop_requested = True

while num_stopped < len(trains):
    debug(f"{num_stopped=}")
    time.sleep(0.25)

for train in trains:
    train.clear_custom_snap_commands()
    train.disconnect()
