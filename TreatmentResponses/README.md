# Treatment Responses

Our study consisted of three treatments: 
1.	No wait (NO_WAIT): The participant is spawned into the receptionist area and there is no one else in the line. The participant may approach the receptionist desk at any time to confirm their appointment.
2.  3-minute wait (3_MINUTE_WAIT): The participant is spawned into the receptionist area behind a waiting customer NPC. The interacting receptionist NPC informs the queue that there is a delay due to a computer problem. After 3-minutes the customer NPC leaves, after which, the participant can approach the receptionist desk to confirm their appointment.
3.  6-minute wait (6_MINUTE_WAIT): The participant is spawned into the receptionist area behind two waiting customer NPCs. The receptionist NPC informs the queue that there is a delay due to a computer problem. The first NPC leaves after 3-minutes and the second NPC after 6-minutes. After 6-minutes, the participant is free to approach the receptionist to confirm their appointment. 

All participants complete all three treatments, however, treatments are assigned in random order to each participant. 

| Dataset Column | Data | Response Value | 
| ------------- | ------------- | ------------- |
| 1 | Participant ID | Unique 5-character ID assigned to each participant. |
| 2 | Treatment1 | NO_WAIT, 3_MINUTE_WAIT or 6_MINUTE_WAIT to indicate which treatment the participant completed first. |
| 3 | Treatment1TimeEst | Decimal number indicating participant's estimate of wait. |
| 4 | Treatment1Frustration | 5-point Likert scale with 1 being lowest and 5 being highest for the frustration level after completing the treatment. |
| 5 | Treatment1ExitLikelihood | 5-point Likert scale: Very likely; Likely; Neutral; Unlikely; Very unlikely for the likelihood of exiting the simulation. |
| 6 | Treatment2 | NO_WAIT, 3_MINUTE_WAIT or 6_MINUTE_WAIT to indicate which treatment the participant completed second. |
| 7 | Treatment2TimeEst | Decimal number indicating participant's estimate of wait. |
| 8 | Treatment2Frustration | 5-point Likert scale with 1 being lowest and 5 being highest for the frustration level after completing the treatment. |
| 9 | Treatment2ExitLikelihood | 5-point Likert scale: Very likely; Likely; Neutral; Unlikely; Very unlikely for the likelihood of exiting the simulation. |
| 10 | Treatment3 | NO_WAIT, 3_MINUTE_WAIT or 6_MINUTE_WAIT to indicate which treatment the participant completed third. |
| 11 | Treatment3TimeEst | Decimal number indicating participant's estimate of wait. |
| 12 | Treatment3Frustration | 5-point Likert scale with 1 being lowest and 5 being highest for the frustration level after completing the treatment. |
| 13 | Treatment3ExitLikelihood | 5-point Likert scale: Very likely; Likely; Neutral; Unlikely; Very unlikely for the likelihood of exiting the simulation. |
