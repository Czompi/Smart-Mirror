# Smart-Mirror
Raspberry powered mirror which can display the news, weather, and time.


```bash
cd Smart-Mirror
```

## Automated install

### Get the repository
If you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed, clone the repository.

```bash
git clone git@github.com:Czompi/Smart-Mirror.git
```

**Alternatively, you can download a zip file containing the project (green button on the repository page)**

Navigate to the folder for the repository

### Setup project
```shell
chmod -x ./setup.sh
./setup.sh
```

### Start
#### Linux/macOS
```shell
chmod -x ./run.sh
./run.sh
```
#### Windows
```batch
run.bat
```

## Manual install

### Get the repository
If you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed, clone the repository.

```bash
git clone git@github.com:Czompi/Smart-Mirror.git
```

**Alternatively, you can download a zip file containing the project (green button on the repository page)**

Navigate to the folder for the repository

### Install your dependencies 
make sure you have [pip](https://pip.pypa.io/en/stable/installing/) installed before doing this

```bash
sudo pip install -r requirements.txt
```

```bash
sudo apt-get install python-imaging-tk
```

### Add your api token
Make sure vim is installed on your system: `sudo apt-get install vim`
Use `vim` to edit you file

```bash
vim smartmirror.py
```

replace `weather_api_token` with the token you got from openweathermap.org

## Running
To run the application run the following command in this folder

```bash
python smartmirror.py
```

## Demo and Build Instructions 
(click image for link to video)
[![Link to youtube how-to video](http://i.imgur.com/cMyaSHT.png)](https://youtu.be/fkVBAcvbrjU)
