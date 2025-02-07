from diagrams import Cluster, Diagram
from diagrams.generic.storage import Storage
from diagrams.generic.compute import Rack
from diagrams.generic.database import SQL
from diagrams.onprem.queue import Kafka
from diagrams.programming.language import Python

with Diagram("Scalable Similarity Score Pipeline", show=False):
    # Data Ingestion and Preprocessing
    with Cluster("Data Ingestion"):
        data_source = Storage("Data Source")
        streaming_queue = Kafka("Streaming Queue")
    
    with Cluster("Data Preprocessing"):
        batch_processor = Rack("Batch Processor")
        data_cleaner = Python("Cleaning & Transformation")

    # Vector Embeddings
    with Cluster("Embeddings Service"):
        model_server = Rack("Embedding Model Server")
        embedding_model = Python("Pretrained Embeddings")

    # Data Storage
    with Cluster("Data Storage"):
        vector_database = SQL("Vector Database")
        cache_store = SQL("Cache (Frequent Results)")
        similarity_database = SQL("Similarity Scores Database")

    # Processing and Real-time Scoring
    with Cluster("Real-time Processing"):
        embedding_service = Rack("Embedding Service")
        similarity_calculator = Rack("Similarity Calculator")
    
    # Workflow connections
    data_source >> batch_processor >> data_cleaner >> vector_database
    data_cleaner >> embedding_model >> embedding_service
    embedding_service >> vector_database >> similarity_calculator >> similarity_database
    similarity_calculator >> cache_store
    streaming_queue >> similarity_calculator
