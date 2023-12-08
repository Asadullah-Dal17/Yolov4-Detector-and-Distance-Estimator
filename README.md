# Yolov4-Detector-and-Distance-Estimator

*Find the distance from the object to the camera using the YoloV4 object detector, here we will be using a single camera :camera:, detailed explanation of distance estimation is available in another repository* [**Face detection and Distance Estimation using single camera**](https://github.com/Asadullah-Dal17/Distance_measurement_using_single_camera)



https://user-images.githubusercontent.com/66181793/124917186-f5066b00-e00c-11eb-93cf-24d84e9c2e7a.mp4



 [**Video Tutorial Explains the concept and implementation** ](https://youtu.be/FcRCwTgYXJw) ![YouTube Video Views](https://img.shields.io/youtube/views/FcRCwTgYXJw?style=social)

- Here we are targeting the person and cell phone classes only, for demo purposes.

- you can follow all the steps mentioned in the video to create other objects as well. 

implementation detail available on [_**Darknet**_](https://github.com/pjreddie/darknet)


---

## TO DO

- [x] Finding the distance of multiple objects at the same time.

## Installation you need opencv-contrib-python

[opencv contrib](https://pypi.org/project/opencv-contrib-python/)

### **windows**

```pip
pip install opencv-contrib-python==4.5.3.56
```

### **Linux or Mac**

```pip
pip3 install opencv-contrib-python==4.5.3.56
```

then just clone this repository and you are good to go.

I have used tiny weights, check out more on darknet GitHub for more

---

## Add more Classes(Objects) for Distance Estimation

You will make changes on these particular lines [***DistanceEstimation.py***](https://github.com/Asadullah-Dal17/Yolov4-Detector-and-Distance-Estimator/blob/master/DistanceEstimation.py#L50-L56)
```python
if classid ==0: # person class id 
    data_list.append([class_names[classid[0]], box[2], (box[0], box[1]-2)])
elif classid ==67: # cell phone
    data_list.append([class_names[classid[0]], box[2], (box[0], box[1]-2)])
    
# Adding more classes for distance estimation 

elif classid ==2: # car
    data_list.append([class_names[classid[0]], box[2], (box[0], box[1]-2)])

elif classid ==15: # cat
    data_list.append([class_names[classid[0]], box[2], (box[0], box[1]-2)])
# In that way you can include as many classes as you want 

    # returning list containing the object data. 
return data_list

```

## Reading images and getting focal length

You have to make changes on these lines 📝 [***DistanceEstimation.py***](https://github.com/Asadullah-Dal17/Yolov4-Detector-and-Distance-Estimator/blob/master/DistanceEstimation.py#L69-L76)
there are two situations, if the object(classes) in the single image then, here you can see my reference image <img src='ReferenceImages/image4.png' width=200> 
it has to two object, *person* and *cell phone*
```python
# reading reference images 
ref_person = cv.imread('ReferenceImages/image14.png')
ref_mobile = cv.imread('ReferenceImages/image4.png')
# calling the object detector function to get the width or height of the object
# getting pixel width for person
person_data = object_detector(ref_person)
person_width_in_rf = person_data[0][1]

# Getting pixel width for cell phone
mobile_data = object_detector(ref_mobile)
mobile_width_in_rf = mobile_data[1][1]

# getting pixel width for cat
cat_data = object_detector(ref_person)
cat_width_in_rf = person_data[2][1]

# Getting pixel width for car
car_data = object_detector(ref_person)
car_width_in_rf = person_data[3][1]

```
if there is single class(object) in reference image then you approach it that way 👍
```python
# reading the reference image from dir 
ref_person = cv.imread('ReferenceImages/person_ref_img.png')
ref_car = cv.imread('ReferenceImages/car_ref_img.png.png')
ref_cat = cv.imread('ReferenceImages/cat_ref_img.png')
ref_mobile = cv.imread('ReferenceImages/ref_cell_phone.png')

# Checking object detection on the reference image 
# getting pixel width for person
person_data = object_detector(ref_person)
person_width_in_rf = person_data[0][1]

# Getting pixel width for cell phone
mobile_data = object_detector(ref_mobile)
mobile_width_in_rf = mobile_data[0][1]

# getting pixel width for cat
cat_data = object_detector(ref_cat)
cat_width_in_rf = person_data[0][1]

# Getting pixel width for car
car_data = object_detector(ref_car)
car_width_in_rf = person_data[0][1]
# Then you find the Focal length for each

```
If you have any doubt DM me on insta   <a href="https://www.instagram.com/aiphile17/"> <img alt="Instagram" src="https://user-images.githubusercontent.com/66181793/131223931-32d84c10-88b4-4cd6-8eb8-89f06c3b5b51.png"  width="20"> </a> </h4>

---
if You found this Helpful, please star :star: it.

You can Watch my Video Tutorial on Computer Vision Topics, just check out my YouTube Channel <a href="https://www.youtube.com/c/aiphile">  <img alt="AiPhile Youtube" src="https://user-images.githubusercontent.com/66181793/131223988-882d53a0-4882-468f-9bd7-46b46466baae.png"  width="20"> </a>


I am avalaible for paid work here <a href="https://www.fiverr.com/aiphile"> Fiverr <img alt="fiverr" src="https://user-images.githubusercontent.com/66181793/163767548-9a68e1c1-341a-4b07-9e35-042c35694c08.png"  width="15">  

## 💚🖤 Join me on Social Media 🖤💚 

 
   <div id="badges">

 <!-- Youtube Badge -->
  <a href="https://www.youtube.com/c/aiphile">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>

<!-- Instagram Badge  -->
  <a href="https://www.instagram.com/aiphile17">
    <img src="https://img.shields.io/badge/Instagram-purple?style=for-the-badge&logo=Instagram&logoColor=white" alt="Medium Badge"/>

<!-- Medium Badge  -->
  <a href="https://medium.com/@aiphile">
    <img src="https://img.shields.io/badge/Medium-black?style=for-the-badge&logo=Medium&logoColor=white" alt="Medium Badge"/>
  </a>

<!-- LinkedIn Badge -->
  <a href="https://www.linkedin.com/company/aiphile">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <!-- Face book badge  -->
<a href="https://asadullah.super.site">
    <img src="https://img.shields.io/badge/My%20Profile-black?style=for-the-badge&logo=Profile&logoColor=Green" alt="Facebook Badge"/>
  </a> 
  <!-- Twitter Badge  -->
  <a href="https://twitter.com/ai_phile">
    <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
  </a>
  
 
</div>
