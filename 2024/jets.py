from time import sleep
from intelino.trainlib import TrainScanner


def drive_train_1():
    drive_train("1")
    sleep(3)
    stop_train("1")


def drive_train_2():
    drive_train("2")
    sleep(3)
    stop_train("2")


def drive_train_3():
    drive_train("3")
    sleep(3)
    stop_train("3")


def drive_train_4():
    drive_train("4")
    sleep(3)
    stop_train("4")


def start_train_1():
    drive_train("1")


def start_train_2():
    drive_train("2")


def start_train_3():
    drive_train("3")


def start_train_4():
    drive_train("4")


def stop_train_1():
    stop_train("1")


def stop_train_2():
    stop_train("2")


def stop_train_3():
    stop_train("3")


def stop_train_4():
    stop_train("4")


def turn_train_1_light_on():
    turn_on_train_light("1")


def turn_train_1_light_off():
    turn_off_train_light("1")


def turn_train_2_light_on():
    turn_on_train_light("2")


def turn_train_2_light_off():
    turn_off_train_light("2")


def turn_train_3_light_on():
    turn_on_train_light("3")


def turn_train_3_light_off():
    turn_off_train_light("3")


def turn_train_4_light_on():
    turn_on_train_light("4")


def turn_train_4_light_off():
    turn_off_train_light("4")


def drive_train(train_id):
    train = get_train(train_id)
    train.drive_at_speed(30)
    train.disconnect()


def stop_train(train_id):
    train = get_train(train_id)
    train.stop_driving()
    train.disconnect()


def turn_on_train_light(train_id):
    colors = {
        "1": (255, 0, 0),
        "2": (0, 255, 0),
        "3": (0, 0, 255),
        "4": (255, 255, 0)
    }
    train = get_train(train_id)
    train.set_top_led_color(*colors[train_id])
    train.disconnect()


def turn_off_train_light(train_id):
    train = get_train(train_id)
    train.set_top_led_color(0, 0, 0)
    train.disconnect()


def get_train_1():
    return get_train(1)


def get_train_2():
    return get_train(2)


def get_train_3():
    return get_train(3)


def get_train_4():
    return get_train(4)


def get_train(train_id):
    str_train_id = str(train_id)

    ids = {
        "1": "00:A0:50:38:16:10",
        "2": "00:A0:50:B6:D8:76",
        "3": "00:A0:50:B6:56:E0",
        "4": "00:A0:50:E0:FB:20"
    }
    return TrainScanner().get_train(device_identifier=ids[str_train_id])


def scan():
    scanned_trains = TrainScanner(timeout=5).get_trains()
    for train in scanned_trains:
        print("Name:", train.name)
        print("ID:", train.id)
        print("Is connected:", train.is_connected)
        print("Current driving direction:", train.direction)
        print("Current speed [cm/s]:", train.speed_cmps)
        print("Next planned turn:", train.next_split_decision)
        print("Distance driven since connection [cm]:", train.distance_cm)
        train.disconnect()


def identify(train_id):
    train = get_train(train_id)
    train.set_top_led_color(0, 255, 0)


