import os
import re
import subprocess
import webbrowser

import click

ENTRYPOINTS = 'powershift_cli_plugins'


def server_url():
    # XXX This is only available from Origin 1.4 onwards.
    # command = ['oc', 'whoami', '--show-server']
    # url = subprocess.check_output(command, universal_newlines=True)
    # url = url.strip()

    command = ['oc', 'config', 'view', '--minify', '-o',
            'jsonpath="{.clusters[*].cluster.server}"']

    url = subprocess.check_output(command, universal_newlines=True)
    url = re.sub(r'^\s*"(.*)"\s*$', r'\1', url)

    return url

@click.group()
@click.pass_context
def root(ctx):
    """
    PowerShift client for OpenShift.

    This client provides additional functionality useful to users of the
    OpenShift platform. Base functionality is minimal, but can be extended
    by installing additional plugins.

    For more details see:

        https://github.com/getwarped/powershift

    """

    # Check whether the 'oc' command is installed and fail if not. We
    # are so dependent on it being installed that there isn't much point
    # continuing if it isn't.

    try:
        subprocess.check_output(['oc', 'help'], stderr=subprocess.STDOUT)

    except FileNotFoundError:
        click.echo('Failed: You do not appear to have the \'oc\' command '
                'line tool installed. Please install it to continue.')
        ctx.exit(1)

    except subprocess.CalledProcessError:
        click.echo('Failed: You appear to have the \'oc\' command '
                'line tool installed, but it appears to be non functional.')
        ctx.exit(1)

@root.command()
def console():
    """
    Open a browser on the OpenShift web console.

    """

    webbrowser.open(server_url())

@root.command()
def server():
    """
    Displays the URL for the OpenShift cluster.

    """

    click.echo(server_url())

@root.group()
def completion():
    """
    Output completion script for specified shell.

    """

    pass

@completion.command()
def bash():
    """
    Output shell completion code for 'bash'.

    To generate the completion code and enable it use:

    \b
        powershift completion bash > powershift-complete.sh
        source powershift-complete.sh

    """

    directory = os.path.dirname(__file__)
    script = os.path.join(directory, 'completion-bash.sh')
    with open(script, encoding='UTF-8') as fp:
        click.echo(fp.read())

def session_context():
    command = ['oc', 'whoami', '-c']

    context = subprocess.check_output(command, stderr=subprocess.STDOUT,
            universal_newlines=True)
    context = context.strip()

    return context

def session_token():
    command = ['oc', 'whoami', '-t']

    token = subprocess.check_output(command, stderr=subprocess.STDOUT,
            universal_newlines=True)
    token = token.strip()

    return token

def session_user():
    command = ['oc', 'whoami']

    token = subprocess.check_output(command, stderr=subprocess.STDOUT,
            universal_newlines=True)
    token = token.strip()

    return token

@root.group()
def session():
    """
    Display information about current session.

    """

@session.command()
@click.pass_context
def user(ctx):
    """
    Displays name of user for active session.

    """

    try:
        click.echo(session_user())
    except subprocess.CalledProcessError as e:
        click.echo('Failed: %s' % e.stdout)
        ctx.exit(e.returncode)

@session.command()
@click.pass_context
def context(ctx):
    """
    Displays the active user session context.

    """

    try:
        click.echo(session_context())
    except subprocess.CalledProcessError as e:
        click.echo('Failed: %s' % e.stdout)
        ctx.exit(e.returncode)

@session.command()
@click.pass_context
def token(ctx):
    """
    Displays the active user session token.

    """

    try:
        click.echo(session_token())
    except subprocess.CalledProcessError as e:
        click.echo('Failed: %s' % e.stdout)
        ctx.exit(e.returncode)

def main():
    # Import any plugins for extending the available commands. They
    # should automatically register themselves against the appropriate
    # CLI command group.

    try:
        import pkg_resources
    except ImportError:
        pass
    else:
        entrypoints = pkg_resources.iter_entry_points(group=ENTRYPOINTS)

        for entrypoint in entrypoints:
            __import__(entrypoint.module_name)

    # Call the CLI to process the command line arguments and execute
    # the appropriate action.

    root(obj={})

if __name__ == '__main__':
    main()
