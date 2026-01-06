# Manim Animation Project

This project uses Manim to create mathematical animations and presentations.

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the animations:
```bash
manim -pql main.py SceneName
```

For presentations with manim-slides:
```bash
manim-slides render SceneName presentation.py
manim-slides present SceneName
```

## Project Structure

- `main.py` - Main animation scenes
- `ecommerce_slides.py` - E-commerce presentation slides
- `full_presentation.py` - Full presentation scenes
- `media/` - Generated animation outputs (not tracked in git)
- `slides/` - Generated slide presentations (not tracked in git)
