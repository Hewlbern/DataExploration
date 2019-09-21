## Traffic Analysis and Exploration - and how to build a better coordination system.
- This repo is an analysis of traffic detection and data types including:
     - visualizations (dashboard, mapping, etc)
     - computer vision proof of concept
     - How deep learning can be used over the current coordination system "Masterlink".
- How adopting these technologies could create huge improvements in:
     - Congestion and safety.
     - Adoption of coordinated signalling in countries around the world simple.
- And a detailed explanation of the current system and it's obvious flaws.

## Background on the topic:
- Traffic signal optimization -> reducing time stopped at traffic signals. 
- SCATS is a traffic signal optimization system.
     - This is the major competitor with the best technology behind it (relatively new). https://www.rapidflowtech.com/surtrac . 
     - It is worth noting - SCATS is the market leader in signal optimization.
- In Australia, congestion cost has been estimated to be up to $37.3 billion by 2030.

## What's wrong with SCATS and it's detection? 

## Key Points	
1. What is wrong with SCATS volume (Past)
     - SCATS volume calculations
    - SCATS hierarchical accuracy - The end point being accuracy depends on faultless loop detector operation.
    - Research on loop detector failure - at least 20-30% are failed at any one time in US that understands the failures.
    - Authority Failure rates
    - Is failure rates the only data issue - No.
2.	How can computer vision, overcome, replace and correct what we know about ‘SCATS volume errors’? (Present)
    - More than one approach critical
    - Example of other ATC using computer vision and ML
3.	Where to next, what are the next steps? (Future)
    - Deep learning for coordination.


# What is wrong with scats volume, can it be machine learned ‘fixed’ or not?

### Loop detectors
- What is a loop detector?
    - https://www.youtube.com/watch?v=MQTHcKgDRto#t=5m28s
- A professional installation of loop detectors.
    - https://www.youtube.com/watch?v=OFpnJZ_jF68#t=2m05s


### Why has loop detection and SCATS not changed.
-  This is well covered here, Finance and Economics: http://kimoon.co.kr/gmi/reading/friedman-1966.pdf 
- Positive science and normative science – or better said, unbiased observations and unbiased observations made bias.
     - "The relevant question to ask about the "assumptions" of a theory is not whether they are descriptively "realistic," for they never are, but whether they are sufficiently good approximations for the purpose in hand. And this question can be answered only by seeing whether the theory works, which means whether it yields sufficiently accurate predictions."

### Failure Rates worldwide, and in Victoria, of loop detectors.

#### 1. Is there a World recognized body, who can authoritatively assert failure rates for loop detectors?
    - Yes. Federal Transportation Administrative, and more, 25 years ago wanted to improve loop detectors with 7 different "state of the art" technologies that were vastly superior. 25% at any one time in America were broken.
