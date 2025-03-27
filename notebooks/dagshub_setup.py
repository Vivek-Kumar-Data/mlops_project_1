import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/Vivek-Kumar-Data/mlops_project_1.mlflow")

dagshub.init(repo_owner='Vivek-Kumar-Data', repo_name='mlops_project_1', mlflow=True)
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)