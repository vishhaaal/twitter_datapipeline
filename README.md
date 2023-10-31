
# Twitter Data Pipeline using Apache Airflow

## Overview

This project demonstrates how to set up a data pipeline with Apache Airflow to collect Twitter data through the Twitter API and save it as a CSV file. This README provides an overview of the project, including its purpose, setup, and usage.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Prerequisites

Before using this Twitter data pipeline, ensure you have the following prerequisites:

- [Python](https://www.python.org/) (3.x recommended)
- [Apache Airflow](https://airflow.apache.org/)
- [Tweepy](https://www.tweepy.org/) - Python library for Twitter API
- Twitter API credentials (consumer key, consumer secret, access key, access secret)
- A Twitter developer account with access to Twitter API

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/vishhaaal/twitter_datapipeline.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the pipeline, make sure to configure your Twitter API credentials in the `config.py` file. Update the following variables with your own credentials:

- `CONSUMER_KEY`
- `CONSUMER_SECRET`
- `ACCESS_KEY`
- `ACCESS_SECRET`

## Usage

1. Start Apache Airflow by running:

   ```bash
   airflow webserver -p 8080
   ```

   Access the Airflow web interface at `http://localhost:8080`.

2. Run the Twitter data pipeline DAG by triggering it from the Airflow web interface.

3. The pipeline will collect Twitter data and save it as a CSV file in the specified output directory.

## Project Structure

- `dags/`: Contains the Apache Airflow DAG file.
- `scripts/`: Python scripts for collecting and processing Twitter data.
- `requirements.txt`: List of Python packages required for the project.

