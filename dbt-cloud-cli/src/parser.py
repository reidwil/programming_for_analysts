"""
Parse input arguments and route messages to necessary places

This is a place we can place different command calls to finally be called in github actions
"""
import argparse

parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument(
    "--run",
    action="store_true",
    help="""
    [D]efault command. This command will send a ping to jetBlue's dbt cloud's api instance.
    The dbt job is set to test the current change (in github branch) with the target branches
    dbt database environment. :)
    """,
)

parser.add_argument(
    "--stop-run",
    type=int,
    help="""
    Sends a stop request to stop running a current job
    """
)

parser.add_argument(
    "--get-run",
    type=int,
    help="""
    Get the information about a specific run id
    """
)

parser.add_argument(
    "-q",
    "--quiet",
    action="store_true",
    default=False,
    help="""
    Quietly run results. Defaults to False
    """
)

parser.add_argument(
    "-d",
    "--debug",
    action="store_true",
    help="""
    Internal comman[d] to debug code. When calling this, the run will not ping api but rather
    return code and verbose logs (if they exist).
    """,
)
parser.add_argument(
    "--trigger-job",
    type=int,
    help="""
    Trigger Job relative to a job id.
    """,
)

parser.add_argument(
    "-p",
    "--poll",
    action="store_true",
    default=False,
    help="""
    Poll can be appended to a trigger job to run to return the status every 10 seconds.
    """
)

parser.add_argument(
    "--get-run-result",
    type=int,
    help="""
    Get the run results of a run_id.
    """
)

args = parser.parse_args()
