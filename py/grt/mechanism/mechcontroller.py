class MechController:
	def _init_(self, chalupa, shooter, driver_joystick1, driver_joystick2, xbox_controller):
		self.chalupa = chalupa
		self.shooter = shooter
		self.driver_joystick1 = driver_joystick1
		self.driver_joystick2 = driver_joystick2
		driver_joystick1.add_listener(self._driver_joystick1_listener)
		driver_joystick2.add_listener(self._driver_joystick2_listener)

	def _xbox_controller_listener(self, sensor, state_id, datum):
		if state_id == "b_button":
			if datum:
				self.shooter.start_flywheel
				self.shooter.start_hopper

		if state_id == "a_button":
			if datum:
				self.shooter.start_flywheel
				self.shooter.start_hopper

		if state_id == 'l_y_axis':
			if datum:
				self.shooter.rotate(datum)
				
				

