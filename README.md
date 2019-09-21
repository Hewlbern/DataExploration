
## What's wrong with SCATS and it's detection? 
- This repo is an exploration of different traffic detection and data types, and includes visualizations (dashboard, mapping, etc), computer vision proof of concept to show how to improve the existing traffic detection used in widely industry, and an exploration of how deep learning can be used as a vast improvement over the current coordination system "Masterlink".
- This would create huge improvements in traffic conditions. Not only in congestion but also in safety.
- At the end of this readme is a list of the current competitors. There  is one competing system that has recently been built that is utilizing what is discussed in this repository. https://www.rapidflowtech.com/surtrac .

## Key Points	
1. What is wrong with SCATS volume, can it be machine learned ‘fixed’ or not? (Past)
     - SCATS volume calculations
    - SCATS hierarchical accuracy - The end point being accuracy depends on faultless loop detector operation.
    - Research on loop detector failure - at least 20-30% are failed at any one time in US that understands the failures.
    - DoT Failure rates
    - Is failure rates the only data issue - No.
2.	How can computer vision, overcome, replace and correct what we know about ‘SCATS volume errors’? (Present)
    - More than one approach critical
    - Example of other ATC using computer vision and ML
3.	Where to next, what are the next steps? (Future)
    - Deep learning for coordination.


# What is wrong with scats volume, can it be machine learned ‘fixed’ or not?

### To start with, what is a loop detector 
- What is a loop detector, what does a loop detector look like and can you build your own loop detector?
    - https://www.youtube.com/watch?v=MQTHcKgDRto#t=5m28s
- What does professional installation of loop detectors look like?
    - https://www.youtube.com/watch?v=OFpnJZ_jF68#t=2m05s


### Why has loop detection and SCATS not changed.
-  This is well covered here, Finance and Economics: http://kimoon.co.kr/gmi/reading/friedman-1966.pdf 
- Positive science and normative science – or better said, unbiased observations and unbiased observations made bias.
- The relevant question to ask about the "assumptions" of a theory is not whether they are descriptively "realistic," for they never are, but whether they are sufficiently good approximations for the purpose in hand. And this question can be answered only by seeing whether the theory works, which means whether it yields sufficiently accurate predictions.”

### Failure Rates worldwide, and in Victoria, of loop detectors.

#### 1. Is there a World recognized body, who can authoritatively assert failure rates for loop detectors?
    - Yes. Federal Transportation Administrative, and more, 25 years ago wanted to improve loop detectors with 7 different "state of the art" technologies that were vastly superior. 25% at any one time in America were broken. More information at end of notebook
    -Details in appendix.
#### 2. What are other authorities failure rates and how does it compare to the USA at a estimate 25%?
    - The authority checked developed and uses a excel tool to identify maintenance issues which are impacting on the operation of the traffic signal network. 
    - The failure rate for loop detectors, if we isolated only 1 ‘data’ created as a result of loop detector failure (there are more than 1 type of failure to identify). This is only for very obvious failures. 
    - Loop detector failure, measured by DS (degree of saturation) is not the only data issue created by reliance on loop detectors.
        - Chatter (excessive counting caused by e.g. bus or truck braking), Lane Discipline (car triggering 2 lane detectors) and other contributory variables combine to make reliance upon a broken system of loop detectors, unfeasible as the source of ground truth – as each of these emanate faulty data from failing loop detectors.

## SCATS Traffic Measurements and Calculations
#### SCATS “volume calculations” are $VO, VK, DS.$
### Two basic forms of traffic data are sensed by the each of the detectors and sent by the local controller to the regional computer at the end of every cycle. This data takes the form of:
- The number of gaps (where nothing is detected) that occurred between the vehicles and the total non-occupancy (or space) time that occurred during the lane’s green time. Non-occupancy or space-time is the amount of time (in seconds) during a lane’s green time that the detector has no vehicles travelling over it.
- The phase time for the lane plus any remaining or unused phase time. Remaining or unused phase time can occur if a local controller decides to end a phase prematurely, due for example, to a lack of available vehicles which wish to pass through the green light. From this raw data three fundamental values that are needed by SCATS for each lane can be calculated. These values are:
1. Original Volume (VO).
2. Degree of Saturation (DS).
3. Reconstituted Volume (VK).



