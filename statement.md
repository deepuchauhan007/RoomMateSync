# RoomMateSync - Project Statement

## Problem Statement

Students living in hostels may have different daily routines and personal preferences. Differences in sleep schedules, study timings, noise levels, cleanliness, lighting, fan usage, odour sensitivity, and visitor preferences can create difficulties between roommates.

RoomMateSync is designed to provide a simple preference-based system that allows students to compare their profiles, calculate compatibility, identify possible conflicts, and find a suitable roommate match.

## Scope

The project focuses on comparing student-entered hostel and daily routine preferences.

The system can:

- Create student profiles
- Store student preferences
- Edit existing profiles
- Compare two students
- Calculate compatibility scores
- Find the best available match
- Detect preference conflicts
- Generate match reports
- Store data using a JSON file

The project does not make psychological, medical, or personality assessments. The matching result is based only on the preferences entered by the users.

## Target Users

The primary target users are:

- Hostel students
- College students looking for compatible roommates
- Students comparing their daily routines before sharing a room

## High-Level Features

### Student Profile Management

Students can create and edit their profiles using a Student ID and their hostel-related preferences.

### Compatibility Comparison

The system compares two student profiles and calculates a compatibility score based on matching preferences.

### Best Match Finder

The system compares one student's profile with other available profiles and identifies the profile with the highest compatibility score.

### Conflict Detection

The system identifies differences in important preferences such as sleep time, study time, noise, cleanliness, lighting, and fan usage.

### Match Report

The system generates a report containing the students' names, matching preferences, different preferences, compatibility score, and compatibility level.

### Data Storage

Student profile information is stored in a JSON file so that the data remains available after the program is restarted.