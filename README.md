![NSW Department of Education logo](.github/static/nsw-doe.png)

# Welcome to NSW Department of Educatio data stack in a box 🏫

🚧 ![CI Checks](https://github.com/gwenwindflower/octocatalog/actions/workflows/ci.yml/badge.svg) 

This is an open-source, open-data data-stack-in-a-box based data from [NSW Education Data Hub](https://data.cese.nsw.gov.au/). With the push of one button you can have your own data stack!

> [!IMPORTANT]  
> Click below 👇🏼 to setup your own free data stack packed with [NSW Department of Education](https://education.nsw.gov.au/) data.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/wisemuffin/nsw-doe-data-stack-in-a-box?quickstart=1)

## Objectives
[NSW Department of Education](https://education.nsw.gov.au/) data stack in a box has two objectives:
1)	Getting humans excited about the data within the NSW Department of Education.
2)	Level up our data stack by demoing features in the data stack that we are lacking or need to improve in [NSW Department of Education](https://education.nsw.gov.au/). These demos will start the conversation on what features we want to prioritise.

## Principals
Simple one button click setting you up with your own blazingly fast data stack
Completely free 💲💲💲. 

## Audience
The project is designed to be very simple but allow you the flexibility for you to go as deep you like!
- **I want to analyse and gain insights into the data.** With the infrastructure free and deployed in one click you don’t need to worry about any implementation details. You can skip straight to analysing and training models on top of your own local warehouse.
- **Interested in modelling via SQL?** We got you covered with a environment setup for DBT.
- **Love DevOps and platform engineering?** Check out our Orchestration, CICD pipelines, and automation such as linting, data diffs ect.


## Datasets

🚧 TODO

## Key features

- seperation of business logic and i/o with dagster i/o manager
- co pilot

**Accelerate data modeling Development**

- exploritory data analysis whilst you data model! build models, test, visualise iterate in vscode ![dbt-power-users](.github/static/dbt-power-users-test-and-vis-queries.gif)
- Navigate data models with model level lineage ![Naviate data models](.github/static/dbt-power-users-quick-navigation.gif)
- [Defer to prod](https://docs.myaltimate.com/test/defertoprod/) - dont copy accross all of the prod models into dev when you can simply reference them.

[Full list of dbt accelerations from dbt power users](https://docs.myaltimate.com/)

📓 some additional features below that use AI features require a API key from [Accelerate](https://www.altimate.ai/) but in this project just using the open source free version:

<!-- > [!NOTE]  
> some additional features below that use AI features require a API key from [Accelerate](https://www.altimate.ai/) but in this project just using the open source free version: -->

| :memo:        | some additional features below that use AI features require a API key from [Accelerate](https://www.altimate.ai/) but in this project just using the open source free version:       |
|---------------|:---------------------------------------------|


- Document data models with AI ![AI docs](.github/static/dbt-altimate-ai-documentation.gif)
- Explore column level lineage and carry out impact analysis![lineage and impact analysis](.github/static/dbt-power-users-lineage-and-impact-analysis-column-lineage.gif)


**Accelerate data data ingestion**

Just create a python pandas dataframe and put that logic into the orchistrator dagster

> [!WARNING]  
> Pandas will only scale so far. But for +95% of the work we do at NSW DOE analytics its probably enough.

**testing**

🚧

**debugging**

🚧 debuggin demo


**data consumers**

🚧 data vis
🚧 data science


## Key Features - where we dont have a good open source option

**semantic/metrics layer**

🚧

**AI metrics**

🚧 AI metrics e.g. tableau


## Architecture 🥨

COMING SOON 🚧 use https://excalidraw.com/


[DuckDB](https://duckdb.org/) + [dbt](https://www.getdbt.com/) + [Evidence](https://evidence.dev/).

It offers a simple script to extract and load (EL) data from the [NSW Education Data Hub](https://data.cese.nsw.gov.au/), a dbt project built on top of this data inside a DuckDB database, and BI tooling via Evidence to analyze and present the data.

## Todo

🚧working on
- example metrics layer - saved queries vs exports
- machine learning - e.g. facebook prophecy
- why cant i preview markdown anymore?
- raw_orders_py fails when first run contains no data thus data types are all int. Then next partition with data will fail. Not a show stopper. Maybe just get a dataset with data every day to avoid this?
- auto start dagster in codespace and popup webserver but also want evidence-dev to also pop up?
  - "postStartCommand": "task dag" does this mean the codesandbox wont closed down?
  - also need to find way to stop process so can make changes whilst editing
- DOE data

🔙🪵backlog
- local reporting (evidence)
- limitation, when dbt model fails all downstream fails (i.e. if have depency on any other dbt table). To investigate.
- Motherduck upgrade to 0.10.X eta end of march
  - waiting on motherduck to 0.10.0 to get sql tools to work & backwards compatability of duckdb versions
  - this will also fix issue around lock on database when connected via sql tools then try and do etl...
  - backwards compatability
- speed up codespace by using uv as a python package manager
- dbt tests in dagster
- cube.dev
- deployment CICD
- architecture diagram use https://excalidraw.com/
- for sources show then with python key in dagster dag
- docs on taskfile
- docs on dbt power users for vscode
- setup linting and formating with black

Limitations 😢😭
- python package manager uv is so much faster but cant use in taskfile. Explore this some more
- dynamic check for dbt's manifest.json not working. For now will always parse dbt project.
- duckdb locks from different processes. Think this is solved in duckdb 0.10.0?
- pandas to duckdb io manager (see notes in jaffle shop raw_orders_py when recieves empty df then it wont use the dtypes from dataframe when building db objects. i.e. strings are getting convereted to int32...


Fixes
- failing partitions when nothing returned by df
- dagster auto start container
- duckdb_pandas_io_manager is legacy and should be replaced by  DuckDBPandasIOManager but currently getting duckdb locks so trying to figure out what caused this

## Contributing

🚧 TODO