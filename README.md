<div align="center">
<h1 align="center">
<img src="https://www.pcworld.com/wp-content/uploads/2023/04/microsoft_excel_logo_primary_resized2-100726640-orig-3.jpg?quality=50&strip=all&w=1024" width="100" />
<br>Excel Data Search</h1>
<h3>◦ Find and fetch with ease!</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style&logo=NumPy&logoColor=white" alt="NumPy" />
</p>
<img src="https://img.shields.io/github/license/aroproduction/excel_data_search?style&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/aroproduction/excel_data_search?style&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/aroproduction/excel_data_search?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/aroproduction/excel_data_search?style&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running excel_data_search](#-running-excel_data_search)
    - [🧪 Tests](#-tests)
- [🛣 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project provides a GUI application that allows users to search for keywords in an Excel file. The application loads the data into a dataframe, performs searches based on user input, and displays the results in a treeview widget. The core functionalities of the project include selecting search columns, navigating through the results with a scrollbar, and providing a user-friendly interface for efficient data searching. This project aims to streamline the process of finding specific information in large Excel datasets, enhancing productivity and reducing manual effort.

---

## 📦 Features

Search and filter out data seamlessly out of excel(or csv) files.

---


## 📂 Repository Structure

```sh
└── excel_data_search/
    ├── .gitattributes
    ├── .gitignore
    ├── problemStatements.xlsx
    ├── requirements.txt
    └── search.py
```


---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                       |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                           |
| [search.py](https://github.com/aroproduction/excel_data_search/blob/main/search.py)               | This code allows users to search for keywords in an Excel file using a GUI application. It loads the data into a dataframe, performs searches based on user input, and displays the results in a treeview widget. The code also includes options for selecting search columns and a scrollbar for navigation. |
| [requirements.txt](https://github.com/aroproduction/excel_data_search/blob/main/requirements.txt) | The code requires specific versions of external libraries (et-xmlfile, numpy, openpyxl, pandas, python-dateutil, pytz, six, tzdata) to be installed.                                                                                                                                                          |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ Python`

`- ℹ️ Pip`

### 🔧 Installation

1. Clone the excel_data_search repository:
```sh
git clone https://github.com/aroproduction/excel_data_search
```

2. Change to the project directory:
```sh
cd excel_data_search
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🤖 Running excel_data_search

```sh
python search.py
```

### 🧪 Tests
```sh
pytest
```


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 👏 Acknowledgments

`- ℹ️ ChatGPT`

`- ℹ Google`

[↑ Return](#Top)

---
