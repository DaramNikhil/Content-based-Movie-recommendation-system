
<p align="center">
    <h1 align="center">CONTENT-BASED-MOVIE-RECOMMENDATION-SYSTEM</h1>
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

<code>► This repository hosts a small-scale implementation of a content-based movie recommendation system. Unlike collaborative filtering methods that rely on user interactions, content-based recommendation systems suggest items similar to those a user has liked based on the item's features.</code>

---


##  Repository Structure

```sh
└── Content-based-Movie-recommendation-system/
    ├── AUTHORS.rst
    ├── CONTRIBUTING.rst
    ├── HISTORY.rst
    ├── LICENSE
    ├── MANIFEST.in
    ├── Movie_recommendation_system
    │   ├── Movie_recommendation_system.py
    │   ├── __init__.py
    │   └── cli.py
    ├── README.md
    ├── app.py
    ├── data_dev
    │   ├── __pycache__
    │   ├── clean_data.py
    │   └── model_train.py
    ├── docs
    │   ├── Makefile
    │   ├── authors.rst
    │   ├── conf.py
    │   ├── contributing.rst
    │   ├── history.rst
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── make.bat
    │   ├── readme.rst
    │   └── usage.rst
    ├── movies.pkl
    ├── pipeline
    │   ├── __pycache__
    │   ├── model_dev_pipeline.py
    │   └── train_pipeline.py
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── src
    │   ├── __pycache__
    │   ├── ingestion.py
    │   ├── model_training.py
    │   ├── notebook
    │   └── preprocess.py
    ├── tests
    │   ├── __init__.py
    │   └── test_Movie_recommendation_system.py
    └── tox.ini
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                                          | Summary                         |
| ---                                                                                                                           | ---                             |
| [AUTHORS.rst](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/AUTHORS.rst)           | <code>► INSERT-TEXT-HERE</code> |
| [CONTRIBUTING.rst](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/CONTRIBUTING.rst) | <code>► INSERT-TEXT-HERE</code> |
| [setup.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/setup.py)                 | <code>► INSERT-TEXT-HERE</code> |
| [app.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/app.py)                     | <code>► INSERT-TEXT-HERE</code> |
| [MANIFEST.in](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/MANIFEST.in)           | <code>► INSERT-TEXT-HERE</code> |
| [requirements.txt](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/requirements.txt) | <code>► INSERT-TEXT-HERE</code> |
| [HISTORY.rst](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/HISTORY.rst)           | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>data_dev</summary>

| File                                                                                                                               | Summary                         |
| ---                                                                                                                                | ---                             |
| [model_train.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/data_dev/model_train.py) | <code>► INSERT-TEXT-HERE</code> |
| [clean_data.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/data_dev/clean_data.py)   | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>Movie_recommendation_system</summary>

| File                                                                                                                                                                                  | Summary                         |
| ---                                                                                                                                                                                   | ---                             |
| [Movie_recommendation_system.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/Movie_recommendation_system/Movie_recommendation_system.py) | <code>► INSERT-TEXT-HERE</code> |
| [cli.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/Movie_recommendation_system/cli.py)                                                 | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>src</summary>

| File                                                                                                                                | Summary                         |
| ---                                                                                                                                 | ---                             |
| [model_training.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/src/model_training.py) | <code>► INSERT-TEXT-HERE</code> |
| [preprocess.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/src/preprocess.py)         | <code>► INSERT-TEXT-HERE</code> |
| [ingestion.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/src/ingestion.py)           | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>src.notebook</summary>

| File                                                                                                                           | Summary                         |
| ---                                                                                                                            | ---                             |
| [main.ipynb](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/src/notebook/main.ipynb) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>pipeline</summary>

| File                                                                                                                                             | Summary                         |
| ---                                                                                                                                              | ---                             |
| [model_dev_pipeline.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/pipeline/model_dev_pipeline.py) | <code>► INSERT-TEXT-HERE</code> |
| [train_pipeline.py](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/master/pipeline/train_pipeline.py)         | <code>► INSERT-TEXT-HERE</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the Content-based-Movie-recommendation-system repository:
>
> ```console
> $ git clone https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd Content-based-Movie-recommendation-system
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run Content-based-Movie-recommendation-system using the command below:
> ```console
> $ python main.py
> ```

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/issues)**: Submit bugs found or log feature requests for the `Content-based-Movie-recommendation-system` project.
- **[Submit Pull Requests](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/DaramNikhil/Content-based-Movie-recommendation-system.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/DaramNikhil/Content-based-Movie-recommendation-system.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=DaramNikhil/Content-based-Movie-recommendation-system.git">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.
