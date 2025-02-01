
# EPLM-YOLO: Effective plug-and-play lightweight modules for YOLO series models


## Introduction

The increase of lightweight models based on the YOLO architecture has been a
notable trend in recent years. However, most of these models are designed for
specific application scenarios, often requiring researchers to redesign lightweight
models for different scenarios, thereby increasing development costs. To address
this challenge, this paper proposes an efficient lightweight strategy that can
be integrated into existing YOLO models, eliminating the need for network
architecture redesign.

Our lightweight strategy consists of three modules:
1. **Lightweight Feature Extraction Module (LFEM):** Enhances feature extraction efficiency in the backbone network by generating potentially redundant feature maps through standard convolution.
2. **Multi-Feature Shared Convolution Module (MSCH):** Reduces the number of parameters in the detection head using shared convolutional layers.
3. **Feature Segmentation and Sparse Optimization Module (LDown):** Performs feature segmentation during downsampling and incorporates the NAM attention mechanism to effectively utilize sparse feature information.

To validate the effectiveness of this strategy, we applied it to various YOLO models, including YOLOv5, YOLOv6, YOLOv8, YOLOv10, YOLO-lite, SPDConv, YOLO-Drone, Hyper-YOLO, RCS-YOLO, and ASF-YOLO. Experiments conducted on the DOTA, Pascal VOC2012, and TZ-Plane datasets demonstrate that our proposed lightweight strategy significantly reduces computational complexity while maintaining detection performance.

[//]: # (## Features)

[//]: # ()
[//]: # (- **Lightweight Design:** Easily integrates into existing YOLO models without requiring architectural redesign.)

[//]: # (- **High Adaptability:** Compatible with various YOLO models and diverse object detection scenarios.)

[//]: # (- **High Performance:** Reduces computational complexity while preserving detection accuracy.)

## Supported Datasets

We validated our strategy on the following datasets:
- **DOTA:** A high-resolution dataset for object detection in remote sensing imagery.
- **Pascal VOC2012:** A classic object detection dataset.
- **TZ-Plane:** A dataset for airplane detection tasks.

## Environment Setup

Ensure the following dependencies are installed:

- Python >= 3.8
- PyTorch >= 1.8
- CUDA >= 10.2 (if GPU support is required)

Install other dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

[//]: # (## Training and Testing the Model)

[//]: # ()
[//]: # (### 1. Data Preparation)

[//]: # ()
[//]: # (Download and extract the target detection datasets &#40;e.g., DOTA, Pascal VOC2012, or TZ-Plane&#41; to the specified directory.)

[//]: # ()
[//]: # (### 2. Train the Model)

[//]: # ()
[//]: # (Run the following command to start training:)

[//]: # ()
[//]: # (```bash)

[//]: # (python train.py --data ./data/dataset.yaml --cfg ./models/yolo_model.yaml --weights ./weights/pretrained.pt --epochs 100)

[//]: # (```)

[//]: # ()
[//]: # (**Parameters:**)

[//]: # (- `--data`: Path to the dataset configuration file.)

[//]: # (- `--cfg`: Path to the YOLO model configuration file.)

[//]: # (- `--weights`: Path to the pretrained weights &#40;optional&#41;.)

[//]: # (- `--epochs`: Number of training epochs.)

[//]: # ()
[//]: # (### 3. Test the Model)

[//]: # ()
[//]: # (Run the following command to test the model:)

[//]: # (```bash)

[//]: # (python test.py --data ./data/dataset.yaml --weights ./weights/trained_model.pt)

[//]: # (```)

## Integrating the Lightweight Strategy

To integrate the lightweight strategy into other YOLO models, include the following modules in the model architecture:

- **LFEM**
- **MSCH**
- **LDown**

Refer to the `models/` directory and code annotations for detailed instructions.

## Experimental Results

We conducted comparative experiments on different datasets and models. For detailed experimental results, please refer to our paper.

## License

This project is open-sourced under the MIT License.

## Contact

For any questions, please contact us via [GitHub Issues](https://github.com/lixiaobai-star/EPLM-YOLO/issues).


