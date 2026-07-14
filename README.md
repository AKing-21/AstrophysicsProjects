# Astrophysics Research Portfolio

This repository contains computational astrophysics projects involving data analysis, simulations, and visualization of astronomical systems.

## Project 1: Exoplanet Transit Detection

**Goal:**  
Detect and analyze the transit signal of an exoplanet by measuring changes in a star's brightness as the planet passes in front of it.

**Target:**  
Kepler-10b

**Data Source:**  
NASA Kepler Space Telescope archive (accessed through the Lightkurve Python package)

**Methods:**
- Retrieved Kepler light curve data
- Normalized stellar brightness measurements
- Analyzed flux variations caused by planetary transits
- Visualized the resulting light curve

**Script:**  
`transit_search.py`

**Output:**  
A plot showing the decrease in stellar flux caused by Kepler-10b's transit.

---

## Project 2: Earth Orbit Simulation

**Goal:**  
Simulate Earth's orbit around the Sun using Newtonian gravitational physics and numerical integration.

**Methods:**
- Applied Newton's law of universal gravitation to calculate acceleration
- Updated velocity and position over time using numerical integration
- Simulated Earth's orbital motion around the Sun
- Created a real-time visualization of the orbit using Python and Matplotlib

**Physics Model:**
- Two-body gravitational system (Sun and Earth)
- Position and velocity updated using time-stepped calculations

**Script:**  
`earth_orbit.py`

**Output:**  
An animated visualization of Earth's orbit around the Sun with an orbital trail.