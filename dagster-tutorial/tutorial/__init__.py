from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    repository,
    job,
)
from dagster_docker import docker_executor

from . import assets

all_assets = load_assets_from_modules([assets])

# Define a job that will materialize the assets
hackernews_job = define_asset_job(
    "hackernews_job",
    selection=AssetSelection.all(),
    executor_def=docker_executor.configured(
        image="dagster_multi_tutorial", network="public"
    ),
)

# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
hackernews_schedule = ScheduleDefinition(
    job=hackernews_job,
    cron_schedule="0 * * * *",  # every hour
)

defs = Definitions(
    assets=all_assets,
    schedules=[hackernews_schedule],
)