#### 2. What are other authorities failure rates and how does it compare to the USA at a estimate 25%? 
    - Yes it does compare. The best authorities are only able to isolate extremely obvious faults (one type).
    - The failure rate for loop detectors, if we isolated only 1 ‘data’ created as a result of loop detector failure (there are more than 1 type of failure to identify), is still ridiculously high. This is only for very obvious failures. 
    - Loop detector failure, measured by DS (degree of saturation) is only one fault type.
        - Chatter (excessive counting caused by e.g. bus or truck braking), Lane Discipline (car triggering 2 lane detectors) and more fault types combine to make reliance upon loop detectors, a bad idea in the 21st century (and really since the 1980's onwards).

## SCATS Traffic Measurements and Calculations
#### SCATS “volume calculations” are $VO, VK, DS.$
### Two basic forms of traffic data are sensed by the each of the detectors and sent by the local controller to the regional computer at the end of every cycle. This data takes the form of:
- The number of gaps (where nothing is detected) that occurred between the vehicles and the total non-occupancy (or space) time that occurred during the lane’s green time. Non-occupancy or space-time is the amount of time (in seconds) during a lane’s green time that the detector has no vehicles travelling over it.
- The phase time for the lane plus any remaining or unused phase time. Remaining or unused phase time can occur if a local controller decides to end a phase prematurely, due for example, to a lack of available vehicles which wish to pass through the green light. From this raw data three fundamental values that are needed by SCATS for each lane can be calculated. These values are:
1. Original Volume (VO).
2. Degree of Saturation (DS).
3. Reconstituted Volume (VK).



### Assumptions/dependencies: -
1.	‘Number of gaps’ is a ‘voltage drop’, assuming the current/loop detector is not broken, this ‘voltage drop’ itself additionally is premised on a vehicle size of 4.5 meters and is subject to being affected by speed calibration when setting up the ‘gain’ of the signal.
2.	‘ending a phase may be decided by a local controller’ based on…not detecting a vehicle (i.e. ‘a lack of available vehicles which wish to pass through’).
3.	All 3 ‘data’ calculations created by a Regional controller, (VO, DS, VK) manifest from a sourcing of loop detector information ‘passed from the local controller’.


## Research dissertation using actual SCATS data from Dublin which explored the internal SCATS algorithms and limitations.
- https://www.scss.tcd.ie/publications/tech-reports/reports.00/TCD-CS-2000-46.pdf
- One may interpret this dissertation effort as, ‘get the raw data out of SCATS and design an improved Algorithm to reduce traffic congestion and learn what’s going on’, another interpretation may be, ‘how badly is the SCATS algorithms performing against our own design, using the same data as SCATS actually uses’.

## Other Dependencies
1. SCATS relies on the faultless functioning of each lanes loop detector. 
     - Subsequent SCATS calculations and further assumptions which SCATS applies to the raw sourced information from the loop detector, including ‘smoothing and damping’ data the loop detector provides (sic), to compensate for ‘occasional significant fluctuation’, attributed to ‘various causes’.
#### 2. SCATS relies upon humans deciding for themseles if a detector is faulty or not. This ultimately relies on user knowledge to displace SCATS calculations and to ignore the faulty volume calculations based on SCATS's reliance on faultless loop detectors.
    - This issue interestingly not mentioned in SCATS's promotional materials or manuals or well anywhere lel. 



## Computer Vision

### It's super easy to do and cheaper than loop detectors and has more future functionality.

#### Truth must be established.
 - "To establish ground truth, in terms of “occupancy, volume, queue lengths and speed”, we need a “technology (that) has been refined to a point, that field evaluations are currently being made.”. 
     - A 25 year old quote a 1993 U.S. Department of Transportation, Federal Highway Administration training video, based on having conducted numerous surveys across numerous U.S. States showing that at any one point in time they had 25% detector failure. 

#### Examples of computer vision

1. BOX: LaTrobe Street, Melbourne, YOLO Tram Real time
    - https://www.youtube.com/watch?v=BNHJRRUKMa4#t=2m01s
2. MASK: Singapore
    - https://www.youtube.com/watch?v=UWtac4cFERM
3. Exception
    - https://www.youtube.com/watch?v=ATlcEDSPWXY&t=40s
4. Combined COCO RCNN
    - https://www.youtube.com/watch?v=OOT3UIXZztE&t=44s


- No simplistic listing of the free open sourced computer vision technologies is adequate to represent the list of International companies (Facebook, Google, Microsoft, Nvidia, Baidu, etc etc) who are in a race to ‘gain market share’ of their technology stacks to avoid losing relevance – by deliberately freely providing deep learning and convolutional neural network, frameworks and production pipelines.

    - Note, each is based on freely available open source code which any person, company can internally implement without, royalties, intellectual property payments or reliance on external vendors if they choose to pursue such an approach:-

### Is a one method approach for Computer Vision proposed, as the best solution?

- No, combining multiple technologies, with multiple failsafe is required. A audit trail with a person performing once a week randomised checking of video data quality is an additional failsafe.

## Deep Learning Coordination

### Current Coordination.

### Reinforcement Learning - See the DoTa openAI 1v1 match.
- more to come. Action - Value Optimization.

### Deep Reinforcement Learning
- Each intersection is an Agent that is optimized to decrease the congestion for the whole traffic network.
### Data requirements
- Detector loops are not capable of providing accurate traffic information for this system.
- Video based analysis will work instead.
     - Also vehicle to x may take its place, depends on time, can also use bluetooth or a variety of other detectors, but computer vision is the best option known now.

