variable "credentials" {
  description = "Project credentals"
  default     = "/Users/shubhrajitpal/Documents/Data_Zoomcamp/Terraform_demo/keys/my-creds.json"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}


variable "project_name" {
  description = "Project Name"
  default     = "terraform-setup-test"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset name"
  default     = "demodataset"
}

variable "gcs_bucket_name" {
  description = "My storage bucket name"
  default     = "terraform-setup-test-18-terra-bucket"
}

variable "gcp_storage_class" {
  description = "Storage bucket class"
  default     = "STANDARD"
}