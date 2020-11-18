# EDA𝑥: Task-Centric Exploratory Data Analysis for Statistical Modeling in Python

## Ducumentation
The documentation and examples could be found in https://edatechreport.github.io/edax/.

## Daily Downloads
![Daily Downloads](daily_downloads.png)

## Stars
![Stars](stars.png)


## Library Demo
In this 50 seconds demo we show how to get an overview of the data, doing correlation analysis
and missing value analysis using just one line of code.

![eda demo](EDAx.gif)

## Experiment Setup

### Dependency Installation
The host machine should have the following libraries/packages/binaries installed.

- [Just](https://github.com/casey/just)
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

### Dataset Preparation
First, download the dataset from the links and rename the dataset to `<dataset-name>.csv`
according the dataset column in the [dataset description](dataset.pdf).
All the datasets should be put under `benchmark/data` folder.

### Docker Image Preparation
Under the project root, run `just build-docker` to build the docker image.

## Reproduce Table 1
1. The result of Table 1 can be directly calculated from the data in [`benchmark/results/report.json`](benchmark/results/report.json).
2. The following steps rerun the experiment.
3. Remove the `.disabled` extension for file `benchmark/benchmarks/create_report_edax.py.disabled` and `benchmark/benchmarks/create_report_pp.py.disabled`.
4. Execute `just bench benchmark/results/report.json` to run the experiment for Table 1.
   This will **append** experiment results to `benchmark/results/report.json`. Clear the file content before running the experiment if you want a fresh start.
5. Go back to step 1.

## Reproduce Figure 6
1. The result of Figure 6 can be generated by executing the notebook [`notebooks/self_comparison_overview.ipynb`](https://nbviewer.jupyter.org/github/edatechreport/edax/blob/master/notebooks/self_comparison_overview.ipynb)
2. The following steps rerun the experiment.
3. Add back the `.disabled` extension for all the files under `benchmark/benchmarks/` except for `lib.py`.
4. For each of `benchmark/benchmarks/{plot, plot_correlation, plot_missing}.py.disabled`,
   remove the `.disabled` extension and execute `just bench benchmark/results/{function_name}.json` to run the experiments for each plot function.
   This will **append** experiment results to `benchmark/results/{function_name}.json`. Clear the file content before running the experiment if you want a fresh start.
5. Go back to step 1.

## Reproduce Figure 7
1. The result of Figure 7 can be generated by executing notebook [`notebooks/self_comparison_subfunctions.ipynb`](https://nbviewer.jupyter.org/github/edatechreport/edax/blob/master/notebooks/self_comparison_subfunctions.ipynb)
2. The following steps rerun the experiment.
3. Add back the `.disabled` extension for all the files under `benchmark/benchmarks/` except for `lib.py`.
4. For each of `benchmark/benchmarks/{plot, plot_correlation, plot_missing}_*.py.disabled`,
   remove the `.disabled` extension and execute `just bench benchmark/results/{function_name}.json` to run the experiments for each plot function.
   This will **append** experiment results to `benchmark/results/{function_name}.json`. Clear the file content before running the experiment if you want a fresh start.
5. Go back to step 1.

## Reproduce Figure 8
The result data for user study is in [`benchmark/results/userstudy.csv`](benchmark/results/userstudy.csv)
Run [`notebooks/EDA SIGMOD User Study.ipynb`](https://nbviewer.jupyter.org/github/edatechreport/edax/blob/master/notebooks/EDA%20SIGMOD%20User%20Study.ipynb) to generate the figure.

## Repo Structure

- benchmark: experiment codes and data.
- edax: edax library.
- notebook: notebooks to generate the figures.
