# AI-Based-Accident-Detection
Traditional traffic systems are designed only to monitor traffic but it
does not provide any solution to decrease the fatal accidental rate
which occur due to lack of medical aid in real time. Consider a
scenario where an accident occurred but no one was there to report
this accident, the victim is critical. We cannot root out accidents
totally but we can improve in providing post-crash care by detecting
the accident as quick as possible. There are lots of sensors available in
the market as well but that requires installation in vehicles. The
sensors will trigger the system that will alert nearby medical
assistance or an emergency contact number. But what if the accident
happened for a vehicle which is not equipped with such sensor-based
system. We need an advance Artificial intelligence-based surveillance
system which can detect occurrence of accident depending on
different accident-prone regions.

Section-1:

In this section, on the dataset which consists of various parameters
such as Accident Severity, Pothole Severity, Weather Conditions etc
predictive techniques are applied to Label the given area as High,
Medium and Low based on its Accident Severity.
Then, K-means Clustering is performed which clusters together the
areas with their respective accident-severity label (High, Medium or
Low).

Section-2:

Now, our proposed system will be integrated with various CCTV
cameras and frame rate will be configured according to the AccidentSeverity Label assigned to that region in section-1. So, if the area falls
under More High severity region, then the live video frames captured
will have shorter time duration between them. Moreover, after all
such configuration the system will be able to detect accident if any
occurs.

![image](https://user-images.githubusercontent.com/70505625/169817823-76c4be2e-47d0-48e2-9522-c1a66ce486ad.png)
![image](https://user-images.githubusercontent.com/70505625/169817999-df7cb563-6549-46bc-ba01-31c5d7d2303b.png)
![image](https://user-images.githubusercontent.com/70505625/169818173-8b86f0b2-fa75-45dd-8c09-194ae8224288.png)

Frame capturing speed based on accident prone region severity-
High Accident prone areas: More Quick Frame Capturing so on..
![image](https://user-images.githubusercontent.com/70505625/169818256-7207899c-a34d-47e1-8161-ef4642a791c4.png)


