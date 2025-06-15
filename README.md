---
title: Abusive Comment Detection
emoji: 🔥
colorFrom: red
colorTo: green
sdk: gradio
sdk_version: 3.29.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Abusive Comment Detection

A machine learning-based system for detecting abusive comments in text. This project uses natural language processing to identify potentially harmful or inappropriate content.

## Features

- Text classification for abusive content detection
- Language detection support
- Web interface for easy interaction
- API endpoint for integration with other systems

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Abusive-Comment-Detection.git
cd Abusive-Comment-Detection
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the web application:
```bash
python app.py
```

2. Access the web interface at `http://localhost:7860`

## Project Structure

- `app.py`: Main application file with the web interface
- `language_detection.py`: Language detection functionality
- `clean.py`: Text preprocessing utilities
- `model_joblib.pkl`: Trained model for abuse detection
- `requirements.txt`: Project dependencies

## Dependencies

The project requires Python 3.7+ and the following main packages:
- gradio
- scikit-learn
- pandas
- numpy

See `requirements.txt` for the complete list of dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
