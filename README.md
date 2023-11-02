# Template Python Project

- **Understanding the standard project structure**: This includes the organization of directories, such as source code, tests, documentation, among others.

- **Standard structures in data projects**: We will refactor the project using classes, modules, and best practices in an ETL.

- **Familiarizing with development tools**: We will cover the use of virtual environments and discuss tools like PIP, CONDA, and POETRY.

- **Testing with Pytest**: Ensure that your code works as expected by creating unit and integration tests.

- **Version control with Git and GitHub**: Learn how to version your project and use GitHub for collaboration and publishing.

- **Documentation with MKDocs**: You will learn how to document your project with MKDocs and publish your documentation on [GitHub Pages](https://phillipefs.github.io/template-python-project).

- **Automation and CI/CD**: Set up continuous integration and delivery routines to maintain project quality.

## Getting Started

### Prerequisites

- **VSCode**: It is the code editor we will use in the workshop. [Instructions for installing VSCode here](https://code.visualstudio.com/download).

- **Git and GitHub**:

  1. You must have Git installed on your machine. [Git installation instructions here](https://git-scm.com/book/en/v2).
  2. You must also have a GitHub account. [GitHub account creation instructions here](https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account).
  3. If you are a Windows user, I recommend this video: [YouTube](https://www.youtube.com/watch?v=_hZf1teRFNg).
  4. Basic Git and GitHub tutorial [Ebook](https://www.linkedin.com/feed/update/urn:li:activity:7093915148351864832/?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity:7093915148351864832%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29&originTrackingId=4GUdvXH4TK%2BtZtlNHmiqJA%3D%3D).
  5. If you are already a Git user, I recommend the Akita video: [YouTube](https://www.youtube.com/watch?v=6Czd1Yetaac).

- **Pyenv**: It is used to manage Python versions. [Pyenv installation instructions here](https://github.com/pyenv/pyenv#installation). In this project, we will use Python 3.11.5. For Windows users, it is recommended to watch this tutorial [YouTube](https://www.youtube.com/watch?v=TkcqjLu1dgA).

- **Poetry**: This project uses Poetry for dependency management. [Poetry installation instructions here](https://python-poetry.org/docs/#installation). If you are a Windows user, I recommend watching this video: [YouTube](https://www.youtube.com/watch?v=BuepZYn1xT8), which installs Python, Poetry, and VSCode. But a simple `PIP INSTALL POETRY` command will also work.

### Installation and Configuration

1. Clone the repository:

```bash
git clone https://github.com/phillipefs/template-python-project.git
cd template-python-project
```

2. Set the correct Python version with pyenv:

```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

3. Install project dependencies:

```bash
poetry install
```

4. Activate the virtual environment:

```bash
poetry shell
```

5. Run tests to ensure everything is working as expected:

```bash
task test
```

6. Run the command to view the project documentation:

```bash
task doc
```

7. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
task run
```

8. Run the pipeline execution command to perform the ETL:

## Contact

For questions, suggestions, or feedback:

* **Phillipe Santos** - [phillipefs@msn.com](mailto:phillipefs@msn.com)