from dagster import (
    repository,
)

from tutorial import all_assets, hackernews_job, hackernews_schedule


@repository
def deploy_docker_repository():
    return [hackernews_job, all_assets, hackernews_schedule]