### Assumptions/dependencies: -
1.	‘Number of gaps’ is a ‘voltage drop’ (remember video showing vehicle detection), assuming the current/loop detector is not broken, this ‘voltage drop’ itself additionally is premised on a vehicle size of 4.5 meters and is subject to being affected by speed calibration when setting up the ‘gain’ of the signal.
2.	‘ending a phase may be decided by a local controller’ based on…not detecting a vehicle (i.e. ‘a lack of available vehicles which wish to pass through’).
3.	All 3 ‘data’ calculations created by a Regional controller, (VO, DS, VK) manifest from a sourcing of loop detector information ‘passed from the local controller’.


## Research dissertation using actual SCATS data from Dublin which explored the internal SCATS algorithms and limitations.
- https://www.scss.tcd.ie/publications/tech-reports/reports.00/TCD-CS-2000-46.pdf
- One may interpret this dissertation effort as, ‘get the raw data out of SCATS and design an improved Algorithm to reduce traffic congestion and learn what’s going on’, another interpretation may be, ‘how badly is the SCATS algorithms performing against our own design, using the same data as SCATS actually uses’.

## Other Dependencies
1. SCATS is premised upon the faultless functioning of each lanes loop detector. This is magnified by subsequent SCATS ‘calculations’ and further assumptions which SCATS applies to the raw sourced information from the loop detector, including ‘smoothing and damping’ data the loop detector provides (sic), to compensate for ‘occasional significant fluctuation’, attributed to ‘various causes’.
#### 2. SCATS for “the first time being lets humans decide for themselves if a detector is faulty and to otherwise ignore the SCATS calculations and operations (paraphrased)”. This concession, ultimately relies on user knowledge to displace SCATS calculations and ignore the erroneous volume calculations based on SCATS utter dependency upon faultless operation of loop detectors.
    - Can we find this feature “(that) SCATS involves human user to decide for themselves if a detector is faulty and no longer detecting vehicles as they pass by.” and make necessary traffic management decisions, anywhere in the SCATS promotional materials available online today, alternatively will the ‘caveat emptor’ raised in the above dissertation be raised by the vendor?.
#### Interestingly, the official SCATS manual is less than helpful on targeting readers to potential issues of concern.



### Computer Vision

### It's super easy to do and cheaper than loop detectors and has more future functionality.

#### Ground Truth is key to establish.
 - "To establish ground truth, in terms of “occupancy, volume, queue lengths and speed”, we need a “technology (that) has been refined to a point, that field evaluations are currently being made.”. 
     - This is a 25 year old quote made in the above 1993 U.S. Department of Transportation, Federal Highway Administration training video, based on their having conducted numerous surveys across numerous U.S. States which had led to the assertion, that they collectively had a constant/at any point in time a 25% detector failure…causing “the large number of failures nationwide (having) created a deep concern within the traffic engineering community”.

    - Note, each is based on freely available open source code which any person, company can internally implement without, royalties, intellectual property payments or reliance on external vendors if they choose to pursue such an approach:-
1. BOX: LaTrobe Street, Melbourne, YOLO Tram Real time
    - https://www.youtube.com/watch?v=BNHJRRUKMa4#t=2m01s
2. MASK: Singapore
    - https://www.youtube.com/watch?v=UWtac4cFERM
3. Exception
    - https://www.youtube.com/watch?v=ATlcEDSPWXY&t=40s
4. Combined COCO RCNN
    - https://www.youtube.com/watch?v=OOT3UIXZztE&t=44s


- No simplistic listing of the free open sourced computer vision technologies is adequate to represent the list of International companies (Facebook, Google, Microsoft, Nvidia, Baidu, etc etc) who are in a race to ‘gain market share’ of their technology stacks to avoid losing relevance – by deliberately freely providing deep learning and convolutional neural network, frameworks and production pipelines.


### Is a one method approach for Computer Vision proposed, as the best solution?

- No, combining multiple technologies, with multiple failsafe is required. A audit trail with a person performing once a week randomised checking of video data quality is an additional failsafe.
