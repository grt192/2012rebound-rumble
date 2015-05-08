class MechController:
	def __init__(self, chalupa, shooter, driver_joystick1, driver_joystick2, xbox_controller):
		self.chalupa = chalupa
		self.shooter = shooter
		self.driver_joystick1 = driver_joystick1
		self.driver_joystick2 = driver_joystick2
		self.xbox_controller = xbox_controller
		xbox_controller.add_listener(self._xbox_controller_listener)
		driver_joystick1.add_listener(self._driver_joystick1_listener)
		driver_joystick2.add_listener(self._driver_joystick2_listener)

	def _xbox_controller_listener(self, sensor, state_id, datum):
		if state_id == "b_button":
			if datum:
				self.shooter.start_flywheel()
				#self.shooter.start_hopper()
				
				print("B button pressed")

		if state_id == "a_button":
			if datum:
				self.shooter.stop_flywheel()
				#self.shooter.stop_hopper()
				print("A button pressed")

		if state_id == "y_button":
			if datum:
				self.chalupa.start_belt()
				self.shooter.start_hopper()
				
				print("Y button pressed")

		if state_id == "x_button":
			if datum:
				self.chalupa.stop_belt()
				self.shooter.stop_hopper()
				print("X button pressed")

		if state_id == 'l_x_axis':
			if datum:
				self.shooter.rotate(datum)

	def _driver_joystick1_listener(self, sensor, state_id, datum):
		if state_id == "trigger":
			if datum:
				self.chalupa.start_ep()
			else:
				self.chalupa.stop_ep()
		if state_id == "button3":
			if datum:
				self.chalupa.angle_change(0.5)
			else:
				self.chalupa.angle_change(0)
		if state_id == "button2":
			if datum:
				self.chalupa.angle_change(-0.5)
			else:
				self.chalupa.angle_change(0)

	def _driver_joystick2_listener(self, sensor, state_id, datum):
		if state_id == "trigger":
			if datum:
				self.chalupa.reverse_ep()
			else:
				self.chalupa.stop_ep()
