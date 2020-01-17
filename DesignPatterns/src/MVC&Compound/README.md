### Compound Pattern and Model View Controller
We can use Model View Controller pattern to explain the compound pattern.  
**Model** contains all the state, data and application logic needed to maintain the application.  
**View** is what's presented to the users and how users interact with the app.  
**Controller** updates the view when the model changes. 

**Model** uses **Observer** to keep the views and controllers updated on the latest state changes.   
**View** uses **Composite Pattern** to manage the windows, buttons and other components of the display.   
**Controller** implements **Strategy Pattern** with View. 

![alt text](http://mblogthumb2.phinf.naver.net/MjAxNzA2MjlfMTAy/MDAxNDk4NjkzNTM2NTg3.QXtjSuwzl1o61fJQlEWXx4NXdyc7_w-CW5ZRgYg8gt4g.6ggQLy3iuCirVKMTcPUBWHPo33NklBuldA5cjsuu5UYg.PNG.cestlavie_01/mvc3.png?type=w800 "MVC")
