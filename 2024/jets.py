from time import sleep
from intelino.trainlib import TrainScanner

trains = { "1": None, "2": None, "3": None, "4": None}


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


def stop_train(train_id):
    train = get_train(train_id)
    train.stop_driving()


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


def get_train(train_id):
    ids = {
        "1": "47AD4114-516E-06DE-2423-AA3632C162AE",
        "2": "0BB12C85-4837-D064-E2BE-D7C00685A30E",
        "3": "8036FE4C-5BDE-3618-1682-F36E693600CE",
        "4": "18701831-D35F-3C23-78AE-D5219AD32263"
    }
    if trains[train_id] is not None:
        return trains[train_id]
    train = TrainScanner().get_train(device_identifier=ids[train_id])
    return train


def scan():
    trains = TrainScanner(timeout=5).get_trains()
    for train in trains:
        print("Name:", train.name)
        print("ID:", train.id)
        print("Is connected:", train.is_connected)
        print("Current driving direction:", train.direction)
        print("Current speed [cm/s]:", train.speed_cmps)
        print("Next planned turn:", train.next_split_decision)
        print("Distance driven since connection [cm]:", train.distance_cm)


def identify(train_id):
    train = get_train(train_id)
    train.set_top_led_color(0, 255, 0)


if __name__ == "__main__":
    turn_train_4_light_on()
    sleep(2)
    turn_train_4_light_off()
