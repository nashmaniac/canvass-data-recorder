# Canvass Data Recorder

## Requirements
The following things should be installed in the laptop
* python3
* docker
## Installation
* Clone the repository
```
git clone https://github.com/nashmaniac/canvass-data-recorder.git
```
* Go into the project directory
* Intialize the virtual environment
```
python -m venv venv
```
* Activate the virtual environment
```
source venv/bin/activate
```
* Install the `requirements.txt`
```
pip install -r requirements.txt
```

At this point our application has all the dependencies that are needed to be in the machine.

## Running the application

* First run postgres on docker
```
docker compose up
```
* Run database migrations
```
python manage.py migrate
```
* Start Server in another terminal window
```
python manage.py runserver
```
* Start running the simulator in another terminal window
```
python recorder/scripts/simulator.py
```
This would populate the data in the database for 15 sensor. you can change the params in the file.


## Viewing the histogram
Histogram data are provided through an api here 

http://localhost:8000/recorder/api/v1/sensor-data/histogram?sensor=sensor-2&diff=10

Here `sensor` is the id of the sensor and `diff` is the interval on which the histogram is built. 


For seeing the histogram, I have written a jupyter notebook named `Graph.ipynb`

* Start jupyter notebook in another terminal
```
jupyter-notebook
```

* Open `Graph.ipynb`. You can change the sensor and interval using `sensor` and `diff` variable.