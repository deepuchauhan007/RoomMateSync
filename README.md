# RoomMateSync

## Overview

RoomMateSync is a Python-based hostel roommate preference matching system.

The project helps students compare their daily habits and hostel preferences before sharing a room. It compares preferences such as sleep time, wake-up time, study time, noise, cleanliness, lighting, fan usage, odour sensitivity, and visitor preference.

The system calculates a compatibility score and identifies matching preferences, different preferences, and possible conflicts.

## Problem Statement

Students sharing a hostel room may have different daily routines and personal preferences. Differences in sleep schedules, study timings, noise levels, cleanliness, lighting, fan usage, and visitors can create difficulties between roommates.

RoomMateSync provides a simple preference-based system to compare student profiles and identify compatibility and potential conflicts before selecting roommates.

## Objectives

- Create and store student preference profiles.
- Compare two students based on their preferences.
- Calculate a compatibility score.
- Find the best available roommate match.
- Detect major preference conflicts.
- Generate a match report.
- Allow students to edit their existing profiles.
- Store profile data for future use.

## Features

- Student profile creation
- Student ID validation
- Duplicate Student ID detection
- Profile editing
- Roommate compatibility calculation
- Best roommate matching
- Conflict detection
- Match report generation
- JSON-based data storage
- Input validation
- Modular Python architecture

## Main Modules

### 1. Profile Management
Creates and edits student profiles containing hostel and daily routine preferences.

### 2. Compatibility Engine
Compares two student profiles and calculates their compatibility score.

### 3. Conflict Detector
Identifies differences in important roommate preferences.

### 4. Match Finder
Compares a student with other available profiles and finds the highest compatibility match.

### 5. Match Report
Displays a structured compatibility report between two students.

### 6. Storage
Stores and loads student profiles using a JSON file.

## Technologies Used

- Python
- JSON
- Visual Studio Code
- Git / GitHub

## Project Structure

RoomMateSync/

- main.py
- profile.py
- compatibility.py
- conflict_detector.py
- matcher.py
- report.py
- storage.py
- students.json
- README.md

## How to Run

1. Install Python on the system.
2. Open the RoomMateSync project folder in Visual Studio Code.
3. Open the terminal.
4. Run:

```bash
python main.py

5. Use the menu to create profiles, compare roommates, find matches, detect conflicts, generate reports, or edit profiles.


Compatibility Calculation

The system compares 9 preference fields:

Sleep time
Wake-up time
Study time
Noise
Cleanliness
Light
Fan
Odour sensitivity
Visitor preference

The compatibility score is calculated from the number of matching preferences.

Compatibility Score =
(Number of Matching Preferences / Total Preferences) × 100

Compatibility levels are:

80% or above: High
60% to below 80%: Moderate
Below 60%: Low
Data Storage

Student profiles are stored locally in:
students.json

The JSON file allows profile information to remain available even after the program is closed and restarted.


Testing

The following features have been tested:

Student profile creation
Duplicate Student ID validation
Invalid preference validation
Profile editing
Roommate comparison
Compatibility score calculation
Best match finding
Conflict detection
Match report generation
Data persistence after restarting the program


Future Enhancements

Weighted compatibility scoring
Graphical user interface
Login and authentication
Advanced roommate filtering
Export reports to PDF
Database-based storage
Web-based version

Author

Developed as a Python project for academic learning and application of Python programming concepts.