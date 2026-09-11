# Course Title

Course materials and Python environment.

## Installation

Clone the repository:

    git clone git@github.com:cheuchenne/course-name.git

Move into the repository:

    cd course-name

Create the Python environment:

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

Install the required packages:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

Install the Jupyter kernel:

    python -m ipykernel install --user \
      --name course-name \
      --display-name "Python (course-name)"
      
## Using VS Code

Open the course folder in VS Code.

For Jupyter notebooks:

1. Open a `.ipynb` file.
2. Select the `Python (course-name)` kernel.
3. Run the cells.

For Quarto documents:

1. Open a `.qmd` file.
2. Execute Python cells.
3. Render the document with Quarto.
