import os

#--------------------------------------------------------------------------------
# Flags for different sections execution- useful for testing/retraining

# Whether to perform clustering and classification - use for retraining
perform_clustering_and_classification = False 

# Whether to validate with existing L3 data
validation_with_existing_L3_data = False      

# Whether to extract camera parameters from each cluster
extract_camera_param_from_each_cluster = True 

# Number of Camera views to be recommended for each cluster
number_of_Rcamera_views = 4 

# Minimum angle difference in degress for isometric views
min_iso_diversity_angle = 30 
#--------------------------------------------------------------------------------

# Schema definition and table names for Databricks EDL - Dummy values
SCHEMA_NAME = "dummy_schema" 
parts_render_details_table = f"{SCHEMA_NAME}.parts_render_details"
users_table = f"{SCHEMA_NAME}.users"
parts_metadata_table = f"{SCHEMA_NAME}.parts_metadata" 

#--------------------------------------------------------------------------------
# Local paths for script and other file storage locations

# Base directory for the project
script_dir = os.path.dirname(os.path.abspath(__file__))

# parts metadata csv file for clustering
metadata_csv_file= os.path.join(script_dir, "data", "parts_metadata.csv")

# clustering model location for saving and loading
clustering_model_path = os.path.join(script_dir, "models", "clustering_model.pkl")

# clustering results csv output file for classification
clustering_results_csv = os.path.join(script_dir, "output", "clustering_results.csv")

# Rendered parts details containing approved camera parameters
parts_rendering_data_csv_file = os.path.join(script_dir, "data", "approved_camera_details_for_rendered_parts.csv")

# Cluster assignment details for testing output
cluster_assignment_details = os.path.join(script_dir, "output", "cluster_assignment_details.csv")

# json output containing camera parameters extracted for each cluster
output_file_camera_details_per_cluster = os.path.join(script_dir, "output", "top_n_cameras_per_cluster.json")

#output summary : views and cluster details
output_summary = os.path.join(script_dir, "output", "output_summary.csv")
#--------------------------------------------------------------------------------

number_of_clusters_list = [30]  # List of different cluster counts to try during clustering

feature_correlation_heatmap = True # Whether to generate feature correlation heatmap

#algorithms_to_run = ['KMeans','GMM', 'DBSCAN','Agglomerative','Spectral']  # List of algorithms to run- Final run should contain 1

algorithms_to_run = ['Spectral']  # Best performing algorithm from previous experiments

#Visualization methods = ['PCA','t-SNE','UMAP'] # List of visualization methods to use

visualization_methods = ['t-SNE'] # Best performing visualization from previous experiments

results_export_option = ['Spectral']  # Export results for specific algorithms only
#--------------------------------------------------------------------------------

# Define standard isometric views

STANDARD_ISOMETRIC_VIEWS = {
    "iso_1" : {'azimuth':45.0, 'incl':35.26, 'twist':0.0},    #Classic Iso view
    "iso_2" : {'azimuth':-135.0, 'incl':35.26, 'twist':0.0},  #Oppostite ISO
    "iso_3" : {'azimuth':135.0, 'incl':35.26, 'twist':0.0},
    "iso_4" : {'azimuth':-45.0, 'incl':35.26, 'twist':0.0}
}

STANDARD_ORTHOGONAL_VIEWS = {
    'front' : {'azimuth':0.0, 'incl':0.0, 'twist':0.0}, #Front view
    'back' : {'azimuth':180.0, 'incl':0.0, 'twist':0.0}, #Back view
    'left' : {'azimuth':-90.0, 'incl':0.0, 'twist':0.0}, #Left view
    'right' : {'azimuth':90.0, 'incl':0.0, 'twist':0.0}, #Right view
    'top' : {'azimuth':0.0, 'incl':90.0, 'twist':0.0}, #Top view
    'bottom' : {'azimuth':0.0, 'incl':-90.0, 'twist':0.0}  #Bottom view
}

#--------------------------------------------------------------------------------

