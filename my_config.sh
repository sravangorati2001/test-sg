export SG_ROLE=arn:aws:iam::992382664147:role/awssagemaker #An AWS IAM Role with Full SG Access (I give full S3 Access too fwiw )
export WORK_DIRECTORY=data #the name of your local data_dir, i.e., data
export PREFIX="DEMO-scikit-iris-gus" #the prefix you want for you S3 bucket e.g., DEMO-scikit-iris-gus
export FRAMEWORK_VERSION="1.0-1"
export SCRIPT_PATH=train.py
export INSTANCE_TYPE="ml.m5.large" #the instance size you want to use, i.e., ml.m5.large