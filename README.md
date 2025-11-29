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

## 📫 Let's Connect

<div align=\"center\">

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@asadullah-dal)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/aiphile17)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/aiphile)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/ai_phile)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@aiphile)
[![Portfolio](https://img.shields.io/badge/Portfolio-00C7B7?style=for-the-badge&logo=About.me&logoColor=white)](https://asadullah-dal17.github.io/asadullahdal.github.io)

### 💼 Freelance Platforms

[![Fiverr](https://img.shields.io/badge/Fiverr-1DBF73?style=for-the-badge&logo=fiverr&logoColor=white)](https://www.fiverr.com/asadullahdal482)
[![Kwork](https://img.shields.io/badge/Kwork-Freelance-black?style=for-the-badge&logo=kwork&logoColor=white)](https://kwork.com/user/asadullah92)

</div>

## 💬 Questions or Need Help?

If you have any questions or need help with the project, feel free to DM me on [Instagram](https://www.instagram.com/aiphile17)!

<a href="https://www.instagram.com/aiphile17">
    <img src="https://img.shields.io/badge/Instagram-purple?style=for-the-badge&logo=Instagram&logoColor=white" height=20  alt="Insta Badge"/>
  </a>
