from sys import intern
from diagrams import Diagram, Cluster

import diagrams.onprem.compute
import diagrams.onprem.network
import diagrams.onprem.monitoring
import diagrams.onprem.container
import diagrams.onprem.storage

import diagrams

graph_attr = {
    "fontsize": "20",
    "bgcolor": "white"
}

with Diagram("IT-Services Kreuzkirche", show=False, graph_attr=graph_attr):
    internet = diagrams.onprem.network.Internet("Internet")

    with Cluster("Apollo - Main Webservices Host"):
        with Cluster("Docker-Network"):
            with Cluster("Ingress/Egress"):
                nginx = diagrams.onprem.network.Nginx("NGINX-Proxymanager")
            with Cluster("OnlyOffice"):
                onlyoffice = diagrams.onprem.container.Docker("OnlyOffice")

            with Cluster("wordpress-production"):
                wordpress_production = diagrams.onprem.container.Docker("wordpress-production")
                wordpress_production_db = diagrams.onprem.container.Docker("wordpress-production-db")
            with Cluster("wordpress-staging"):
                wordpress_staging = diagrams.onprem.container.Docker("wordpress-staging")
                wordpress_staging_db = diagrams.onprem.container.Docker("wordpress-staging-db")
            with Cluster("borgmatic"):
                borgmatic = diagrams.onprem.container.Docker("borgmatic")

    internet >> nginx
    internet << nginx
    onlyoffice >> nginx
    wordpress_production_db >> wordpress_production >> nginx
    wordpress_staging_db >> wordpress_staging >> nginx
