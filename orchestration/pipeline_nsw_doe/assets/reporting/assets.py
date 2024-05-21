import subprocess

from dagster import asset, file_relative_path

from ..semantic_layer.assets import (
    metrics_by_year_saved_query,
    metrics_by_year_school_saved_query,
)


@asset(
    compute_kind="evidence",
    group_name="reporting",
    deps=[metrics_by_year_saved_query, metrics_by_year_school_saved_query],
)
def evidence_dashboard__experimental():
    """
    Dashboard built using Evidence showing Duck metrics.
    Dashboard generation is declared via an asset
    Source queries are downloaded locally and cached as parquet
    Static HTML/JS web pages built for high performance leveraging duckdb and WASM.
    This isnt really to do with data and its a bit of a hack to do a bit of CICD locally.
    example over at: https://github.com/dagster-io/devrel-project-demos/blob/main/motherduck-dagster-hybrid-compute/motherduck_dagster_hybrid/assets.py#L239

    For demos still using `npm run dev` instead of waiting for static files to be built (webpack budling ect)

    *TODO 🚧 also getting an error: `FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory` but succeeding in dagster.
    """
    evidence_project_path = file_relative_path(__file__, "../../../../reports")
    subprocess.run(["npm", "--prefix", evidence_project_path, "install"])
    subprocess.run(["npm", "--prefix", evidence_project_path, "run", "sources"])
    # dont waste time building static site, just do this in CICD step and host on static website
    # subprocess.run(["npm", "--prefix", evidence_project_path, "run", "build"])


@asset(
    compute_kind="tableau",
    group_name="reporting",
    deps=[metrics_by_year_saved_query, metrics_by_year_school_saved_query],
)
def tableau_dashboard__experimental():
    """
    🚧 to work on setting up automated refresh of cache on tableau public
    """
    pass


@asset(
    compute_kind="powerbi",
    group_name="reporting",
    deps=[metrics_by_year_saved_query, metrics_by_year_school_saved_query],
)
def powerbi_dashboard__experimental():
    """
    🚧 to work on setting up automated refresh of cache on power bi
    """
    pass
