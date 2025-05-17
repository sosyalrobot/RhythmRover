# RhythmRover Dancing Robot

## Overview
RhythmRover is a dancing robot project that generates random dance moves in specific styles (hip-hop, salsa, robot) using a Python control script. It simulates motor controls for a robot with arms, legs, and head, suitable for hardware like Raspberry Pi or Arduino (with modifications). The project includes tempo-based dancing, combo moves, and music synchronization.

## Features
- Supports three dance styles: hip-hop, salsa, and robot.
- Random dance moves synchronized to a specified music tempo (BPM).
- Choreographed combo moves for specific styles.
- Detailed motor control with speed and angle simulation.
- Reset function to return motors to neutral position.
- Extensible for real hardware integration.

## Requirements
- Python 3.6+
- (Optional) Hardware-specific libraries (e.g., RPi.GPIO for Raspberry Pi)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sosyalrobot/RhythmRover.git
   cd RhythmRover
   ```
2. Run the script:
   ```bash
   python DancingRobot_RhythmRover.py
   ```

## Usage
- Run the script to execute a demo sequence including hip-hop dance, a salsa combo, and a robot-style dance synced to 128 BPM.
- Modify the `main()` function to customize dance styles, durations, or tempos.
- Use `random_dance(style, dance_duration, tempo)` for a single dance style.
- Use `combo_move(style, num_moves)` for a choreographed sequence.
- Use `sync_to_music(tempo, duration)` for tempo-based dancing.
- Replace the `RobotMotor` class with actual hardware control code for your robot.

## Code Structure
- `RobotMotor`: Simulates motor control with angle and speed tracking.
- `DanceMove`: Manages dance styles, random moves, combos, and tempo synchronization.
- Dance styles are defined with specific moves, durations, and speeds.

## Example
```python
robot = RobotMotor()
dance = DanceMove(robot)
dance.random_dance(style="hip_hop", dance_duration=20, tempo=110)  # 20-second hip-hop dance
dance.combo_move(style="robot", num_moves=5)  # 5-move robot combo
```

## Future Improvements
- Add real-time music analysis for dynamic tempo detection.
- Implement more dance styles (e.g., ballet, breakdance).
- Support for additional robot components (e.g., torso, hands).
- Integrate with actual motor hardware and sensors.

## License
MIT License
