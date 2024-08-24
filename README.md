 Xtage_DE_Assignment

The objective of this project/repository is to design and develop a resilient and scalable data engineering pipeline capable of integrating and processing data from multiple sources. The ultimate goal is to transform disparate data into a unified, standardized format, making it suitable for in-depth analysis, machine learning, or other downstream applications.

 Project Structure
1. Ingestion: Scripts for fetching data from various sources.
2. Transformation: Scripts for data transformation and standardization.
3. Pipeline: Data preprocessing pipeline implementation.
4. Deployment: Cloud architecture and deployment configurations.
5. Docs: Documentation and presentation materials.

We will go through each step in detail, covering all the techniques used.

 Ingestion

I used Python scripts to fetch data from all sources, including flat files, APIs, and a database. In the `ingestion.py` file:
- Flat files are ingested into a DataFrame.
- For API ingestion, I defined the API endpoint and authentication token, created a dictionary with the authentication token in the Authorization header, sent a GET request to the API endpoint, parsed the response as JSON, and stored it in the `exchange_rates` variable, similarly for customer data in JSON format.
- Data is also ingested from PostgreSQL, retrieving products and transactions data. The script establishes a connection to the database using the provided credentials, executes SQL queries to retrieve the data, and returns the results as tuples.

By the end of this step, we have completed the ingestion process.

 Standardization/Transformation

The `standardize_data.py` file is used to join and integrate all the CSV files into a single dataset. The script integrates and standardizes data from multiple sources (sales, products, transactions, customers, and exchange rates) into a unified format, converts date columns for consistency, and saves the final dataset to a CSV file for further analysis or reporting. This code combines data from five different files, matches them based on common columns, and converts two date columns to a standard format.

As a result, the `standardized_data` DataFrame contains a unified view of the data from all five sources, with consistent formats and data types. This file will be used for further preprocessing.

 Preprocessing

I have uploaded two Python files: `preprocess.py` and `robust_preprocess.py`. While both files perform similar tasks, the `robust_preprocess.py` code processes the data at multiple levels. It performs the following actions:
- Handling Missing Values: Fills in missing values with suitable replacements.
- Removing Duplicates: Eliminates duplicate rows to ensure each row is unique.
- Standardizing Inconsistent Data: Ensures data consistency in its format.
- Removing Abnormal Values: Removes values that are abnormal or don't make sense.
- Engineering New Features: Creates new features from existing ones.

The code loads standardized data from a file named `standardized_data.csv`, creates an instance of the `DataPreprocessor` class (which includes methods for each preprocessing step), and calls the `preprocess` method to execute all preprocessing steps in order. If any errors occur during preprocessing, they are caught and a message is printed. If preprocessing is successful, the preprocessed data is saved to a new file named `preprocessed_data.csv`.

 Cloud Hosting and Deployment

I have chosen Amazon Cloud Services (AWS) to host and deploy our pipeline for the following reasons:
- Cost Efficiency: AWS charges only for the resources we use. Since our pipeline does not run continuously, AWS is a suitable choice.
- Monitoring and Troubleshooting: AWS CloudWatch is crucial for maintaining and troubleshooting the data pipeline.
- Scalability: AWS allows for effortless scaling of our pipeline.

Services Utilized:
- AWS S3: Store raw CSV and JSON files.
- AWS Lambda: Ingest and process data.
- AWS Glue: Transform and prepare data.
- AWS RDS (PostgreSQL): Store and query structured data.
- AWS API Gateway: Expose and manage APIs.
- AWS CloudFormation/Terraform: Automate infrastructure deployment.

Pipeline Flow:
1. Data Source → Data Ingestion (S3 Bucket) → Data Standardization (AWS Lambda) → Data Preprocessing (Glue) → Data Storage (Redshift) → Data Serving (API Gateway)

 Steps to Execute AWS Pipeline

