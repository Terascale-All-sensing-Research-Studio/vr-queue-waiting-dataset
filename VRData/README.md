# VR Data

Our study consisted of three treatments: 
1. No wait: When the participant is teleported into the receptionist area, they are presented with an empty queue and can approach the receptionist NPC when they wish. 
2. 3-minute wait: The participant is teleported into the scene and stands behind a single NPC. The receptionist indicates that there is an issue with their computer to the NPC in the queue. After 3 minutes, the queue NPC walks away to indicate that are tired of waiting leaving the participant as the only person in the queue. 
3. 6-minute wait: The participant is placed in a queue behind two NPCs. Similar to the 3-minute wait, the receptionist NPC indicates there is an issue. The first NPC leaves after the 3-minute mark. The second NPC leaves after the 6-minute mark. The participant is the only person in the queue after 6 minutes.

Each of the 36 folders here represents a single participant. The folder is named with a unique 5-character ID assigned to each participant. Within each of these 36 folders there are three subfolders named ParticipantID_NO_WAIT, ParticipantID_3_MINUTE_WAIT, and ParticipantID_6_MINUTE_WAIT. Here, ParticipantID is the 5-character ID assigned to each participant and NO_WAIT, 3_MINUTE_WAIT, and 6_MINUTE_WAIT indicates whether the participant was in an empty queue, waiting for 3-minutes behind a single NPC, or waiting 6-minutes behind two NPCs. Within the NO_WAIT, 3_MINUTE_WAIT, and 6_MINUTE_WAIT sub-subfolders are 4 raw CSV files, for a total of 12 raw CSV files per participant. The names and locations of each of these 12 CSV files are as follows:

| Filename |	Location |
| -------- | -------- |
| EyeGazeLog_NO_WAIT.csv	| ParticipantID/ParticipantID_NO_WAIT |
| HeadPositionLog_NO_WAIT.csv	| ParticipantID/ParticipantID_NO_WAIT |
| LeftHandLog_NO_WAIT.csv	| ParticipantID/ParticipantID_NO_WAIT | 
| RightHandLog_NO_WAIT.csv	| ParticipantID/ParticipantID_NO_WAIT |
| EyeGazeLog_3_MINUTE_WAIT.csv	| ParticipantID/ParticipantID_3_MINUTE_WAIT |
| HeadPositionLog_3_MINUTE_WAIT.csv	| ParticipantID/ParticipantID_3_MINUTE_WAIT |
| LeftHandLog_3_MINUTE_WAIT.csv	| ParticipantID/ParticipantID_3_MINUTE_WAIT | 
| RightHandLog_3_MINUTE_WAIT.csv	| ParticipantID/ParticipantID_3_MINUTE_WAIT |
| EyeGazeLog_6_MINUTE_WAIT.csv	| ParticipantID/ParticipantID_6_MINUTE_WAIT |
| HeadPositionLog_6_MINUTE_WAIT.csv	| ParticipantID/ParticipantID_6_MINUTE_WAIT |
| LeftHandLog_6_MINUTE_WAIT.csv	| ParticipantID/ParticipantID_6_MINUTE_WAIT | 
| RightHandLog_6_MINUTE_WAIT.csv	| ParticipantID/ParticipantID_6_MINUTE_WAIT |

The content stored in each of these 12 CSV files per participant are as follows:

| Filename |	Content |
| -------- | -------- |
| EyeGazeLog_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the eye gaze event was recorded.<br> **GameTime:** Game time stamp for when the eye gaze event was recorded.<br>**ObjectName:** Human readable name for the scene object for the eye gaze.<br> **HitPosition:** x, y, and z location of the eye gaze hit location. |
| HeadPositionLog_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the head movement was recorded.<br> **GameTime:** Game time stamp for when the head movement was recorded.<br> **HeadPosition:** x, y, z position of the head.<br> **HeadRotation:** X, Y, and Z rotation of the head.|
| LeftHandLog_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the left hand movement was recorded.<br> **GameTime:** Game time stamp for when the left hand movement was recorded.<br> **LeftHandPosition:** x, y, z position of the left hand.<br> **LeftHandRotation:** X, Y, and Z rotation of the left hand.
| RightHandLog_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the right hand movement was recorded.<br> **GameTime:** Game time stamp for when the right hand movement was recorded.<br> **RightHandPosition:** x, y, z position of the right hand.<br> **RightHandRotation:** X, Y, and Z rotation of the right hand.
| EyeGazeLog_WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the eye gaze event was recorded.<br> **GameTime:** Game time stamp for when the eye gaze event was recorded.<br> **ObjectName:** Human readable name for the scene object for the eye gaze.<br> **HitPosition:** x, y, and z location of the eye gaze hit location.
| HeadPositionLog_ WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the head movement was recorded.<br> **GameTime:** Game time stamp for when the head movement was recorded.<br> **HeadPosition:** x, y, z position of the head.<br> **HeadRotation:** X, Y, and Z rotation of the head. |
| LeftHandLog_ WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the left hand movement was recorded.<br> **GameTime:** Game time stamp for when the left hand movement was recorded.<br> **LeftHandPosition:** x, y, z position of the left hand.<br> **LeftHandRotation:** X, Y, and Z rotation of the left hand. |
| RightHandLog_ WITHOUT_NOTIFICATION.csv	| **Timestamp(ns):** Epoch time stamp for when the right hand movement was recorded.<br> **GameTime:** Game time stamp for when the right hand movement was recorded.<br> **RightHandPosition:** x, y, z position of the right hand.<br> **RightHandRotation:** X, Y, and Z rotation of the right hand. |

