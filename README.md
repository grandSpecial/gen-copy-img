# Generative Copy Image

A CLI tool that recursively edits images using OpenAI's `gpt-image-1` model to explore how the model interprets and applies iterative improvement prompts. Each iteration builds upon the previous image, creating a visual evolution of the model's decision-making process.

---

## Features

- Recursively applies improvement prompts to images using OpenAI's new image model
- Creates a visual timeline of the model's decision-making process
- Combines all generated images into an animated GIF (250ms per frame)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/gen-copy-img.git
cd gen-copy-img
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key to a `.env` file

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-key-here
```

### 4. Place your source image

Put your starting image in the `inputs/` folder (e.g., `inputs/source.jpg`).

---

## Usage

### Basic Example
```bash
python main.py inputs/source.jpg --runs 5
```
This will:
- Generate 5 iterations of the image
- Use the default prompt "Generate a copy of the attached image"
- Save the result as `outputs/videos/evolution.gif`

### Advanced Examples

#### Explore Image Improvement
```bash
python main.py inputs/source.jpg --prompt "Improve this image" --runs 50
```


### Arguments

| Argument   | Description                         | Default                                    |
| ---------- | ----------------------------------- | ------------------------------------------ |
| `source`   | Path to the source image            | —                                          |
| `--prompt` | Text prompt to apply per iteration  | `"Generate a copy of the attached image."` |
| `--runs`   | Number of image iterations to apply | `5`                                        |
| `--out`    | Output GIF file path                | `outputs/videos/evolution.gif`             |

---

## 📂 Output

* Images are saved in: `outputs/images/` (numbered 0 to N)
* Final GIF is saved in: `outputs/videos/`

Note: All images are automatically resized to match OpenAI's output dimensions to ensure consistent GIF quality.

---

## Research Use

This tool is particularly useful for:
- Studying how GPT-image-1 interprets iterative improvement prompts
- Analyzing the model's decision-making process in image generation
- Understanding the model's approach to incremental changes
- Investigating the stability and consistency of image modifications

---

## 🛠 Dependencies

* `openai`
* `tqdm`
* `opencv-python`
* `imageio`
* `python-dotenv`

Install them all via:

```bash
pip install -r requirements.txt
```

---

## License

MIT — do whatever you want.

## Contact 

Tyler Batten
info@tbat.io 
