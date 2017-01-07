Realtime FMRI Design Document
=============================

  ------------------------------------------------------------------------------------------------------------------------------------------
  **Target release**    2017-04-05
  --------------------- --------------------------------------------------------------------------------------------------------------------
  **Epic**              1.  As a user, I can monitor data quality in real time to keep participants from having to return for repeat scans
                        
                        2.  As a user, I can get all my realtime data streams in one easy to visualize place to help with decision making
                        
                        3.  As a user, I want to give my participant biofeedback to improve task performance
                        
                        

  **Document status**   DRAFT

  **Document owner**    [Lynne Williams](file://localhost/display/~lwilliams)

  **Designer**          [Lynne Williams](file://localhost/display/~lwilliams)

  **Developers**        [Lynne Williams](file://localhost/display/~lwilliams)

  **QA**                [Danny Kim](file://localhost/display/~dkim)
  ------------------------------------------------------------------------------------------------------------------------------------------

 

Goals
-----

For scientists and clinicians who need to ensure high data quality, the
realtime fMRI system is a data quality management tool that will provide
a single point of access to monitoring structural, functional, and
physiological data streams from the GE Discovery 750 MR scanner and
peripheral equipment at the BC Children's Core 3T MRI Research Facility
and the Brain Mapping and Neurotechnology Laboratory. The system will
present data streaming in near-realtime, flag scans with high levels of
motion, and provide 'quick and dirty' analyses of functional data. This
system will reduce motion in the final fMRI scans by 10% over the first
year by allowing scientists to visualize motion and physiological
signals during scanning. Unlike the current workflow, the realtime data
monitoring system will assess known potential data quality issues and
automatically generate reports in compliance with UBC Ethics and patient
confidentiality requirements.

-   Develop an extensible platform for a family of related products

-   Build comprehensive GUI interface

-   Improve functional data quality by 10% over the first year

Background and strategic fit
----------------------------

Assumptions
-----------

-   User will primarily access the data collection/streaming software
    from a laptop computer

-   Computer will run Linux or Mac OS

-   Software needs to be portable across OS

-   Visualization tool will require a tablet version and network
    streaming

-   Backend needs to be open-source

-   Software needs to be able to make Matlab calls to another machine

Iteration & Release Plan
------------------------

  **Target Iteration Length**   2 weeks
  ----------------------------- ---------
  **Iterations per Release**    8-12

Requirements
------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **\#**   **Title**                       **User Story**                                                                                                                                                                                     **Importance**   **Release.Iteration**   **Constraints**                                                                                **Notes**
  -------- ------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------- ----------------------- ---------------------------------------------------------------------------------------------- --------------------------------------------------------------
  1                                        As a neuroimager, I want to be able to collect physiological information about my participant to help in data analysis                                                                             *Must have*                              -   Make sure it works with all physiological data channels streaming off of the MRI scanner    
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                      

  2                                        As a neuroimager, I want to be able to visualize physiological data from the MR scanner in real time                                                                                               *Must have*                              -   Make sure that data plotting tools do not interfere with accurate data collection           
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                       -   Make the display simple to read                                                            
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                      

  3                                        As a neuroimager, I want my physiological data to be synchronized to the MR scanner                                                                                                                *Must have*                              -   Make sure that the MR scanner is used as the master clock                                   
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                       -   Make sure that the timing of the signals is aligned                                        
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                      

  4        Detect head motion              As a neuroimager, I want to be able to detect participant head motion in the MRI scanner to eliminate as many bad scans as possible                                                                *Must have*      1.1                                                                                                                    -   Bob D's code doesn't run anymore. Backend is deprecated.
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                      

  5        Online data analysis            As a neuroimager, I want to be able to visualize fMRI functional activity in near real time to make sure that the participant is on task                                                                                                    -   Make sure that results compare favourably to offline results                                
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                       -   Preliminary results should be available during or immediately following the scan           
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                      

  6                                        As a neuroimager, I want to get online tractography results to be able to determine DTI scan quality                                                                                                                                                                                                                                        

  7        Flag atypical/outlier scans     As the director of brain mapping, I want questionable data to be flagged as being an outlier to help me determine if it is bad data or a veritable outlier                                                                                                                                                                                  

  8        Seamless data transfer          As a user, I want data transfer to be seamless to keep data viewing in real time                                                                                                                                                                                                                                                            

  9        Data visualization              As a user, I would like channels for all the data types that I use to give me all of my information in one spot                                                                                                                                                                                                                             

  10                                       As a neuroimager, I would like to simultaneously view my EEG, NIRS, physiological and MR data in one place                                                                                                                                  -   Make sure that peripheral equipment is 'plug-and-play' &gt; no additional setup required    
                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                      

  11       Feedback re: head motion        As an MRI Patient/Participant I want feedback when I am moving too much to get a good picture                                                                                                                                                                                                                                               

  12       Feedback re: task performance   As an MRI Patient/Participant I want feedback when I am off task                                                                                                                                                                                                                                                                            

  13       Integrate with MATATABI         As director of Brain Mapping, I want the realtime software to integrate with MATATABI                                                                                                                                                                                                                                                       

  14                                       As a brain mapping team member, I want the motion detection software to show the same features in the simulator as in the scanner to make sure that the child is fully prepared for MRI scanning                                                                                                                                            

  15                                       As a MRI user, I want a simulation of what motion looks like to train students/RA in quality control monitoring                                                                                                                                                                                                                             
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

### Use Case 1

  ------
    --
    --

  ------
  ------

### Use Case 2: Release 1 Development

  ------
    --
    --

  ------
  ------

User interaction and design
---------------------------

### Motion Detection Window

  ------
    --
    --

  ------
  ------

Questions
---------

Below is a list of questions to be addressed as a result of this
requirements document:

  **Question**   **Outcome**
  -------------- -------------
                 

Not Doing
---------

-   Not doing biofeedback for initial release (may be considered for a
    later release)

Revision History
----------------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Version**                                                                                    **Date**                  **Comment**
  ---------------------------------------------------------------------------------------------- ------------------------- ------------------------------------------------------------------------------------------------------
  **[Current Version](file://localhost/display/BL/viewpage.action%3fpageId=7018482) (v. 36) **   **Dec 16, 2016 13:51 **   [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a):\
                                                                                                                           updated iteration field

  [v. 35](file://localhost/display/BL/viewpage.action%3fpageId=7019084)                          Dec 16, 2016 13:31        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a):\
                                                                                                                           Updated use case; Created use case for Release 1.0

  [v. 34](file://localhost/display/BL/viewpage.action%3fpageId=7019082)                          Dec 16, 2016 13:21        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 33](file://localhost/display/BL/viewpage.action%3fpageId=7019059)                          Dec 16, 2016 11:33        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 32](file://localhost/display/BL/viewpage.action%3fpageId=7019034)                          Dec 15, 2016 16:23        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a):\
                                                                                                                           added some assumptions

  [v. 31](file://localhost/display/BL/viewpage.action%3fpageId=7018980)                          Dec 15, 2016 12:46        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a):\
                                                                                                                           updated motion detection window wireframe to include thresholds and different types of motion graphs

  [v. 30](file://localhost/display/BL/viewpage.action%3fpageId=7018868)                          Dec 15, 2016 10:54        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a):\
                                                                                                                           Add more titles to requirements

  [v. 29](file://localhost/display/BL/viewpage.action%3fpageId=7018777)                          Dec 15, 2016 10:53        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a):\
                                                                                                                           Add titles to requirements

  [v. 28](file://localhost/display/BL/viewpage.action%3fpageId=7018775)                          Dec 15, 2016 10:19        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 27](file://localhost/display/BL/viewpage.action%3fpageId=7018760)                          Dec 15, 2016 10:17        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 26](file://localhost/display/BL/viewpage.action%3fpageId=7018758)                          Dec 15, 2016 10:15        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 25](file://localhost/display/BL/viewpage.action%3fpageId=7018756)                          Dec 15, 2016 10:10        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 24](file://localhost/display/BL/viewpage.action%3fpageId=7018754)                          Dec 14, 2016 17:25        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 23](file://localhost/display/BL/viewpage.action%3fpageId=7018736)                          Dec 14, 2016 11:51        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 22](file://localhost/display/BL/viewpage.action%3fpageId=7018670)                          Dec 14, 2016 11:46        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 21](file://localhost/display/BL/viewpage.action%3fpageId=7018665)                          Dec 14, 2016 11:41        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a):\
                                                                                                                           added another user story

  [v. 20](file://localhost/display/BL/viewpage.action%3fpageId=7018660)                          Dec 14, 2016 11:37        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 19](file://localhost/display/BL/viewpage.action%3fpageId=7018658)                          Dec 14, 2016 11:36        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 18](file://localhost/display/BL/viewpage.action%3fpageId=7018657)                          Dec 14, 2016 10:11        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 17](file://localhost/display/BL/viewpage.action%3fpageId=7018638)                          Dec 14, 2016 10:10        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 16](file://localhost/display/BL/viewpage.action%3fpageId=7018637)                          Dec 14, 2016 10:07        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 15](file://localhost/display/BL/viewpage.action%3fpageId=7018636)                          Dec 14, 2016 10:01        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 14](file://localhost/display/BL/viewpage.action%3fpageId=7018634)                          Dec 14, 2016 09:58        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 13](file://localhost/display/BL/viewpage.action%3fpageId=7018633)                          Dec 14, 2016 09:57        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 12](file://localhost/display/BL/viewpage.action%3fpageId=7018631)                          Dec 14, 2016 09:57        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 11](file://localhost/display/BL/viewpage.action%3fpageId=7018630)                          Dec 14, 2016 09:53        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 10](file://localhost/display/BL/viewpage.action%3fpageId=7018626)                          Dec 13, 2016 11:29        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 9](file://localhost/display/BL/viewpage.action%3fpageId=7018595)                           Dec 13, 2016 09:55        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 8](file://localhost/display/BL/viewpage.action%3fpageId=7018565)                           Dec 13, 2016 09:47        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 7](file://localhost/display/BL/viewpage.action%3fpageId=7018559)                           Dec 13, 2016 09:46        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 6](file://localhost/display/BL/viewpage.action%3fpageId=7018558)                           Dec 12, 2016 11:44        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 5](file://localhost/display/BL/viewpage.action%3fpageId=7018500)                           Dec 12, 2016 11:43        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 4](file://localhost/display/BL/viewpage.action%3fpageId=7018498)                           Dec 12, 2016 11:25        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 3](file://localhost/display/BL/viewpage.action%3fpageId=7018486)                           Dec 12, 2016 11:24        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 2](file://localhost/display/BL/viewpage.action%3fpageId=7018485)                           Dec 12, 2016 11:24        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)

  [v. 1](file://localhost/display/BL/viewpage.action%3fpageId=7018483)                           Dec 12, 2016 11:24        [**Lynne Williams**](%20%20%20%20/display/~lwilliams%0d%0a)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


