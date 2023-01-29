This proyect contains the neccessay code to install and deploy a YOLOv5 model to detect people wearing masks, not wearing masks and incorreclty wearing masks. This script has the ability to make an access control application. Compatible with Jetson Nano.

<summary>Install</summary>

Clone the repo and install [requirements.txt](https://github.com/carolina-martinez/TFM/blob/master/requirements.txt) in a
[**Python>=3.6.9**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048).
Also 

```bash
git clone https://github.com/carolina-martinez/TFM.git  # clone
cd TFM
pip install -r requirements.txt  # install
```
If you are going to use the RFID functionality for access control, you also have to install an mqtt broker. For this, we can install mosquitto.

```bash
sudo apt update
sudo apt install -y mosquitto
```

<summary>Deploy</summary>

We can use the default YOLOv5 detector to see detections using your webcam with:

```bash
python3 detect.py --weights datasetv4_bach16_100epoch.pt --source 0
```

If you want to setup the full access control software you will have to run detect_tfm.py and RFID.py

```bash
python3 detect.py --weights datasetv4_bach16_100epoch.pt --source 0
```
Open another terminal and write:

```bash
sudo modprobe spidev #To enable SPI on the Jetson Nano
python3 RFID.py
```

This proyect is based on YOLOv5: https://github.com/ultralytics/yolov5
