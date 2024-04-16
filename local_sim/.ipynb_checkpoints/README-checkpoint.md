# Notes

path.py/obstacle.py
 - working, correctly avoids obstacles (circles)
 - model isn't ackermann yet

wheel_model.py
 - questionable model that approximates a wheel that you can turn and drive by accelerating
 - seems to work? but doesn't avoid obstacles correctly at all

bicycle_model.py
 - ackermann approximate kinematics 
 - same issue -- seems to work but definitely not avoiding obstacles correctly at all
 - inputs are velocity and steering angular velocity -- this is questionable (can basically jump to any velocity instantaneously)

bicycle_mode2.py
 - ackermann model kinematics with accelerations as inputs
 - doesn't work at all