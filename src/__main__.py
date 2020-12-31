import os
import sys
import click
import pytest

@click.group()
def cli():
    return None


@click.group(name="system")
def system_group():
    return None


@system_group.command(name="version")
def version_command():
    print("not implemented")


@system_group.command(name="selftest")
def selftest_command():
    print("not implemented")


@system_group.command(name="selfcoverage")
def selfcoverage_command():
    print("not implemented")


cli.add_command(system_group)
main = cli
