from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    model = YOLO(r'ultralytics\cfg\models\ours\yolov8-LFEM-MSCH-LDown.yaml') # build a new model from YAML
    model.info()

