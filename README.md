# Django_webapp_iris_classification

## Creating a Webapp using Django with Python to perform classification on iris followers dataset.

### Steps
- Creating a virtual environment <br>
  `python -m venev iris_api`    <br> 
  `cd iris_api`                 <br>
  `.\iris_api\Scripts\activate` <br>
  <br>
  <br>

- ### Git Clone
  `git clone https://github.com/Gangadharbhuvan/Django_webapp_iris_classification.git`    <br> <br>

- ### Run
  Find path to manage.py file <br>
  `python manage.py runserver` <br> <br>
  



Go to Localhost 8000 port, and change to prediction page, Copy the path and use Postman for request using POST method and enter the values for 
- sepal_length  (values - min_value=4.3, max_value=7.9 )
- sepal_width   (values - min_value=2.0, max_value=4.4 )
- petal_length  (values - min_value=1.0, max_value=6.9 )
- petal_width   (values - min_value=0.1, max_value=2.5 )

<!--- 
### Home page
![Homepage](https://github.com/Gangadharbhuvan/Django_webapp_iris_classification/blob/main/iris_classification/templates/iris_app/images/homepage.png)


### Prediction page
![Predictionpage](https://github.com/Gangadharbhuvan/Django_webapp_iris_classification/blob/main/iris_classification/templates/iris_app/images/predictionpage.png)

---->
### Django REST Framework
![Django REST Framewrok](https://github.com/Gangadharbhuvan/Django_webapp_iris_classification/blob/main/iris_classification/templates/iris_app/images/django_rest_framework.png)

### Postman API results
![Postman api](https://github.com/Gangadharbhuvan/Django_webapp_iris_classification/blob/main/iris_classification/templates/iris_app/images/iris_api.png)
