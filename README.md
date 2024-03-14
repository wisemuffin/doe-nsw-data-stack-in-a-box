# DOE NSW data stack in a box 📊

## Todo

🚧working on
- CESE data

🔙🪵backlog
- Motherduck
- cube.dev
- deployment CICD
- architecture diagram use https://excalidraw.com/
- for sources show then with python key in dagster dag
- docs on taskfile
- docs on dbt power users for vscode
- setup linting and formating with black


## Key features

- seperation of business logic and i/o with dagster i/o manager
- speed up data ingestion development with dataframe strait to delta via dagster i/o manager
- standardised and well known transformation framework with dbt's integration with fabric warehouse




## Architecture 🥨

COMING SOON 🚧 use https://excalidraw.com/

transformations with:
- dbt
- pyspark
- sql stored procs
- dataflows gen 2

# Tooling

## Orchistration

COMING SOON 🚧



### .env dagster

TODO: want to make the DAGSTER_HOME dynamic

in ./cese_dia_dagster/cese_dia_dagster is an .env file
change DAGSTER_HOME to your location (has to be absoloute path for local dev)


note if a dagster.yml file exists in DAGSTER_HOME location then dagster will use that for instance config.

## dbt 
### new to dbt?
For more information on dbt:
- Read the [introduction to dbt](https://docs.getdbt.com/docs/introduction).
- Read the [dbt viewpoint](https://docs.getdbt.com/docs/about/viewpoint).
- Join the [dbt community](http://community.getdbt.com/).

### dbt documentation 📃

Generate documentation for the project:
```bash
$ dbt docs generate
```

View the documentation for the project:
```bash
$ dbt docs serve
```


# Debugging


## debuging end to end with dagit UI
simply run the dagit ui in debug mode in vscode via .vscode/launch.json:

```json
{
    "version": "0.2.0",
    "configurations": [
      {
        "name": "Dagster: Debug Dagit UI",
        "type": "python",
        "request": "launch",
        "module": "dagster",
        "justMyCode": false,
        "args": ["dev",
                    "-f",
                    "${workspaceFolder}/cese_dia_dagster/cese_dia_dagster/definitions_example_delta_azure.py"
            ],
        "envFile": "${workspaceFolder}/.env"
      }
    ]
  }
```

## local debuging without the UI

This way we skip spinning up the dagster UI saving time when developing. But we still want to test with the dagit UI before deployment.

You just need to change which assets you want run in `./debug`

debug mode in vscode via .vscode/launch.json:

```json
{
    "version": "0.2.0",
    "configurations": [
    {
      "name": "Dagster: debug with .debug.py",
      "type": "python",
      "request": "launch",
      "cwd": "${workspaceFolder}/cese_dia_dagster",
      "module": "debug",
      "justMyCode": false,
      "envFile": "${workspaceFolder}/.env",
    },
}
```


# updating dagster

```bash
 pip install dagster==1.6.0 dagster-webserver==1.6.0 dagster-dbt==0.22.0 dagster-duckdb==0.22.0 dagster-duckdb-pyspark==0.22.0 dagster-duckdb-pandas==0.22.0 dagster-deltalake-pandas==0.22.0 dagster-aws==0.22.0
 ```


