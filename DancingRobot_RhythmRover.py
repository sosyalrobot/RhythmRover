import random
import time
import sys
import math

# Simulated robot motor control (replace with actual hardware library, e.g., RPi.GPIO)
class RobotMotor:
    def __init__(self):
        self.motors = {
            "left_arm": {"angle": 0, "speed": 0},
            "right_arm": {"angle": 0, "speed": 0},
            "left_leg": {"angle": 0, "speed": 0},
            "right_leg": {"angle": 0, "speed": 0},
            "head": {"angle": 0, "speed": 0}
        }
    
    def move(self, motor, direction, duration, speed=1.0):
        """Move a motor in a direction for a duration at a given speed."""
        if motor not in self.motors:
            print(f"Error: Invalid motor {motor}")
            return
        print(f"Moving {motor} {direction} at speed {speed:.2f} for {duration:.2f} seconds")
        self.motors[motor]["speed"] = speed
        # Simulate angle change based on direction
        angle_change = {"up": 30, "down": -30, "forward": 20, "back": -20, 
                       "tilt_left": -15, "tilt_right": 15, "spin": 45}
        self.motors[motor]["angle"] += angle_change.get(direction, 0) * speed
        self.motors[motor]["angle"] = max(-90, min(90, self.motors[motor]["angle"]))
        time.sleep(duration)
    
    def reset_position(self):
        """Reset all motors to neutral position."""
        for motor in self.motors:
            self.motors[motor]["angle"] = 0
            self.motors[motor]["speed"] = 0
        print("All motors reset to neutral position")

# Dance move library with styles
class DanceMove:
    def __init__(self, motor_controller):
        self.motor = motor_controller
        self.styles = {
            "hip_hop": [
                {"motor": "left_arm", "direction": "up", "duration": 0.4, "speed": 1.2},
                {"motor": "right_arm", "direction": "down", "duration": 0.4, "speed": 1.2},
                {"motor": "left_leg", "direction": "forward", "duration": 0.6, "speed": 1.0},
                {"motor": "head", "direction": "tilt_right", "duration": 0.3, "speed": 0.8}
            ],
            "salsa": [
                {"motor": "left_leg", "direction": "forward", "duration": 0.5, "speed": 0.9},
                {"motor": "right_leg", "direction": "back", "duration": 0.5, "speed": 0.9},
                {"motor": "left_arm", "direction": "up", "duration": 0.3, "speed": 1.0},
                {"motor": "head", "direction": "tilt_left", "duration": 0.2, "speed": 0.7}
            ],
            "robot": [
                {"motor": "left_arm", "direction": "up", "duration": 0.8, "speed": 0.5},
                {"motor": "right_arm", "direction": "up", "duration": 0.8, "speed": 0.5},
                {"motor": "head", "direction": "tilt_left", "duration": 0.4, "speed": 0.6},
                {"motor": "head", "direction": "tilt_right", "duration": 0.4, "speed": 0.6}
            ]
        }
    
    def random_dance(self, style=None, dance_duration=30, tempo=120):
        """Perform a random dance in a given style with tempo-based timing."""
        print(f"Starting RhythmRover {style or 'freestyle'} dance for {dance_duration} seconds!")
        start_time = time.time()
        beat_interval = 60.0 / tempo  # Time per beat in seconds
        
        while (time.time() - start_time) < dance_duration:
            if style and style in self.styles:
                move = random.choice(self.styles[style])
            else:
                # Freestyle: pick from all moves
                all_moves = [m for moves in self.styles.values() for m in moves]
                move = random.choice(all_moves)
            
            # Scale duration with tempo
            adjusted_duration = move["duration"] * (120 / tempo)
            self.motor.move(
                motor=move["motor"],
                direction=move["direction"],
                duration=adjusted_duration,
                speed=move["speed"]
            )
            time.sleep(random.uniform(0.1, beat_interval / 2))
        
        self.motor.reset_position()
        print("Dance sequence complete!")
    
    def combo_move(self, style, num_moves=3):
        """Execute a choreographed combo of moves in a specific style."""
        if style not in self.styles:
            print(f"Error: Style {style} not available")
            return
        print(f"Performing {style} combo move!")
        for _ in range(num_moves):
            move = random.choice(self.styles[style])
            self.motor.move(
                motor=move["motor"],
                direction=move["direction"],
                duration=move["duration"],
                speed=move["speed"] * 1.1  # Slightly faster for combos
            )
            time.sleep(0.2)
    
    def sync_to_music(self, tempo=120, duration=30):
        """Dance synchronized to a given music tempo."""
        print(f"Dancing to music with tempo {tempo} BPM for {duration} seconds")
        self.random_dance(style=random.choice(list(self.styles.keys())), 
                        dance_duration=duration, tempo=tempo)

def main():
    try:
        robot = RobotMotor()
        dance = DanceMove(robot)
        
        # Demo: Perform a sequence of dances
        print("=== RhythmRover Dance Demo ===")
        
        # Hip-hop dance
        dance.random_dance(style="hip_hop", dance_duration=15, tempo=100)
        time.sleep(1)
        
        # Salsa combo move
        dance.combo_move(style="salsa", num_moves=4)
        time.sleep(1)
        
        # Robot style with music sync
        dance.sync_to_music(tempo=128, duration=20)
        
    except KeyboardInterrupt:
        print("\nDance stopped by user")
        robot.reset_position()
        sys.exit(0)

if __name__ == "__main__":
    main()