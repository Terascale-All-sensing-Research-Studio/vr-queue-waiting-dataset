## Waiting in Line in Virtual Reality Dataset (WAIT)

## Contents
[Description](#description)

[Contributors](#contributors)

[Overview of Dataset](#overview-of-dataset)

[Data Dictionary](#data-dictionary)

## Description
The WAIT dataset consists of 36 human participants waiting in line at a virtual doctor's office receptionist area, designed using a Unity 2022.3.9 f1, to check in for an appointment. Each participant is randomly assigned to 3 treatment: no (NO_WAIT), 3-minute (3_MINUTE_WAIT), and 6-minute (6_MINUTE_WAIT) waits, after which they confirm their appointment with a virtual receptionist. Each participant completed all 3 treatments using a Meta Quest Pro headset. For each participant, we collect demographic data and frustration intolerance using the Frustration Discomfort Scale (FDS) prior to immersion. After each treatment, participants provided their perceived frustration and likelihood to exit using a 5-point Likert scale, and their perception of time elapsed. After all treatments, participants retook the FDS and completed the NASA Task Load Index, System Usability Scale, and Cybersickness in VR Questionnaire. Our dataset also consists of head, left hand, and right hand position and orientation data as well as object names and hit positions of all objects the participant visually engaged with. 

## Contributors
Elza Ibragimov, Ava Megyeri, Natasha Kholgade Banerjee, Sean Banerjee, Ashutosh Shivakumar

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

## Data Dictionary
The file [dictionary.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-dataset/blob/main/dictionary.csv) provides a summary of the data found in the following CSV files in our dataset: 
* [Cybersickess/cybersickness.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-dataset/blob/main/Cybersickness/cybersickness.csv)
* [Demographics/demographics.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-dataset/blob/main/Demographics/demographics.csv)
* [FDS/pre_fds.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-dataset/blob/main/FDS/pre_fds.csv)
* [FDS/post_fds.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-dataset/blob/main/FDS/post_fds.csv)
* [NASA_TLX/nasatlx.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-dataset/blob/main/NASA_TLX/nasatlx.csv)
* [SUS/sus.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-dataset/blob/main/SUS/sus.csv)
* [TreatmentResponses/TreatmentResponses.csv](https://github.com/Terascale-All-sensing-Research-Studio/vr-queue-waiting-dataset/blob/main/TreatmentResponses/TreatmentResponses.csv)

The file contains the following information:

| Column | Description |
| ------ | ----------- |
| Directory/FileName | Provides the directory and filename, e.g., Demographics/demographics.csv |
| ColumnName | Provides the column name in the file being referenced in Directory/FileName, e.g., Participant ID |
| Value | Provides detailed information of the value stored in ColumnName, e.g., Unique 5-character ID assigned to each participant |

### Dataset Frame Rate Summary
The minimum (Min), maximum (Max), and average (Mean) frame rate for the head, eye gaze, right hand, and left hand for our dataset are provided below.  

| Treatment | Type of Data | Min | Max | Mean | SD |
| ----- | ----- | ----- | ----- | ----- | ----- |
| NO_WAIT | Head | 49.52 | 71.55 | 67.81 | 3.42 |
| | Eye gaze | 49.36 | 70.83 | 67.65 | 3.46 |
| | Right hand | 49.52 | 71.55 | 67.81 | 3.42 |
| | Left hand | 49.52 | 71.55 | 67.81 | 3.42 |
| 3_MINUTE_WAIT | Head | 55.42 | 103.84 | 65.11 | 7.23 |
| | Eye gaze | 54.09 | 103.84 | 64.85 | 7.20 |
| | Right hand | 55.42 | 103.84 | 65.11 | 7.23 |
| | Left hand | 55.42 | 103.84 | 65.11 | 7.23 |
| 6_MINUTE_WAIT | Head | 55.18 | 71.69 | 60.91 | 3.32 |
| | Eye gaze | 55.18 | 71.67 | 60.70 | 3.94 |
| | Right hand | 55.18 | 71.69 | 60.92 | 3.32 |
| | Left hand | 55.18 | 71.69 | 60.92 | 3.32 |
