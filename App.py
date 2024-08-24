import subprocess
from MassSpringAnimation import MassSpring 

test = MassSpring.construct(1,2,3,4,5,0)
# Command to make the animation render
command = ["manim", "-p", "-ql", "MassSpringAnimation.py", "massSpring"]
# Run the commands in the terimal(git bash)
subprocess.run(command, shell=True)
