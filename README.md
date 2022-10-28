
# Vallabhya: The Popularity Predictor 
> A Quantitative approach for prediction of YouTube Video’s Polpularity


## IDEA

- We all get recommendations from our friends, relatives, parents, teachers to watch dif-
ferent sort of good videos (as what they call it) on YouTube, Amazon Prime, NPTEL etc.
But what they mean by the term ‘good’? Is it content? Is it the video quality? Is it the
background music? Or maybe it is the combination of various factors depending upon the
demography of where the video is released? As a creative and curious group of people,
we explored the different dimensions of what makes a visual good and tried to predict
whether any given video is good or not. We have tried to quantify our whole analysis.

- The primary goal of the proposed research project is to analyse and evaluate the con-
tent of the visuals. We know that video is comprised of two parts - image and audio. To
initiate, we divided the problem into two major components - image analysis and audio
analysis. We explored variety of features in both of these and extracted those features from
each of these parts separately using different libraries like Librosa (for audio analysis) and
for the video part we used image processing taking out the frames from the videos and
process it using various libraries like OpenCV, beautifulsoup, youtubedl module etc. After
preprocessing the dataset to get the prediction of like or view counts applies various clas-
sification models like random forest classifier, XGBoost based on certain X parameters like
for the video part we have keypoints values, split in a video, blurness, brightness and sim-
ilarly for the audio part we have - chroma vector, spectral features, mel frequency capstral
coefficient. Finally implemented SHAP plot to get feature importance.

- As we know platforms like You Tube brings a new level of interaction and communica-
tion between users for creating & sharing content online. Now a day you tube is ranked as
2nd most popular website with hundreds of millions of users around the world. All users
have the opportunity to freely upload and share videos on you tube uploading them proper
categories: Entertainment, News polities, film, animation, Gaming, Education etc.

- Since the videos are from different genres may have a variety of different sets attributes
(that are mutually disjoints), deciding their popularity. To get a controllable domain, we
are restricting our model analysis to the Data Analytics videos available on YouTube(for
now; may increase the domain to learning platform videos).

- This study of both qualitative and quantitative aspect of video provides a starting point
to seek information about the video’s universality. Furthur research can be made to iden-
tify the popularity by using kind of sentiment analysis on the comments on videos, would
provide a more grip on the qualitative analysis.

## Tools

- Librosa
- Recursive Feature Elimination(RFE)
- Principal Component Analysis(PCA)
- XGBoost
- SHAP (SHapley Additive exPlanations)

## Contribute

Contributions are always welcome!
Please read the [contribution guidelines](contributing.md) first.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, <a href="mailto:devangu@iitk.ac.in">Devang Uniyal</a>, <a href="mailto:jithemji@iitk.ac.in">Jitesh Hemji</a>, <a href="mailto:veerby@iitk.ac.in">Veer Bhadra Yadav</a>, <a href="mailto:veerby@iitk.ac.in">Veer Bhadra Yadav</a>, <a href="mailto:fhamid@iitk.ac.in">Faiz Hamid</a>  has waived all copyright and related or neighboring rights to this work.