1. Log in to the AWS Management Console.
2. Navigate to the AWS Glue dashboard.
3. Click on "Jobs" in the left-hand menu.
4. Click on "Create job" and select "Python" as the job type.
5. Upload the `ingest_data.py`, `standardize_data.py`, and `preprocess_data.py` scripts to the job.
6. Configure the job to run the scripts in the correct order (e.g., ingest, standardize, preprocess).
7. Set the input and output locations for the job (e.g., S3 bucket).
8. Click "Create job" to create the job.
9. Navigate to the AWS Glue dashboard and click on "Jobs" in the left-hand menu.
10. Find the job you created and click on "Run job" to execute the pipeline.

Alternatively, we can use AWS Glue for ingestion and execute the pipeline as follows:

1. Data Ingestion:
   - CSV Files: Store in S3, then use Lambda or Glue jobs to ingest into RDS (PostgreSQL).
   - JSON Files: Store in S3, then use Lambda or Glue for ingestion.
   - APIs: Use Lambda triggered by API Gateway to fetch and process data, storing results in S3 or RDS.

2. Data Processing:
   - AWS Lambda: Triggered by S3 events or API Gateway for lightweight processing.
   - AWS Glue: Perform complex ETL tasks, standardize formats, and transform data.

3. Data Storage:
   - Amazon Redshift: Use as a data warehouse for processed datasets.

4. Data Serving:
   - AWS API Gateway: Expose APIs for external/internal access.
   - AWS Lambda: Handle API requests and serve processed data.

5. Orchestration:
   - AWS Step Functions: Coordinate and manage the entire data pipeline.

6. Monitoring and Logging:
   - Amazon CloudWatch: Monitor the pipeline and set up alerts.
   - AWS CloudTrail: Enable audit logging.

Implementation Steps:
1. Set up AWS S3: Create an S3 bucket (xtage-data-pipeline) to store CSV and JSON files.
2. Implement AWS Lambda Functions:
   - CSV Ingestion: Read CSV files from S3 and load them into RDS.
   - JSON Ingestion: Read JSON files from S3 and load them into RDS.
3. Set Up AWS RDS (PostgreSQL): Create tables matching the data schema from the provided files (e.g., sales, products, transactions, exchange_rates, customers).
4. Develop and Deploy AWS Glue Jobs:
   - Convert JSON to a tabular format.
   - Perform data transformations and standardization.
   - Combine data from different sources into a unified dataset.
5. Deploy the Pipeline Using CloudFormation/Terraform: Automate the deployment of all resources, including S3, Lambda, RDS, and Glue.

The API has been exposed to the database using the Lambda function. The Lambda function connects to a PostgreSQL database, retrieves product data, processes it into JSON format, and returns it as an HTTP response.

Belows are two step by step process to exceute the pipeline:
Deploying to AWS
1.	Create an AWS S3 bucket to store the ingested and preprocessed data.
2.	Create an AWS Glue job to run the data processing pipeline.
3.	Create an AWS API Gateway to expose the preprocessed data as a RESTful API.
4.	Update the ingest_data.py script to upload the ingested data to the S3 bucket.
5.	Update the preprocess_data.py script to upload the preprocessed data to the S3 bucket.
6.	Configure the AWS Glue job to run the pipeline scripts in the correct order.
7.	Deploy the pipeline to AWS and run the Glue job.
Running the Pipeline Locally
1.	Create a new directory for your project and navigate into it.
2.	Create the following folders: ingest_data, standardize_data, preprocess_data, and data.
3.	Create the Python scripts: ingest_data.py, standardize_data.py, and preprocess_data.py in their respective folders.
4.	Copy the code from my previous response into the corresponding files.
5.	Run the scripts in the following order:
•	python ingest_data/ingest_data.py to ingest data from all sources.
•	python standardize_data/standardize_data.py to standardize the ingested data.
•	python preprocess_data/preprocess_data.py to preprocess the standardized data.
6.	The preprocessed data will be saved to a CSV file in the data folder.


A diagrammatic flow chart of the pipeline is provided in the PPT.
-------------
