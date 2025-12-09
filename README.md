## Waiting in Line in Virtual Reality Dataset (WAIT)

## Contents
[Description](#description)

[Contributors](#contributors)

[Overview of Dataset](#overview-of-dataset)

## Description
To fill. 

## Contributors
Elza Ibragimov, Natasha Kholgade Banerjee, Sean Banerjee, Ashutosh Shivakumar

[Terascale All-sensing Research Studio](https://tars-home.github.io)

## Overview of Dataset
The dataset is organized into the following folders:

| FolderName |	SubFolders |	DataType |	Contents |
| ------------- | ------------- | ------------- | ------------- |
| Cybersickness |	None |	CSV	| Participant responses to the standard Virtual Reality Sickness Questionnaire (VRSQ). Each participant is assigned a unique 5-character ID. |
| Demographics |	None |	CSV	| Participant demographics consisting of: age, ethnicity, race, self-identified gender, education level, whether they wear glasses, if the glasses are worn for reading, if they wear contacts, how frequently they play video games, what type of video games they play, how frequently they use VR, if they own a VR device, what type of VR devices they use, how frequently they use telehealth services, and what telehealth services they use. Each participant is assigned a unique 5-character ID. |
| FDS	| None |	CSV |	Participant responses to the standard Frustration Discomfort Scale (FDS). The CSV files are annotated as pre_ and post_ to indicate that they were administered prior to and after the immersion. Each participant is assigned a unique 5-character ID. |
| NASA_TLX |	None |	CSV	| Participant responses to the standard 21-tick NASA Task Load Index (TLX). Each participant is assigned a unique 5-character ID. |
| SUS	| None |	CSV	| Participant responses to the standard System Usability Scale (SUS). Each participant is assigned a unique 5-character ID. |
| TreatmentResponses |	None |	CSV	| Participant responses to each treatment, i.e., being notified about the reason for the wait (With_Notification) or not being notified about the reason (Without_Notification). Participant responses include their time estimate for the wait in minutes, their frustration level on a 5-point Likert scale (1 being lowest and 5 highest), and their likelihood to exit on a 5-point Likert scale. Each participant is assigned a unique 5-character ID.
| VRData	| Yes	| CSV	| Contains 36 subfolders that represents each participant. Each subfolder is named with the unique 5-character ID. Within each participant subfolder there are three additional subfolders named ParticipantID_NO_WAIT, ParticipantID_3_MINUTE_WAIT and ParticipantID_6_MINUTE_WAIT. Here Participant_ID is the unique 5-character ID and NO_WAIT, 3_MINUTE_WAIT and 6_MINUTE_WAIT are the wait conditions. Within the ParticipantID_NO_WAIT, ParticipantID_3_MINUTE_WAIT, and ParticipantID_6_MINUTE_WAIT subfolders are four CSV files for Eye Gaze (EyeGazeLog), Head Position and Orientation (HeadPosition), Left Hand (LeftHandLog), and Right Hand (RightHandLog). Thus, each participant has 12 CSV files. |

### Dataset Frame Rate Summary
The minimum (Min), maximum (Max), and average (Mean) frame rate for the head, eye gaze, right hand, and left hand for our dataset are provided below.  

| Treatment | Type of Data | Min | Max | Mean | SD |
| ----- | ----- | ----- | ----- | ----- | ----- |
| NO_WAIT |	Head | 67.54 | 73.87 | 71.11 | 0.96 |
| |	Eye Gaze | 66.32 | 73.14 | 70.59 | 1.2 |
| | Right Hand | 67.54 | 73.87 | 71.12 | 0.97 | 
| | Left Hand | 67.54 | 73.87 | 71.12 | 0.97 |
| 3_MINUTE_WAIT	| Head | 70.07 | 72.50 | 71.08 | 0.43
| | Eye Gaze | 68.96 | 71.37 | 70.56 | 0.62 | 
| | Right Hand | 70.06 | 72.50 | 71.10 | 0.43 | 
| |	Left Hand | 70.06 | 72.50 | 71.10 | 0.43 | 
| 6_MINUTE_WAIT	| Head | 70.07 | 72.50 | 71.08 | 0.43
| | Eye Gaze | 68.96 | 71.37 | 70.56 | 0.62 | 
| | Right Hand | 70.06 | 72.50 | 71.10 | 0.43 | 
| |	Left Hand | 70.06 | 72.50 | 71.10 | 0.43 | 
