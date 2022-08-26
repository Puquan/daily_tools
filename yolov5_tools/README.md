## <div align="center">Yolov5项目工具</div>

<details open>
<summary>数据集标签处理</summary>
1. [formatting_xml.py](./formatting_xml.py)：将乱序的xml文件格式化

2. [xml_to_yolov5-txt](./xml_to_yolov5-txt)：将xml标签文件转换成yolo训练所需要用到的txt标签文件

<summary>模型转化：onnx -> rknn</summary>

1. `generate_optDataset.py`: `python3 generate_optDataset.py`

2. `export_rknn.py`: `python3 export_rknn.py`
3. 







<summary>文件夹用途说明</summary>

- `onnx_models`: 源onnx模型文件夹，onnx模型文件是模型转化与量化中常见的中间介模型，大致可以理解和归纳为 pytroch -> onnx -> rknn。
- `rknn_optimize_image`: 存放rknn量化所需要的用到的图片，量化原理详见rknn说明文档。
- `test_xml`: 存放测试用xml后缀标签。
