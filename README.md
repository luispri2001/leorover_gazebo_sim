# Leo Sim Gazebo

Leo Rover simulation using Gazebo Garden with ROS 2 Humble, adapted for integration with [gps_ignition_simulation](https://github.com/luispri2001/gps_ignition_simulation.git).

![Screenshot of the simulation](screenshots/thumbnail.png)

## Description

This repository is a fork of the original project by [Dave-van-der-Meer](https://github.com/Dave-van-der-Meer/leorover_gazebo_sim_docker), which provides a simulation of the Leo Rover in Gazebo Garden with ROS 2 Humble. It has been refactored to better fit the needs of the [gps_ignition_simulation](https://github.com/luispri2001/gps_ignition_simulation.git) package, removing Docker dependency and improving compatibility.

## Installation

Clone this repository and navigate to its directory:

```shell-session
$ git clone https://github.com/luispri2001/leorover_gazebo_sim.git
$ cd leorover_gazebo_sim
```

Install the required dependencies and build the workspace:

```shell-session
$ rosdep install --from-paths src --ignore-src -r -y
$ colcon build --symlink-install
```

## Usage

To launch the Leo Rover simulation in Gazebo:

```shell-session
$ source install/setup.bash
$ ros2 launch leorover_gazebo_sim leo_gazebo.launch.py
```

## Roadmap

The goal of this project is to integrate the Leo Rover into a simulated (and simplified) navigation environment in Gazebo, working alongside the [gps_ignition_simulation](https://github.com/luispri2001/gps_ignition_simulation.git) package. It serves as a baseline for SLAM and navigation experiments in educational and research applications.

## License

MIT license.

## Project status

First adapted version is functional. Further tuning is required for navigation optimization. Suggestions and contributions are welcome!
