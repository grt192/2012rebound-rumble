import math

class Chalupa:
    def __init__(self, angle_change_motor, ep_motor, conveyor_motor, achange_power=0.6, ep_power=1, conveyor_power=1):
        self.angle_change_motor = angle_change_motor
        self.ep_motor = ep_motor
        self.conveyor_motor = conveyor_motor
        self.achange_power = achange_power
        self.ep_power = ep_power
        self.conveyor_power = conveyor_power


    def angle_change(self, power):
        """
        Set power of angle change. Power > 0 --> forwards.
        """
        self.angle_change_motor.set(power * self.achange_power if math.fabs(power) < 0.3 else 0)

    def start_ep(self):
        self.ep_motor.set(self.ep_power)
        self.conveyor_motor.set(self.conveyor_power)

    def reverse_ep(self):
        self.ep_motor.set(-self.ep_power)

    def stop_ep(self):
        self.ep_motor.set(0)
        self.conveyor_motor.set(0)

class Shooter:
    def __init__(self, hopper_motor, shooter_motor, turntable_motor, hopper_power=1, shooter_power=1, turntable_power=0.4):
        self.hopper_motor = hopper_motor
        self.shooter_motor = shooter_motor
        self.turntable_motor = turntable_motor
        self.hopper_power, self.shooter_power, self.turntable_power = hopper_power, shooter_power, turntable_power

    def rotate(self, power):
        self.turntable_motor.set(power * self.turntable_power if math.fabs(self.turntable_power) > 0.2 else 0)

    def start_flywheel(self):
        self.shooter_motor.set(self.shooter_power)

    def start_hopper(self):
        self.hopper_motor.set(self.hopper_power)

    def stop_flywheel(self):
        self.shooter_motor.set(0)

    def stop_hopper(self):
        self.hopper_motor.set(0)