# Worker Safety Monitoring Using Thermal Imaging

## Overview

This project aims to enhance safety in industrial settings by using thermal imaging to detect unauthorized human presence. By leveraging thermal cameras and machine learning models, the system can automatically monitor restricted areas, alerting personnel if a human is detected near heavy machinery where entry is prohibited.

## Features

- **Real-Time Detection:** Utilizes thermal cameras to continuously monitor areas for human presence.
- **Automated Alerts:** Instant notifications are triggered when a human is detected in restricted zones.
- **Robust in Adverse Conditions:** Effective in low-light, no-light, and visually challenging environments.
- **Scalable Solution:** Can be integrated into existing safety and surveillance infrastructure.

## Dataset

The project utilizes the **ThermalPersonDetector** dataset, comprising 8,778 samples with annotations for the "person" class. This dataset is integral for training the model to recognize human figures in thermal imagery.

## Technology Stack

- **Programming Language:** Python
- **Machine Learning Framework:** PyTorch
- **Object Detection Model:** YOLOv5
- **Image Processing:** OpenCV
- **Deployment:** Compatible with edge deployment on thermal camera systems

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   cd FiftyHackathon
   ```

2. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   - Check folder

4. **Download Dataset:**
   - Obtain the ThermalPersonDetector dataset and place it in the `data/` directory. Make sure the dataset is properly annotated with bounding boxes for training.

5. **Train the Model:**
   - Fine-tune the YOLOv5 model using the provided dataset.
   - Training scripts and configurations can be found in the `scripts/` directory.


## Usage

- The system is designed to operate in real-time, detecting and alerting stakeholders through visual/sound notifications or system alerts when unauthorized human presence is detected.

## Future Work

- **Enhanced Accuracy:** Continue improving detection accuracy by integrating additional datasets.
- **Integration:** Develop plugins or APIs to integrate with more comprehensive safety solutions.
- **Scalability:** Implement distributed processing for large-scale deployments.

## Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or suggestions, please contact [Aishwarya Dekhane - adekhane@umich.edu - Track (A)  
Atharva Pore - atharva@umich.edu - Track (A)  
Kritika Sharma - kritish@umich.edu - Track (A)](mailto:adekhane@umich.edu).

