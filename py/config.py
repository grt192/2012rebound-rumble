"""
Config File for Robot
"""


from wpilib import DriverStation, Victor

from grt.sensors.attack_joystick import Attack3Joystick
from grt.sensors.xbox_joystick import XboxJoystick
from grt.sensors.gyro import Gyro
from grt.core import SensorPoller
from grt.mechanism.drivetrain import DriveTrain
from grt.mechanism.drivecontroller import TankDriveController
from grt.mechanism.motorset import Motorset
from grt.mechanism import Chalupa, Shooter
from grt.sensors.ticker import Ticker
from grt.sensors.encoder import Encoder
from grt.sensors.switch import Switch
from grt.mechanism.mechcontroller import MechController



LEFT_SIDECAR_MODULE = 1
RIGHT_SIDECAR_MODULE = 2

#Driver station components
primary_joystick = Attack3Joystick(1)
secondary_joystick = Attack3Joystick(2)
tertiary_joystick = XboxJoystick(3)





#Mechanism Encoders
turret_rotation_encoder = Encoder(5, 6, pulse_dist=4.0)
turret_visor_encoder = Encoder(7, 8, pulse_dist=4.0)

#Mechanism Victors
#wedge_victor = Victor(LEFT_SIDECAR_MODULE, 4)
ep = Victor(RIGHT_SIDECAR_MODULE, 3)
visor_victor = Victor(RIGHT_SIDECAR_MODULE, 4)
#flywheel_victor1 = Victor(RIGHT_SIDECAR_MODULE, 7)
#flywheel_victor2 = Victor(RIGHT_SIDECAR_MODULE, 8)
drawbridge_victor = Victor(RIGHT_SIDECAR_MODULE, 2)
conveyor = Victor(LEFT_SIDECAR_MODULE, 3)
hopper = Victor(LEFT_SIDECAR_MODULE, 2)
dt_right1 = Victor(LEFT_SIDECAR_MODULE, 4)
dt_right2 = Victor(LEFT_SIDECAR_MODULE, 5)
flywheel1 = Victor(LEFT_SIDECAR_MODULE, 6) #flywheel
flywheel2 = Victor(LEFT_SIDECAR_MODULE, 7)
bot_trans_victor2 = Victor(LEFT_SIDECAR_MODULE, 8)
rotation_victor = Victor(RIGHT_SIDECAR_MODULE, 1)


#Drivetrain Victors and encoders
 
left_encoder = Encoder(2, 1, pulse_dist=0.32)
right_encoder = Encoder(3, 4, pulse_dist=0.32)
#Third value is the pulse distance.

#dt_left = Motorset((Victor(LEFT_SIDECAR_MODULE, 9), Victor(LEFT_SIDECAR_MODULE, 10)), scalefactors=(-1, 1))
dt_right = Motorset((dt_right1, dt_right2), scalefactors=(1, -1))
dt_left = Motorset((Victor(LEFT_SIDECAR_MODULE, 9), Victor(LEFT_SIDECAR_MODULE, 10)), scalefactors=(1, -1))
#DT
dt = DriveTrain(dt_left, dt_right, left_encoder=left_encoder, right_encoder=right_encoder)



#Teleop Controllers
#ac = ArcadeDriveController(dt, primary_joystick)
tc = TankDriveController(dt, primary_joystick, secondary_joystick)

#VICTORS FOR MECHANISMS
 






#MECHANISM INTIALIZATION
 


collection_switch = Switch(LEFT_SIDECAR_MODULE,14)
upper_rollers_switch = Switch(LEFT_SIDECAR_MODULE,13)
hopper_switch = Switch(LEFT_SIDECAR_MODULE, 12)
ball_queue_switch = Switch(LEFT_SIDECAR_MODULE, 11)

flywheel_motors = Motorset((flywheel1, flywheel2))

#conveyor_motors = Motorset((conveyor1, conveyor2), scalefactors=(1, -1))

chalupa = Chalupa(drawbridge_victor, conveyor, ep)	
shooter = Shooter(hopper, flywheel_motors, rotation_victor)

mechcontroller = MechController(chalupa, shooter, primary_joystick, secondary_joystick, tertiary_joystick)

ds = DriverStation.GetInstance()



#Sensor Pollers
sp = SensorPoller((dt.right_encoder,
                   dt.left_encoder, turret_rotation_encoder, turret_visor_encoder))
hid_sp = SensorPoller((primary_joystick, secondary_joystick, tertiary_joystick))  # human interface devices


#End of ported pin map. All code in the large commented-out block is
#the old Java mechanism code.
"""
Wedge wedge = new Wedge(wedgeVictor, null, null, "Wedge");
wedge.start();
wedge.enable();
Drawbridge drawbridge = new Drawbridge(drawbridgeVictor, null, null, "DrawBridge");
drawbridge.start();
drawbridge.enable();

ShootingSystem ss = new ShootingSystem(rotationVictor, visorVictor,
        flywheelVictor1, flywheelVictor2,
        flailVictor1,
        topTransVictor1, topTransVictor2,
        botTransVictor1, botTransVictor2, 
        turretRotationEncoder, turretVisorEncoder);
ss.start(); ss.enable();
ss.enableAllSystems();      //YOU MUST DO THIS BEFORE USING THE SHOOTING SYSTEMS

ss.addDataLogger(new RPCLogger(rpcConn));

BallTracker bt = new BallTracker(STARTING_BALLS, collectionSwitch, hopperSwitch, upperRollersSwitch, ballQueueSwitch);
bt.start(); bt.enable();


MechTester tester = new MechTester(tertiary, dt, wedge, drawbridge, ss, "Mechanism Tester");

BetabotController bc = new BetabotController(tertiary, primary, secondary, ss, wedge, drawbridge, tester);

bt.addBallListener(bc);

RPCShootingController shootControl = new RPCShootingController(rpcConn, ss, 88);






addTeleopController(driveControl);
addTeleopController(bc);
addTeleopController(shootControl);
//        addTeleopController(encTest);
//        addTeleopController(rpcController);
//        addTeleopController(distTest);
//        addAutonomousController(balancer);
"""





