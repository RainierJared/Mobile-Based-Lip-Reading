
# PWA-Based Mobile Lip Reading
This system is for my fourth-year class, Mobile Systems Development where I am assigned to develop and build one or more major features of the proposed project.


## Demo

![](MSDProject-Imgur-ezgif.com-optimize.gif)


## Installation and how to run

This project was built using Python v3.11.9

Install the dependencies via requirements.txt
```bash
pip3 install -r requirements.txt
```

To run the mobile application locally (localhost), run main.py via:
```bash
python3 main.py
```

To access it as a web application, open main.py and change the host parameter in line 5 of main.py to your IPv4 address.
```python
pwa.run(host='YOUR-IPv4-ADDRESS', port='8000', debug=True)
```
Afterwards, run main.py again via: `python3 main.py`, and go to the browser of a device that's connected to the same network as the webserver, and search for:
```bash
http://YOUR-IPv4-ADDRESS:8000
```

## Training a new classifier
If you would like to train the classifier with your face:

First, run the feature extraction script:
```bash
python3 .\Model\featureEx.py
```
The script captures 900 images and saves it to the `./Model/data` directory. While it's capturing the images, please move your lips to the shape of the word. 

(To change the amount of words that the model will be trained to interpret, first change the number of `words_recognised` in `featureEx.py` to the amount you choose, and update `labels_dict` variable in `model.py` to the amount you have increased).

Secondly, run the data gathering script:
```bash
python3 .\Model\dataGather.py
```
This script extracts the landmark coordinates from the images, and saves it to  `data.pickle` in binary.

Lastly, run the training script:
```bash
python3 .\Model\training.py
```
This script trains the Random Forest classifier, and saves the model to `model.p`

Afterwards, simply run `python3 main.py`

## License

[MIT](https://choosealicense.com/licenses/mit/)

