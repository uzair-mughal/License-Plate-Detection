# License Plate Detection

YOLOv5 based License Plate Detection model that can be used to detect License Plate and make it blur. A useful tool for deploying and hiding License Plates of cars to keep privacy.

## Demo

<table>
  <tr>
    <td>Image</td>
     <td>Result</td>
  </tr>
  <tr>
    <td><img src="https://github.com/uzairmughal20/License-Plate-Detection/blob/master/test_images/Cars0.png" width="200" height="150"></td>
    <td><img src="https://github.com/uzairmughal20/License-Plate-Detection/blob/master/result_images/Cars0.png" width="200" height="150"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/uzairmughal20/License-Plate-Detection/blob/master/test_images/Cars14.png" width="200" height="150"></td>
    <td><img src="https://github.com/uzairmughal20/License-Plate-Detection/blob/master/result_images/Cars14.png" width="200" height="150"></td>
  </tr>
   <tr>
    <td><img src="https://github.com/uzairmughal20/License-Plate-Detection/blob/master/test_images/Cars38.png" width="200" height="150"></td>
    <td><img src="https://github.com/uzairmughal20/License-Plate-Detection/blob/master/result_images/Cars39.png" width="200" height="150"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/uzairmughal20/License-Plate-Detection/blob/master/test_images/Cars47.png" width="200" height="150"></td>
    <td><img src="https://github.com/uzairmughal20/License-Plate-Detection/blob/master/result_images/Cars47.png" width="200" height="150"></td>
  </tr>
 </table>
 
## Installation

```bash
    conda create --name lpd
    conda activate lpd
    git clone https://github.com/uzairmughal20/License-Plate-Detection.git
    pip install -r requirements.txt
```

## Running Tests

To run tests, run the following command

```bash
    python blur_license_plate.py "image_path"
    example: python blur_license_plate.py test_images/Cars47.png
```

## Training

#### In the train directory yout will find:

**_1-data_formatter.ipynb:_** Use this code to format the data according to YOLOv5.

**_2-:_** `git clone https://github.com/ultralytics/yolov5.git`
 
**_3-:_** `pip install -r yolov5/requirements.txt`

**_4-:_** `python ./yolov5/train.py --data ./data_yaml/LicensePlate.yaml  --batch-size 16  --epochs 100 --weights yolov5/yolov5s.pt`

## Dataset

[Car License Plate Detection](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection)


## License

[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

## References

- [YOLOv5](https://github.com/ultralytics/yolov5)
